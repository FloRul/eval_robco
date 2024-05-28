NICO_TEMPLATE = """Données Québec est un portail de partage de données publiques, résultat d'une collaboration entre les villes et le gouvernement du Québec.
Il propose 1412 jeux de données de 104 organisations, incluant 39 applications, 21 ministères, 21 villes, 35 organismes publics, et 21 organismes de la société civile.
L'accès aux données est gratuit et ne nécessite aucune information personnelle.
Les jeux de données contiennent de l'information sur plusieurs sujet.

<question>
{question}
</question>

Voici une liste d'intentions possibles pour la classification de l'intention de l'utilisateur :
"dqgeneral": Information, jeu, jeux de donnée, dataset ou metadonnée dans le but de trouver un jeu de données provenant de données Quebec. L'information sur donnees Quebec inclut le titre (nom, appellation), le nom (dénomination, désignation), la description (résumé, présentation), l'auteur (créateur, rédacteur), l'email (adresse électronique, courriel, coordonnées) de l'auteur, l'ID (identifiant unique) de l'utilisateur créateur, l'extension (zone, aire) spatiale, l'organisation (structure, établissement) principale, l'ID (identifiant unique), le niveau (degré, rang) d'accès, la localisation (emplacement, situation) des données, la classification (catégorisation, typologie) de sécurité, la langue (idiome, dialecte), l'ID (identifiant unique) de la licence, le titre (nom, appellation) de la licence, l'URL (adresse web, lien) de la licence, le mainteneur (responsable, gestionnaire), l'email (adresse électronique, courriel) du mainteneur, la date (jour, moment) de création des métadonnées, la date (jour, moment) de modification des métadonnées, la méthodologie (procédure, démarche), le nombre (quantité, total) de ressources, le nombre (quantité, total) de tags (étiquettes, mots-clés), l'état (statut, condition), le type (genre, catégorie), la fréquence (périodicité, rythme) de mise à jour, les groupes (ensembles, collections), les tags (étiquettes, mots-clés) et les formats (types, extensions) de fichiers des ressources. La question peut avoir besoin seulement d'un de ces champs. Inclue une demande de courriel (email) du créateur d'un jeu de donnée.
"pii": Incluent des valeurs pour des informations personnelles sensibles (PII, PRP) sont directement fournies comme les numéros de sécurité sociale, numéros d'assurance, comptes bancaires, codes PIN, numéros de cartes de crédit/débit, noms d'utilisateur, mots de passe, numéros de téléphone et autre valeur typiquement considérées comme des PII sensibles. 
"irrelevant": N'est pas une recherche d'information, jeu, jeux de donnée ou dataset.
"greeting": Toute forme de salutation ou de prise de congé de l'utilisateur (Salut, Bonjour, Bonsoir, Comment ça va ?, Merci, Au revoir, Bye).
"contact": Demande comment contacter un humain ou de parler a quelqu'un de maniere explicite chez Données Quebec (je veux parler a un human, transfert moi a quelqu'un, je veux la page contact).
"redirection": Demande d'information pour un individue qui pourrait referer a un service du gouvernment incluant les permis de conduire (SAAQ, obtenir et renouveller un permis de conduire),les immatriculation (SAAQ, immatriculer un vehicule), la recherche d'emploie (trouver un emploi en sante, chercher un emploi en education, travailler pour le gouvernement du quebec), trouver un medecin de famille (prendre rendez-vous, examen medical), l'immigration au Canada (comment venir au Canada, etape pour immigrer au Canada, immigrer au Quebec)
Considérant la question, Classifie le text suivant en une des intentions issue de la liste précédente.
Donne ta réponse finale en l'insérant entre les caractères ## et ##. Example : ##dqgeneral##.
Tu ne dois choisir qu'une seule intention.
"""

