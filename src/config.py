from pathlib import Path
import os

# Ville attribuée : vérifier l'écriture exacte du dossier dans catalogue.csv
VILLE = "lyon"

# Chaque membre définit la variable d'environnement AIRBNB_DATA_ROOT
# vers son dossier Drive "data" (voir README). Défaut : ./data
DATA_ROOT = Path(os.environ.get("AIRBNB_DATA_ROOT", "data"))
DOSSIER = DATA_ROOT / VILLE

PROJET = Path(__file__).resolve().parent.parent
CLEAN = PROJET / "data_clean"
CLEAN.mkdir(exist_ok=True)

SEED = 42
