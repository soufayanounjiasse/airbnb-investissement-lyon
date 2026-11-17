"""Équipements étudiés en C1 : motifs de recherche et indicatrices.

Les libellés Inside Airbnb sont en anglais et détaillés ("Free parking on premises",
"Wifi – 300 Mbps"). On cherche donc par motif (regex) sur des libellés en minuscules,
jamais par libellé exact. Chaque motif est un couple (à inclure, à exclure).
"""
import ast
import json
import re

import pandas as pd

MOTIFS = {
    # parking rattaché au logement : on exclut le parking de rue et hors site
    "a_parking": (r"parking|garage", r"street|off premises"),
    "a_climatisation": (r"air conditioning|\bac\b", None),
    "a_lave_vaisselle": (r"dishwasher", None),
    "a_arrivee_autonome": (r"self check-in|keypad|lockbox|smart lock", None),
    "a_balcon_terrasse": (r"balcony|patio|terrace", None),
    "a_espace_travail": (r"dedicated workspace", None),
    "a_ascenseur": (r"elevator", None),
    # (?<!dish) évite de compter "dishwasher" comme un lave-linge
    "a_lave_linge": (r"(?<!dish)washer", None),
    "a_machine_cafe": (r"coffee maker|espresso|nespresso|keurig", None),
    "a_vue": (r"\bview\b", None),
    "a_foyer": (r"fireplace", None),
    # "pool table" n'est pas une piscine
    "a_piscine_spa": (r"\bpool\b|hot tub|\bspa\b|jacuzzi", r"pool table"),
}


def parse_amenities(valeur):
    """Retourne la liste des équipements en minuscules, quel que soit le format d'entrée.

    Accepte une vraie liste / un tableau (table nettoyée), ou une chaîne écrite comme une
    liste JSON ou Python (données brutes). Valeur manquante : liste vide.
    """
    if isinstance(valeur, str):
        try:
            liste = json.loads(valeur)
        except (ValueError, TypeError):
            try:
                liste = ast.literal_eval(valeur)
            except (ValueError, SyntaxError):
                liste = [e.strip(" \"'") for e in valeur.strip("[]").split(",") if e.strip()]
    elif hasattr(valeur, "__iter__"):
        liste = list(valeur)
    else:
        return []
    return [str(e).lower() for e in liste]


def ajouter_indicatrices(df, col="amenities", equipements=None):
    """Ajoute une colonne booléenne par équipement (voir MOTIFS)."""
    equipements = list(MOTIFS) if equipements is None else list(equipements)
    listes = df[col].map(parse_amenities)
    sortie = df.copy()
    for nom in equipements:
        inclure, exclure = MOTIFS[nom]
        ri = re.compile(inclure)
        re_ex = re.compile(exclure) if exclure else None
        sortie[nom] = listes.map(
            lambda items: any(ri.search(e) and not (re_ex and re_ex.search(e)) for e in items)
        )
    return sortie
