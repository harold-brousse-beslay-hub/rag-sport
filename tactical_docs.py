"""
Seed data : analyses tactiques football pour bootstrapper le RAG.
En production, remplacer par des vrais docs (PDF, scraping, API).
"""

DOCUMENTS = [
    {
        "id": "doc_001",
        "source": "analyse_tactique",
        "team": "Manchester City",
        "season": "2024-25",
        "text": """
Manchester City sous Pep Guardiola utilise un 4-3-3 en phase offensive qui se transforme en 3-2-5 lors de la possession haute.
Le principe central est la surcharge du milieu de terrain pour créer des supériorités numériques dans l'entre-jeu.
Les latéraux, notamment Trent Alexander-Arnold et Joao Cancelo par le passé, remontent très haut pour former une ligne de 5 en attaque.
Le faux 9 ou l'attaquant de pointe crée des espaces en s'éloignant du but, permettant aux milieux de box-to-box d'arriver en retard.
Le pressing de Manchester City est structuré en blocs : déclenchement sur la passe du gardien adverse ou sur un latéral central dans son couloir.
Le pressing trap consiste à laisser intentionnellement un espace pour forcer la relance dans une zone puis refermer le piège à 3 joueurs.
En transition défensive, City adopte un contre-pressing immédiat dans les 5 secondes suivant la perte de balle.
Le taux de récupération haute balle (PPDA) de City est systématiquement dans le top 3 des ligues européennes.
La construction depuis l'arrière utilise le gardien comme joueur supplémentaire, créant toujours une supériorité numérique en première phase.
"""
    },
    {
        "id": "doc_002",
        "source": "analyse_tactique",
        "team": "Arsenal",
        "season": "2024-25",
        "text": """
Arsenal d'Arteta utilise principalement un 4-3-3 qui évolue en 2-3-5 en phase de possession.
La particularité d'Arsenal est l'intégration de ses latéraux Ben White et Jurrien Timber dans la construction centrale.
Ben White se retrouve régulièrement au milieu du terrain, libérant l'aile droite pour Saka qui opère comme un ailier pur.
Le milieu de terrain à 3 avec Rice en sentinelle est l'un des plus efficaces de Premier League pour la récupération : 7,2 ballons récupérés par match.
Arsenal presse très haut avec un PPDA de 6,8, signifiant qu'ils autorisent moins de 7 passes adverses avant de presser.
Le jeu de transitions rapides d'Arsenal est construit sur des combinaisons courtes en déviation, typiques du jeu de position de Guardiola.
Bukayo Saka est le joueur clé du système : 0,31 xA par 90 minutes, meilleur ratio de Premier League parmi les ailiers.
La phase défensive est organisée en 4-4-2 moyen-bloc, piégeant les équipes adverses dans leur couloir.
Arsenal a la meilleure séquence de possession progressive en Premier League : 18,3 passes progressives par possession en moyenne.
"""
    },
    {
        "id": "doc_003",
        "source": "analyse_tactique",
        "team": "Real Madrid",
        "season": "2024-25",
        "text": """
Le Real Madrid de Carlo Ancelotti utilise un 4-3-1-2 adaptable qui dépend fortement des profils individuels.
Contrairement aux équipes de Guardiola ou Arteta, Madrid ne s'appuie pas sur un système rigide mais sur des principes de jeu collectif avec une grande liberté individuelle.
Bellingham dans le rôle de meneur de jeu entre les lignes est la grande innovation tactique : il joue ni milieu, ni attaquant, exploitant les espaces entre défense et milieu adverses.
Le pressing de Madrid est sélectif et situationnel : l'équipe préfère se replier en bloc médian organisé (4-5-1) avant de contre-attaquer.
Les transitions offensives de Madrid sont parmi les plus dangereuses d'Europe avec 2,1 contre-attaques menant à un tir par match.
Vinicius Jr est le principal vecteur de déséquilibre : 7,3 dribbles tentés par 90 minutes, 58% de réussite.
La défense de Madrid sous Ancelotti concède délibérément la possession (47% possession moyenne) pour mieux exploiter les espaces en transition.
Le ratio xG contre/pour de Madrid est de 0,73, reflétant une équipe efficace offensivement et solide défensivement malgré un bloc bas fréquent.
"""
    },
    {
        "id": "doc_004",
        "source": "analyse_tactique",
        "team": "Bayern Munich",
        "season": "2024-25",
        "text": """
Le Bayern Munich de Vincent Kompany applique un 4-2-3-1 ambitieux avec un pressing très haut hérité de sa philosophie à Burnley, adaptée à un effectif de top niveau.
La ligne défensive du Bayern est positionnée extrêmement haute, souvent à la hauteur de la ligne médiane en phase offensive.
Cette défense haute crée des espaces derrière que Kompany compense par un pressing ultra-agressif dès la perte de balle.
Harry Kane comme faux 9 est crucial dans le système : il s'implique dans la construction avec 5,1 passes progressives reçues par 90 minutes.
Müller dans son rôle de Raumdeuter (exploiteur d'espaces) crée des décadrages dans l'arrière-garde adverse sans dribbler.
Le Bayern utilise la possession pour épuiser l'adversaire (63,2% possession moyenne) avant d'accélérer le tempo en fin de match.
La particularité du Bayern sous Kompany est son intensité constante : 98 sprints par match en moyenne, meilleur total de Bundesliga.
Les corners et coups de pied arrêtés sont devenus une arme avec 0,23 xG par corner, grâce à des mouvements coordonnés précis.
"""
    },
    {
        "id": "doc_005",
        "source": "analyse_tactique",
        "team": "Inter Milan",
        "season": "2024-25",
        "text": """
L'Inter Milan de Simone Inzaghi utilise un 3-5-2 très rigoureux, l'un des plus sophistiqués du football européen.
Le système à 3 centraux permet une supériorité numérique permanente contre les attaquants adverses, libérant les pistons pour monter.
Les pistons (piston droit et gauche) sont le vrai moteur de l'Inter : Dumfries et Dimarco cumulent 0,34 xA par 90 minutes combinés.
La particularité tactique d'Inzaghi est la capacité à passer instantanément de 3-5-2 à 5-3-2 en phase défensive sans réorganisation visible.
Le double pivot Barella-Calhanoglu est l'un des milieux les plus complets d'Europe : 91,2% de passes réussies avec un pressing intensity record.
L'Inter utilise peu le jeu long (12% de passes longues) préférant les combinaisons courtes dans les couloirs pour remonter le terrain.
La compacité défensive de l'Inter est extraordinaire : 8,1 mètres d'espacement moyen entre lignes en phase défensive.
Lautaro Martinez et Thuram forment le duo d'attaque le plus complémentaire de Serie A : l'un fixe, l'autre crée des décadrages.
"""
    },
    {
        "id": "doc_006",
        "source": "analyse_performance",
        "topic": "pressing_moderne",
        "text": """
Le pressing moderne dans le football européen de haut niveau a évolué significativement depuis les premières théories de Rinus Michels et Arrigo Sacchi.
Le PPDA (Passes Per Defensive Action) est devenu la métrique de référence pour quantifier l'intensité du pressing : plus le chiffre est bas, plus le pressing est agressif.
Les équipes les plus pressantes d'Europe en 2024-25 : Manchester City (5,9 PPDA), Arsenal (6,8), Bayer Leverkusen (7,1).
Le pressing trap est une technique avancée où l'équipe oriente intentionnellement l'adversaire vers une zone pour déclencher un pressing coordonné.
Le contre-pressing (Gegenpressing popularisé par Klopp) est la récupération immédiate dans les 5 secondes suivant la perte de balle.
Les données montrent que 78% des buts après récupération haute ont lieu dans les 10 secondes suivant la perte, justifiant le contre-pressing.
Le pressing à risque calculé (Arteta, Guardiola) accepte de concéder des espaces dans le dos en échange d'une supériorité numérique dans la zone de pressing.
Les entraîneurs scandinaves (Bjelland, Hojlund) ont introduit des variantes de pressing asymétriques adaptées à leurs systèmes à 3 centraux.
"""
    },
    {
        "id": "doc_007",
        "source": "analyse_performance",
        "topic": "stats_offensives_2024",
        "text": """
Les statistiques offensives de la saison 2024-25 révèlent des tendances importantes dans le football européen de haut niveau.
L'xG (Expected Goals) est devenu la métrique centrale d'évaluation offensive : Manchester City génère 2,31 xG par match, meilleur d'Europe.
Le taux de conversion (buts/xG) distingue les équipes à finisseurs d'élite : Kane au Bayern surperformes son xG de +0,18 par match.
Les passes progressives (forward passes qui avancent le jeu de 10m minimum vers la surface adverse) reflètent mieux l'efficacité offensive que la possession brute.
Real Madrid malgré une possession moyenne (47%) a un ratio passes progressives/possession parmi les plus élevés d'Europe.
Les tirs cadrés depuis la surface de réparation (Inside Box Shots on Target) sont le prédicteur le plus fiable de buts sur une saison.
Le progressive carry (porter le ballon 5m+ vers la surface adverse) est dominé par Vinicius Jr (6,2 par match) et Dribbleurs ailiers.
Les données 2024-25 confirment que les équipes avec le meilleur xG/90 en première moitié de championnat finissent dans les 3 premiers dans 87% des cas.
"""
    },
    {
        "id": "doc_008",
        "source": "analyse_performance",
        "topic": "systemes_defensifs",
        "text": """
Les systèmes défensifs du football moderne oscillent entre deux philosophies : le bloc bas compact et le pressing haut agressif.
Le bloc bas (popularisé par Diego Simeone à l'Atletico Madrid) repose sur une organisation défensive en deux blocs de 4 très serrés.
L'Atletico Madrid avec son 4-4-2 défensif concède en moyenne 0,87 xG contre par match, l'une des meilleures performances défensives.
La zone de contrôle (le rectangle entre les deux lignes de 4) est sanctuarisée : aucune pénétration directe n'est autorisée.
Le pressing situationnel combine bloc bas en possession adverse stable et pressing intense sur les erreurs ou passes courtes du gardien.
Les équipes à 3 centraux (Inter, Atletico en phase transition) offrent une meilleure protection des couloirs sans sacrifier la largeur offensive.
La défense haute (Bayern sous Kompany, City sous Guardiola) est compensée par un pressing ultra-agressif mais expose aux contre-attaques rapides.
Les données montrent que les équipes concédant le moins d'Expected Goals Against (xGA) sont systématiquement dans le top 4 de leur championnat.
Le rôle du gardien moderne dans la défense haute est crucial : il agit comme libéro et intervient 15m+ hors de sa surface en moyenne 3,2 fois par match (Ederson, Ter Stegen).
"""
    },
]


def get_all_documents():
    return DOCUMENTS


def get_documents_by_team(team_name: str):
    return [d for d in DOCUMENTS if d.get("team", "").lower() == team_name.lower()]
