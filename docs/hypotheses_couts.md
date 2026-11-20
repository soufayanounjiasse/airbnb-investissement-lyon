# Hypothèses de coûts, fiscalité et réglementation : sources (C4 et E2)

Consultées le 20/11/2026. À re-vérifier avant le rendu. Légende : **S** = source officielle, **P** = source privée ou presse (ordre de grandeur), **A** = hypothèse à sourcer.

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
| Loyer longue durée meublé | ≈ 17 €/m²/mois (12 à 25 selon secteur) ; studio meublé ≈ 650 €/mois | P | lemonade.com/fr/habitation/conseils/loyer-moyen-lyon ; studapart.com. Source officielle à citer : OLL |
| Encadrement des loyers Lyon-Villeurbanne | en vigueur depuis nov. 2021 ; échéance et suppression envisagée par la nouvelle présidente de la Métropole : à vérifier | P | lyoncapitale.fr ; à confirmer sur un texte officiel |
| Consommables, charges fixes, assurance | 3 €/nuit ; 1 800 €/an ; 250 €/an | A | à sourcer |

## Résultat provisoire de C4 (profil 3-4 personnes, périmètre de C)

| Scénario | Revenu brut | Séjours | Commission | Ménage | Net avant impôt | Loyer longue durée brut |
|---|---|---|---|---|---|---|
| bas (25 %) | 4 527 € | 8 | 702 € | 440 € | 1 227 € | 8 160 € |
| médian | 11 808 € | 26 | 1 830 € | 1 430 € | 6 228 € | 8 160 € |
| haut (75 %) | 23 333 € | 58 | 3 617 € | 3 190 € | 13 918 € | 8 160 € |
