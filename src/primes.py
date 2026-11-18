"""Outils de la partie C : périmètre, primes d'équipements (naïve, comparable, régression)."""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def perimetre_logements_entiers(df, col_active=None):
    """Logements entiers avec un prix publié (> 0), et actifs si col_active est fournie."""
    masque = (
        df["room_type"].astype(str).str.lower().str.contains("entire")
        & df["price"].notna()
        & (df["price"] > 0)
    )
    if col_active is not None:
        masque &= df[col_active].fillna(False).astype(bool)
    return df[masque].copy()


def ajouter_classe_capacite(df):
    """Classes de capacité de l'annexe E : 1-2, 3-4, 5-6, 7+."""
    sortie = df.copy()
    sortie["classe_capacite"] = pd.cut(
        sortie["accommodates"], bins=[0, 2, 4, 6, 100], labels=["1-2", "3-4", "5-6", "7+"]
    )
    return sortie


def prime_naive(df, equipement, mesure):
    """Écart relatif des médianes : annonces équipées contre non équipées."""
    medianes = df.groupby(equipement)[mesure].median()
    if True not in medianes.index or False not in medianes.index or medianes[False] == 0:
        return None
    return medianes[True] / medianes[False] - 1


def _effectifs(df, equipement, groupe):
    return df.groupby(groupe, observed=True)[equipement].agg(equipes="sum", total="count")


def classes_valides(df, equipement, groupe="classe_capacite", minimum=10):
    """Nombre de groupes ayant au moins `minimum` annonces équipées et non équipées."""
    eff = _effectifs(df, equipement, groupe)
    return int(((eff["equipes"] >= minimum) & (eff["total"] - eff["equipes"] >= minimum)).sum())


def prime_comparable(df, equipement, mesure="estimated_revenue_l365d",
                     groupe="classe_capacite", minimum=10):
    """Écart relatif moyen de la mesure, à l'intérieur de groupes homogènes (annexe E)."""
    medianes = (
        df.groupby([groupe, equipement], observed=True)[mesure].median().unstack()
        .reindex(columns=[False, True])
    )
    effectifs = _effectifs(df, equipement, groupe)
    valides = (effectifs["equipes"] >= minimum) & (effectifs["total"] - effectifs["equipes"] >= minimum)
    if not valides.any():
        return None
    ecarts = (medianes[True] / medianes[False] - 1)[valides]
    poids = effectifs.loc[valides, "total"]
    return (ecarts * poids).sum() / poids.sum()


def prime_regression(df, colonnes_equipements, cible="price"):
    """Prime en % de chaque équipement : exp(coefficient) - 1 sur log(prix) (annexe E)."""
    besoin = [cible, "accommodates", "bedrooms", "neighbourhood_cleansed"] + list(colonnes_equipements)
    base = df.dropna(subset=besoin)
    base = base[base[cible] > 0]
    X = pd.concat(
        [
            base[list(colonnes_equipements)].astype(int),
            base[["accommodates", "bedrooms"]],
            pd.get_dummies(base["neighbourhood_cleansed"], prefix="q", drop_first=True).astype(int),
        ],
        axis=1,
    )
    modele = LinearRegression().fit(X, np.log(base[cible]))
    return pd.Series(
        np.exp(modele.coef_[: len(colonnes_equipements)]) - 1, index=list(colonnes_equipements)
    )


def tableau_primes(df, equipements, prix="price", revenu="estimated_revenue_l365d"):
    """Tableau final de C1 : part équipée et primes selon les trois méthodes."""
    df = ajouter_classe_capacite(df) if "classe_capacite" not in df else df
    regression = prime_regression(df, equipements, cible=prix)
    lignes = []
    for eq in equipements:
        lignes.append({
            "equipement": eq,
            "part_equipees": df[eq].mean(),
            "naive_prix": prime_naive(df, eq, prix),
            "naive_revenu": prime_naive(df, eq, revenu),
            "comparable_prix": prime_comparable(df, eq, prix),
            "comparable_revenu": prime_comparable(df, eq, revenu),
            "regression_prix": regression[eq],
        })
    return pd.DataFrame(lignes).set_index("equipement")
