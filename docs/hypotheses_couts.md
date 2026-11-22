# Hypothèses de coûts, fiscalité et réglementation : sources (C4 et E2)

Consultées les 20 et 22/11/2026. À re-vérifier avant le rendu. Légende : **S** = source officielle, **P** = source privée ou presse (ordre de grandeur), **A** = hypothèse à sourcer.

| Paramètre | Valeur utilisée | Statut | Source |
|---|---|---|---|
| Commission Airbnb (hôte) | 15,5 % du sous-total, voyageur 0 %. TVA incluse là où elle s'applique | P (à compléter par la page d'aide Airbnb) | Depuis le 13/10/2026 en France et dans l'EEE : toutsurmesfinances.com, hospitality-on.com. Le 27/10/2025 ne concernait que les hôtes connectés à un PMS (hostaway.com, pricelabs). Sur la TVA : jedeclaremonmeuble.com/frais-service-airbnb (taux affiché TVA incluse) ; une source britannique ajoute 20 % de TVA (rentalscaleup.com) : sensibilité `tva_supplementaire` dans le notebook |
| Ancien modèle | 3 % hôte + 14,1 à 16,5 % voyageur | P | mêmes sources |
| Séjours estimés | avis sur 12 mois / 0,5 | S | insideairbnb.com/data-assumptions (taux d'avis de 50 %, durée de séjour 3 nuits, remplacée par la durée minimale si elle est plus élevée). Vérifié dans nos données : 89 % des annonces sous le plafond ont occupation = avis x 2 x 3 nuits, les autres utilisent minimum_nights |
| Ménage par séjour | 55 € (T2/T3 : 40 à 90 €) | P | houst.com/blog/menage-airbnb-tarifs ; guestready.com (35 à 70 € par check-out à Lyon) |
| Conciergerie (option) | ≈ 20 % des revenus + ménage payé par le voyageur | P | lodgify.com/fr/guides/conciergerie-airbnb/tarifs |
| Micro-BIC meublé de tourisme non classé | abattement 30 %, plafond 15 000 € | S | service-public.gouv.fr/particuliers/actualites/A18880 ; loi n° 2024-1039 du 19/11/2024 |
| Micro-BIC meublé de tourisme classé | abattement 50 %, plafond 77 700 € (revenus 2025), 83 600 € (revenus 2026 selon Service-Public) | S | idem |
| Taxe de séjour Lyon (non classé) | 5 % du prix de la nuitée HT par personne, +10 % additionnels, plafond 5,39 € ; payée par le voyageur | S | visiterlyon.com/qui-sommes-nous/la-taxe-de-sejour-a-lyon ; collectivites-locales.gouv.fr/taxe-de-sejour |
| Enregistrement à Lyon | numéro d'enregistrement obligatoire sur l'annonce (téléservice de la Ville) | S | lyon.fr/demarche/logement-habitat/declarer-un-meuble-de-tourisme |
| Résidence principale à Lyon | location jusqu'à 90 jours par an sans autre formalité | S | lyon.fr (même page) |
| Autre bien (investissement) à Lyon | changement d'usage préalable obligatoire ; hors hyper-centre et ≥ 35 m² : compensation dès le 1er m² ; personnes physiques : autorisation temporaire de 9 ans non reconductible ; personnes morales : compensation dès le 1er m² | S | lyon.fr (même page) |
| API Meublés (transmission des données d'activité aux communes) | ouverture nationale au 4e trimestre 2026 ; décrets n° 2026-196 et 2026-197 du 19/03/2026 | S | lyon.fr (même page) |
| Loyer longue durée, non meublé | 14,10 €/m² par mois (Lyon zone 1, centre), 13,00 €/m² pour Lyon-Villeurbanne ; hors charges | S | Observatoire local des loyers de l'agglomération lyonnaise (OLL, Urbalyon), chiffres clés 2023 : urbalyon.org/sites/default/storage_files/productions/2024-05/2023_OLL_ChiffresCles.pdf. Une édition 2024 existe (avril et octobre 2025) : à relire pour actualiser |
| Loyer longue durée meublé | ≈ 17 €/m² par mois (12 à 25 selon secteur) ; studio meublé ≈ 650 €/mois | P | lemonade.com/fr/habitation/conseils/loyer-moyen-lyon ; studapart.com |
| Surface du bien de 3 à 4 personnes | 45 m² | A | hypothèse (surface habitable moyenne OLL : 55 à 61 m² tous logements) |
| Encadrement des loyers Lyon-Villeurbanne | en vigueur depuis nov. 2021 ; échéance et suppression envisagée par la nouvelle présidente de la Métropole : à vérifier | P | lyoncapitale.fr ; à confirmer sur un texte officiel |
| Assurance | 375 €/an (MRH bailleur meublé ou saisonnier : 250 à 500 €/an ; PNO simple : 60 à 160 €/an, moyenne 128 €) | P | france-epargne.fr/academy/assurance-habitation/pno-vs-mrh-quelle-formule-pour-le-bailleur (d'après Selectra 2026) ; selectra.info/assurance/assurance-habitation/proprietaire-non-occupant/prix |
| Consommables, charges fixes | 3 €/nuit ; 1 800 €/an (énergie, internet, entretien) | A | à sourcer |
| Non modélisé | achat et crédit, taxe foncière, charges de copropriété, vacance, prélèvements sociaux, temps de gestion | – | – |

## Résultat de C4 (profil retenu : 3-4 personnes dans les 1er, 2e et 5e arrondissements, 458 annonces)

| Scénario | Revenu brut | Séjours | Commission | Ménage | Net avant impôt | Loyer OLL (non meublé) | Loyer meublé estimé |
|---|---|---|---|---|---|---|---|
| bas (25 %) | 5 946 € | 10 | 922 € | 550 € | 2 173 € | 7 614 € | 9 180 € |
| médian | 14 928 € | 32 | 2 314 € | 1 760 € | 8 373 € | 7 614 € | 9 180 € |
| haut (75 %) | 27 227 € | 64 | 4 220 € | 3 520 € | 16 700 € | 7 614 € | 9 180 € |

Sensibilité du net médian : 8 373 € (base) ; 7 910 € avec 18,6 % de commission ; 7 893 € avec un ménage à 70 € ; 7 473 € avec des charges fixes majorées de 50 % ; 8 620 € avec une assurance PNO simple.
Lecture : le net médian dépasse le loyer non meublé mais pas le loyer meublé estimé ; l'avantage de la courte durée est mince au regard de l'effort, de la réglementation et du risque. Le scénario bas (nouvel entrant sans historique) reste très inférieur au loyer.