TEMPLATE = """Données Québec est un portail de partage de données publiques, résultat d'une collaboration entre les villes et le gouvernement du Québec.
Il propose 1412 jeux de données de 104 organisations, incluant 39 applications, 21 ministères, 21 villes, 35 organismes publics, et 21 organismes de la société civile.
L'accès aux données est gratuit et ne nécessite aucune information personnelle.
Les jeux de données contiennent de l'information sur plusieurs sujet.
Dans un premier temps essaye de classifier l'intention de l'utilisateur.
<intention></intention>
Dans un second temps voici une liste d'intentions possibles pour la classification de l'intention de l'utilisateur :
"dqgeneral": Information, jeu, jeux de donnée, dataset ou metadonnée dans le but de trouver un jeu de données provenant de données Quebec. L'information sur donnees Quebec inclut le titre (nom, appellation), le nom (dénomination, désignation), la description (résumé, présentation), l'auteur (créateur, rédacteur), l'email (adresse électronique, courriel, coordonnées) de l'auteur, l'ID (identifiant unique) de l'utilisateur créateur, l'extension (zone, aire) spatiale, l'organisation (structure, établissement) principale, l'ID (identifiant unique), le niveau (degré, rang) d'accès, la localisation (emplacement, situation) des données, la classification (catégorisation, typologie) de sécurité, la langue (idiome, dialecte), l'ID (identifiant unique) de la licence, le titre (nom, appellation) de la licence, l'URL (adresse web, lien) de la licence, le mainteneur (responsable, gestionnaire), l'email (adresse électronique, courriel) du mainteneur, la date (jour, moment) de création des métadonnées, la date (jour, moment) de modification des métadonnées, la méthodologie (procédure, démarche), le nombre (quantité, total) de ressources, le nombre (quantité, total) de tags (étiquettes, mots-clés), l'état (statut, condition), le type (genre, catégorie), la fréquence (périodicité, rythme) de mise à jour, les groupes (ensembles, collections), les tags (étiquettes, mots-clés) et les formats (types, extensions) de fichiers des ressources. La question peut avoir besoin seulement d'un de ces champs.
"pii": Informations personnelles sensibles et privées à propos de la personne qui pose la question, comme le numéro d'assurance sociale, les détails bancaires, les identifiants de connexion, les mots de passe, les numéros de carte de crédit ou toute autre donnée confidentielle permettant l'usurpation d'identité ou les transactions financières non autorisées. Exclut les informations de contact générales comme le nom, prénom, numéro de téléphone ou adresse qui pourraient être publiques ou professionnelles.
"irrelevant": N'est pas une recherche d'information, jeu, jeux de donnée ou dataset.
"greeting": L'utilisateur salue le bot (Salue, Bonjour, comment ça va).
"contact": L'utilisateur demande comment contacter un humain.
"redirection": L'utilisateur demande à être redirigé vers un autre service ou une autre ressource ou sa requête concerne d'autres services gouvernementaux.
Considérant ta précédente réponse. Classifie le text suivant en une des intentions issue de la liste précédente.
Texte: "{question}"
Donne ta réponse finale en l'insérant entre les caractères ## et ##. Example : ##dqgeneral##.
Tu ne dois choisir qu'une seule intention. Si tu ne trouves pas d'intention appropriée, tu peux choisir "irrelevant".
"""

OPUS_TEMPLATE = """
Données Québec est un portail de partage de données publiques, résultat d'une collaboration entre les villes et le gouvernement du Québec. Il propose 1412 jeux de données de 104 organisations, incluant 39 applications, 21 ministères, 21 villes, 35 organismes publics, et 21 organismes de la société civile. L'accès aux données est gratuit et ne nécessite aucune information personnelle. Les jeux de données contiennent de l'information sur plusieurs sujets.
Voici une liste d'intentions possibles pour la classification de l'intention de l'utilisateur :

"dqgeneral": L'utilisateur recherche des informations, des jeux de données ou des métadonnées spécifiques à Données Québec, tels que le titre, le nom, la description, l'auteur, l'email de l'auteur, l'ID de l'utilisateur créateur, l'extension spatiale, l'organisation principale, l'ID, le niveau d'accès, la localisation des données, la classification de sécurité, la langue, l'ID de la licence, le titre de la licence, l'URL de la licence, le mainteneur, l'email du mainteneur, la date de création/modification des métadonnées, la méthodologie, le nombre de ressources/tags, l'état, le type, la fréquence de mise à jour, les groupes, les tags et les formats de fichiers des ressources. 
"pii": L'utilisateur mentionne des informations personnelles sensibles et privées le concernant, comme le numéro d'assurance sociale, les détails bancaires, les identifiants de connexion, les mots de passe, les numéros de carte de crédit ou toute autre donnée confidentielle permettant l'usurpation d'identité ou les transactions financières non autorisées. Cela exclut les informations de contact générales comme le nom, prénom, numéro de téléphone ou adresse qui pourraient être publiques ou professionnelles.
"redirection": L'utilisateur demande à être redirigé vers un autre service, une autre ressource, ou sa requête concerne des services gouvernementaux autres que Données Québec.
"greeting": L'utilisateur salue simplement le bot, sans demande spécifique (ex: Bonjour, comment ça va).
"contact": L'utilisateur demande explicitement comment contacter un humain ou obtenir de l'assistance personnalisée.
"irrelevant": La requête de l'utilisateur n'est pas liée à une recherche d'information, de jeux de données ou de datasets sur Données Québec.

En te basant uniquement sur le texte fourni et en considérant les intentions ci-dessus, classe la requête de l'utilisateur en une seule intention parmi celles proposées. Si aucune intention ne correspond, choisis "irrelevant".
Texte: "{question}"

Met ta réponse entre les balises <intention> et </intention> Exemple : <intention>dqgeneral</intention>
"""
