from pathlib import Path
import os

# Ville attribuée (dossier du même nom dans catalogue.csv)
VILLE = "lyon"
SNAPSHOT = "2026-09-17"   # date du snapshot Inside Airbnb (voir source.txt)

PROJET = Path(__file__).resolve().parent.parent

# Données : variable d'environnement AIRBNB_DATA_ROOT si elle existe (ex. Drive pour ordinateur),
# sinon le dossier data/ à la racine du dépôt (ignoré par Git).
DATA_ROOT = Path(os.environ["AIRBNB_DATA_ROOT"]) if "AIRBNB_DATA_ROOT" in os.environ else PROJET / "data"
DOSSIER = DATA_ROOT / VILLE      # attendu : data/lyon/listings.csv.gz, reviews.csv.gz, ...

CLEAN = PROJET / "data_clean"
CLEAN.mkdir(exist_ok=True)

SEED = 42
