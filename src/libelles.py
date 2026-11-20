"""Libellés français des colonnes du projet (noms de code anglais -> affichage français).

Les tables gardent les noms anglais d'Inside Airbnb pour que le code reste cohérent entre les membres ;
on affiche les libellés français dans les graphiques, tableaux et l'application :
    from src.libelles import libelle
    fig.update_layout(xaxis_title=libelle("price"))
"""

# colonne : (libellé français, signification, unité ou valeurs)
LIBELLES = {
    # ---- listings_propre (29 colonnes) ----
    "id": ("identifiant_annonce", "Identifiant unique de l'annonce", "entier"),
    "host_id": ("identifiant_hote", "Identifiant de l'hôte (donnée personnelle indirecte, jamais affichée)", "entier"),
    "calculated_host_listings_count": ("nb_annonces_hote", "Nombre d'annonces de l'hôte à Lyon", "annonces"),
    "host_is_superhost": ("hote_superhote", "L'hôte a le statut Superhôte", "vrai / faux"),
    "neighbourhood_cleansed": ("arrondissement", "Arrondissement de l'annonce (noms de neighbourhoods.csv)", "texte"),
    "latitude": ("latitude", "Latitude approximative de l'annonce", "degrés"),
    "longitude": ("longitude", "Longitude approximative de l'annonce", "degrés"),
    "property_type": ("type_propriete", "Type détaillé de bien (ex. Entire rental unit = appartement entier)", "texte"),
    "room_type": ("type_logement", "Entire home/apt = logement entier ; Private room = chambre privée ; Shared room = chambre partagée ; Hotel room = chambre d'hôtel", "texte"),
    "accommodates": ("capacite_voyageurs", "Nombre maximal de voyageurs", "personnes"),
    "bedrooms": ("chambres", "Nombre de chambres", "chambres"),
    "beds": ("lits", "Nombre de lits", "lits"),
    "amenities": ("equipements", "Liste des équipements proposés (libellés anglais)", "liste"),
    "price": ("prix_nuit", "Prix affiché par nuit, hors frais de ménage et de service", "€ par nuit"),
    "minimum_nights": ("duree_min_sejour", "Durée minimale de séjour", "nuits"),
    "availability_365": ("jours_disponibles_365", "Jours disponibles à la réservation sur les 365 prochains jours", "jours"),
    "number_of_reviews": ("nb_avis_total", "Nombre total d'avis reçus", "avis"),
    "number_of_reviews_ltm": ("nb_avis_12_mois", "Nombre d'avis sur les 12 derniers mois (ltm = last twelve months)", "avis"),
    "first_review": ("date_premier_avis", "Date du premier avis", "date"),
    "last_review": ("date_dernier_avis", "Date du dernier avis", "date"),
    "review_scores_rating": ("note_globale", "Note moyenne globale des voyageurs", "sur 5"),
    "estimated_occupancy_l365d": ("occupation_estimee_365j", "Nuits occupées estimées sur 12 mois (l365d = last 365 days), plafonnées à 255", "nuits"),
    "estimated_revenue_l365d": ("revenu_estime_365j", "Revenu estimé sur 12 mois = occupation estimée x prix", "€ par an"),
    "license": ("licence", "Numéro d'enregistrement ou mention d'exemption ; « Non renseigné » si vide", "texte"),
    "nb_sdb": ("nb_salles_de_bain", "Nombre de salles de bain (0,5 = demi salle de bain)", "salles de bain"),
    "sdb_partagee": ("sdb_partagee", "La salle de bain est partagée", "vrai / faux"),
    "nb_equipements": ("nb_equipements", "Nombre d'équipements listés", "équipements"),
    "prix_manquant": ("prix_manquant", "Indicateur : le prix n'était pas publié (annonce souvent non réservable)", "vrai / faux"),
    "prix_extreme": ("prix_extreme", "Indicateur : prix au-dessus du seuil de valeur aberrante (conservé, signalé)", "vrai / faux"),
    # ---- reviews_propre (4 colonnes) ----
    "listing_id": ("identifiant_annonce", "Annonce à laquelle l'avis est rattaché", "entier"),
    "date": ("date_avis", "Date de l'avis", "date"),
    "comments": ("commentaire", "Texte de l'avis (multilingue, contient des prénoms : ne jamais l'afficher tel quel)", "texte"),
    # ---- colonnes créées en C ----
    "classe_capacite": ("classe_capacite", "Classe de capacité : 1-2, 3-4, 5-6 ou 7+ personnes", "texte"),
    "prix_par_personne": ("prix_par_personne", "Prix par nuit divisé par la capacité", "€ par personne et par nuit"),
    "decile_prix": ("decile_prix", "Décile du prix par personne dans tout le périmètre (1 = le moins cher, 10 = le plus cher)", "1 à 10"),
    "decile_dans_classe": ("decile_prix_dans_classe", "Décile du prix par personne à l'intérieur de la classe de capacité", "1 à 10"),
    "hote_multi": ("hote_multi_annonces", "L'hôte a plus d'une annonce (définition provisoire ; B1 fait foi)", "vrai / faux"),
    "au_plafond": ("au_plafond", "L'occupation estimée atteint le plafond de 255 nuits", "vrai / faux"),
    "a_parking": ("a_parking", "Parking rattaché au logement (hors rue et hors site)", "vrai / faux"),
    "a_climatisation": ("a_climatisation", "Climatisation", "vrai / faux"),
    "a_lave_vaisselle": ("a_lave_vaisselle", "Lave-vaisselle", "vrai / faux"),
    "a_arrivee_autonome": ("a_arrivee_autonome", "Arrivée autonome (boîte à clés, digicode, serrure connectée)", "vrai / faux"),
    "a_balcon_terrasse": ("a_balcon_terrasse", "Balcon, patio ou terrasse", "vrai / faux"),
    "a_espace_travail": ("a_espace_travail", "Espace de travail dédié", "vrai / faux"),
    "a_ascenseur": ("a_ascenseur", "Ascenseur", "vrai / faux"),
    "a_lave_linge": ("a_lave_linge", "Lave-linge", "vrai / faux"),
    "a_machine_cafe": ("a_machine_cafe", "Machine à café", "vrai / faux"),
    "a_vue": ("a_vue", "Vue (ville, cour, jardin…)", "vrai / faux"),
    "a_foyer": ("a_foyer", "Cheminée ou foyer", "vrai / faux"),
    "a_piscine_spa": ("a_piscine_spa", "Piscine, jacuzzi ou spa", "vrai / faux"),
}


def libelle(colonne):
    """Libellé français d'une colonne (le nom lui-même s'il est inconnu)."""
    return LIBELLES.get(colonne, (colonne,))[0]
