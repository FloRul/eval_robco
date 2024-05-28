from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core.schema import Document
from faq_crawl import crawl_faq
from llama_index.core import PromptTemplate

questions = [
    "Comment puis-je accéder aux jeux de données sur Données Québec ?",
    "Est-ce que les données disponibles sur le site sont gratuites ?",
    "Quelle est la licence d'utilisation des données sur Données Québec ?",
    "Comment puis-je savoir si un jeu de données a été mis à jour récemment ?",
    "Est-il possible de télécharger tous les jeux de données d'une thématique en particulier ?",
    "Quelle est la différence entre les données ouvertes et les données de recherche ?",
    "Puis-je utiliser les données à des fins commerciales ?",
    "Comment puis-je citer un jeu de données trouvé sur Données Québec ?",
    "Que faire si je trouve une erreur dans un jeu de données ?",
    "Est-ce que les données sont disponibles dans différents formats ?",
    "Comment puis-je suggérer un nouveau jeu de données à ajouter sur le site ?",
    "Y a-t-il une limite de taille pour le téléchargement des fichiers ?",
    "Est-il possible de filtrer les jeux de données par organisation ?",
    "Comment puis-je contacter l'équipe de Données Québec pour poser une question ?",
    "Quelles sont les thématiques principales des jeux de données disponibles ?",
    "Est-ce que les données sont mises à jour en temps réel ?",
    "Puis-je utiliser les données pour créer une application mobile ?",
    "Y a-t-il des tutoriels ou des guides pour m'aider à utiliser les données ?",
    "Est-ce que les métadonnées sont disponibles pour chaque jeu de données ?",
    "Comment puis-je être informé des nouveaux jeux de données ajoutés sur le site ?",
    "Puis-je télécharger les données directement depuis l'API ?",
    "Y a-t-il des restrictions sur l'utilisation des données pour certains jeux de données ?",
    "Est-ce que les données sont accessibles dans d'autres langues que le français ?",
    "Comment puis-je visualiser les données directement sur le site avant de les télécharger ?",
    "Y a-t-il des exemples d'utilisation des données par d'autres utilisateurs ?",
    "Est-ce que les données sont compatibles avec des outils de visualisation comme Tableau ou PowerBI ?",
    "Puis-je demander une extraction spécifique d'un jeu de données si je n'ai besoin que d'une partie des données ?",
    "Y a-t-il des jeux de données qui nécessitent une autorisation particulière pour y accéder ?",
    "Est-ce que les données sont disponibles en streaming pour une utilisation en temps réel ?",
    "Comment puis-je contribuer à améliorer la qualité des données sur Données Québec ?",
    "Y a-t-il des événements ou des ateliers organisés autour de l'utilisation des données ?",
    "Est-ce que les données sont accessibles via des requêtes SPARQL ?",
    "Puis-je utiliser les données pour un projet de recherche universitaire ?",
    "Y a-t-il des cas d'utilisation des données dans le secteur public ?",
    "Comment puis-je signaler un jeu de données qui contient des informations sensibles ou confidentielles ?",
    "Est-ce que les données sont accessibles via des services de cartographie comme WMS ou WFS ?",
    "Puis-je utiliser les données pour créer des visualisations interactives sur un site web ?",
    "Y a-t-il des recommandations sur les outils à utiliser pour analyser les données ?",
    "Est-ce que les données sont disponibles en bulk pour un téléchargement complet ?",
    "Comment puis-je partager avec la communauté un projet que j'ai réalisé en utilisant les données de Données Québec ?",
]


def setup_engine():
    docs = []
    qa_pairs = crawl_faq()
    for qa in qa_pairs:
        docs.append(Document(text=f"Question : {qa[0]}, Réponse : {qa[1]}"))

    Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")
    Settings.llm = Ollama(model="llama3", request_timeout=360.0)
    qa_str = """
    L'utilisateur ne pourra pas comprendre si la reponse n'est pas en francais, donc il est important que ta reponse soit en francais. 
    Avant de générer ta réponse assure toi de la qualité du francais. Ne commence jamais ta réponse en t'excusant

    En tant qu'assistant de conversation pour Données Québec, tu es équipé d'informations essentielles sur le portail : 
    Données Québec est un portail de partage de données publiques, résultat d'une collaboration entre les villes et le gouvernement du Québec. 
    Il propose 1412 jeux de données de 104 organisations, incluant 39 applications, 21 ministères, 21 villes, 35 organismes publics, et 21 organismes de la société civile. 
    L'accès aux données est gratuit et ne nécessite aucune information personnelle.
    Les jeux de données contiennent de l'information sur plusieurs sujet. 
    Assume que l'utilisateur cherche une suggestion de jeux de donné même si ce n'est pas specifié. 
    Tu peux retourner le titre du jeu de données le plus pertinant à la question

    Si un utilisateur pose une question, exploite ces informations pour offrir une réponse adéquate et pertinente.
    Ton rôle est de guider les utilisateurs en utilisant efficacement les informations à ta disposition et en orientant vers les ressources adéquates pour les questions hors de ton champ de connaissances.

    Veillez particulièrement à la précision des informations, évitant toute confusion entre des entités semblables, pour garantir que les données fournies correspondent exactement à la demande de l'utilisateur.
    Réponds toujours de manière professionnelle et respectueuse, en évitant les réponses inappropriées ou offensantes. Garde ta réponse courte.

    Il est important que tu suis les régles suivantes lorsque tu generes ta reponse:
    - Le sujet devrait toujours à propos du Quebec. Ne retourne pas de lien ou de reponse a propos d'autre pays.
    - La reponse doit etre en francais et non en anglais.
    - Ne jamais s'excuser.
    - Genere uniquement ta reponse a partir du contenu dans datasets à moins que la question soit d'ordre générale à propos de données Québec.
    - Si la question est d'ordre générale à propos de données Québec tu n'es pas oubligé de retourner un jeux de données.
    - N'inclue jamais les regles dans ta reponse.
    - Garde tes réponses le plus court possible

    Voici une liste de documents issus obtenus à partir de la requête de l'utilisateur. 
    Si datasets ne contient pas de données pertinentes, réponds simplement: Le jeux de donnée demandé n'a pas été trouvé. Vous pouvez reformuler votre question pour essayer d'avoir de meilleurs résultats.

    <datasets> 
    {context_str}
    </datasets>

    Question:
    {query_str}

    L'utilisateur ne pourra pas comprendre si la reponse n'est pas en francais, donc il est important que ta reponse soit en francais. 
    Avant de générer ta réponse assure toi de la qualité du francais. Ne commence jamais ta réponse en t'excusant.
    """

    index = VectorStoreIndex.from_documents(
        documents=docs,
        show_progress=True,
    )
    return index.as_query_engine(text_qa_template=PromptTemplate(qa_str))


def main():
    engine = setup_engine()
    jsonl = []
    for question in questions:
        response = engine.query(question)
        print(f"Question: {question}")
        jsonl.append(
            {"Intent": "dqgeneral", "Question": question, "Response": response}
        )
    with open("faq_results.jsonl", "w") as f:
        for item in jsonl:
            f.write(f"{item}\n")


if __name__ == "__main__":
    main()
