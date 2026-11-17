"""Vérifications sur données synthétiques : python tests/test_primes.py (depuis la racine)."""
import sys
sys.path.insert(0, ".")
import numpy as np
import pandas as pd
from src.equipements import MOTIFS, parse_amenities, ajouter_indicatrices
from src.primes import (ajouter_classe_capacite, perimetre_logements_entiers, prime_naive,
                        prime_comparable, prime_regression, tableau_primes)

# 1. Motifs : cas piégeux
cas = pd.DataFrame({"amenities": [
    '["Dishwasher", "Wifi"]',
    '["Washer", "Free parking on premises"]',
    '["Free street parking", "Pool table"]',
    '["Paid parking off premises", "Hot tub", "City skyline view"]',
    '["Window AC unit", "Keypad", "Dedicated workspace"]',
]})
r = ajouter_indicatrices(cas)
assert list(r["a_lave_vaisselle"]) == [True, False, False, False, False]
assert list(r["a_lave_linge"]) == [False, True, False, False, False]   # dishwasher exclu
assert list(r["a_parking"]) == [False, True, False, False, False]      # rue / hors site exclus
assert list(r["a_piscine_spa"]) == [False, False, False, True, False]  # pool table exclu
assert list(r["a_climatisation"]) == [False, False, False, False, True]
assert list(r["a_vue"]) == [False, False, False, True, False]
assert parse_amenities(np.array(["Wifi", "TV"])) == ["wifi", "tv"]
assert parse_amenities(np.nan) == []

# 2. Primes : effet vrai de +10 % sur le prix pour a_parking, corrélé à la capacité
rng = np.random.default_rng(42)
n = 6000
acc = rng.integers(1, 9, n)
p_equip = np.clip(0.1 + 0.08 * acc, 0, 0.9)   # les grands biens ont plus d'équipements
parking = rng.random(n) < p_equip
quartier = rng.choice(["Lyon 1er", "Lyon 2e", "Lyon 3e", "Lyon 6e"], n)
prix = 40 * acc ** 0.8 * np.where(parking, 1.10, 1.0) * np.exp(rng.normal(0, 0.15, n))
df = pd.DataFrame({
    "room_type": "Entire home/apt", "price": prix, "accommodates": acc,
    "bedrooms": np.maximum(1, acc // 2), "neighbourhood_cleansed": quartier,
    "a_parking": parking, "estimated_revenue_l365d": prix * 150,
})
df = ajouter_classe_capacite(perimetre_logements_entiers(df))
naive = prime_naive(df, "a_parking", "price")
comp = prime_comparable(df, "a_parking", "price")
reg = prime_regression(df, ["a_parking"])["a_parking"]
print(f"naïve {naive:.1%} | comparable {comp:.1%} | régression {reg:.1%} (vrai effet : +10 %)")
assert naive > comp > 0.05, "la prime naïve doit surestimer"
assert abs(reg - 0.10) < 0.03
assert tableau_primes(df, ["a_parking"]).shape == (1, 6)
print("OK")
