# Investir dans la location courte durée à Lyon

Projet en équipe noté : Data Management, Data Viz & Text Mining.
Données : Inside Airbnb (licence CC BY 4.0), snapshot à compléter.

## Équipe

| Membre | Rôle principal |
|---|---|
| À compléter | A, D, E3 |
| À compléter | B, E1 |
| À compléter | C, E2 |

## Installation

```bash
git clone <url-du-depot>
cd airbnb-investissement
python -m venv .venv
# Windows : .venv\Scripts\activate   |   Mac/Linux : source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name airbnb --display-name "Python (airbnb)"
nbstripout --install
```

## Accès aux données

Les données sont sur le Drive partagé de l'énoncé (lecture seule). Ajouter le raccourci du
dossier `data` dans « Mon Drive », puis définir `AIRBNB_DATA_ROOT` :

- Windows (PowerShell) : `setx AIRBNB_DATA_ROOT "G:\Mon Drive\data"`
- Mac/Linux : `export AIRBNB_DATA_ROOT="/chemin/vers/data"`

Redémarrer VS Code après avoir défini la variable. Ne jamais écrire dans le dossier partagé.
Aucune donnée n'est versionnée (voir `.gitignore`).

## Organisation

- `notebooks/` : A, B, C, D (un responsable par notebook à la fois)
- `src/` : `config.py`, `signature.py`
- `app/app.py` : application Streamlit (`streamlit run app/app.py`)
- `docs/` : note de décision, présentation, rapport

## Règles d'équipe

- Branche `main` protégée : on passe par des Pull Requests relues par un autre membre.
- Nommage des branches : `A-prenom`, `B-prenom`, etc.
- Avant chaque commit : Restart Kernel and Run All.
- Aucun nom d'hôte ou de voyageur dans les livrables.
- Usage d'assistants IA : à déclarer dans le rapport (outil, usage, part reprise).

