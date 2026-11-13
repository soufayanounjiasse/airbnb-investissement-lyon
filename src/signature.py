# Fonction signature de l'annexe A de l'énoncé, copiée sans modification.
# Seul ajout : l'import de display, absent hors Jupyter par défaut.
import hashlib
import pandas as pd
from IPython.display import display


def signature(df, nom):
    """Résumé détaillé et empreinte d'une table nettoyée."""
    copie = df.copy()
    for col in copie.columns:
        # les listes (ex. amenities) sont converties en texte pour pouvoir être résumées
        if copie[col].map(lambda v: isinstance(v, (list, dict, set, tuple))).any():
            copie[col] = copie[col].map(str)
    empreinte = hashlib.md5(
        pd.util.hash_pandas_object(copie.astype(str), index=False).values.tobytes()
    ).hexdigest()
    print(f"=== Signature : {nom} ===")
    print(f"Lignes : {copie.shape[0]} Colonnes : {copie.shape[1]}")
    print(f"Empreinte MD5 : {empreinte}")
    resume = pd.DataFrame({
        "type": copie.dtypes.astype(str),
        "manquants": copie.isna().sum(),
        "pct_manquants": (copie.isna().mean() * 100).round(2),
        "valeurs_distinctes": copie.nunique(),
    })
    display(resume)
    numeriques = copie.select_dtypes("number")
    if not numeriques.empty:
        display(numeriques.describe().T.round(2))
    return empreinte
