======================================================================
INTRODUCTION - RESTful APIs, HTTP, Flask & API Architecture
======================================================================

INTRODUCTION
------------
Dans le monde en constante évolution du développement logiciel, la capacité
à communiquer et transférer efficacement des données entre systèmes est
devenue essentielle. Ce projet explore l’univers des API RESTful, un pilier
fondamental des services web modernes.

L’architecture REST (Representational State Transfer) repose sur un ensemble
de contraintes garantissant un système de communication scalable, stateless
et cacheable. Cette approche facilite l’intégration de services web et les
rend accessibles à une grande variété d’applications.

----------------------------------------------------------------------
LEARNING OBJECTIVES
-------------------

HTTP / HTTPS BASICS
    Comprendre les principes fondamentaux du protocole HTTP, les méthodes
    utilisées pour transférer des données, ainsi que la différence entre
    HTTP et HTTPS.

API CONSUMPTION WITH COMMAND LINE
    Manipuler des APIs via des outils simples en ligne de commande, afin
    d’acquérir les bases de l’interaction avec des services distants.

API CONSUMPTION WITH PYTHON
    Utiliser Python pour consommer des APIs, traiter les données reçues
    et automatiser des interactions plus avancées.

API DEVELOPMENT WITH http.server
    Découvrir comment créer une API simple en utilisant les modules
    intégrés de Python, afin de comprendre les fondations d’un serveur.

API DEVELOPMENT WITH FLASK
    Approfondir la création d’API avec Flask : routing, gestion des données,
    organisation du code, montée en charge.

API SECURITY & AUTHENTICATION
    Étudier les mécanismes de sécurité essentiels : authentification,
    protection des données, contrôle d’accès.

API STANDARDS & DOCUMENTATION WITH OPENAPI
    Comprendre l’importance de la documentation standardisée pour assurer
    la maintenabilité, la clarté et l’accessibilité d’une API.

----------------------------------------------------------------------
IMPORTANCE
----------
Dans notre ère numérique interconnectée, les API RESTful jouent un rôle
central dans l’intégration de systèmes hétérogènes. Elles servent
d’intermédiaires, traduisant des requêtes en actions compréhensibles,
récupérant des données ou déclenchant des opérations.

Des réseaux sociaux aux systèmes industriels automatisés, les APIs sont
partout. Maîtriser leur consommation, leur création, leur sécurisation et
leur documentation constitue une compétence essentielle. Cela implique
autant la compréhension technique que la vision d’ensemble permettant une
communication fluide et efficace entre services.

----------------------------------------------------------------------
REST API - CONCEPTUAL DIAGRAM
-----------------------------

+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database

COMPONENTS
----------
Client:
    L’émetteur de la requête, souvent un navigateur ou une application.

Web Server:
    Reçoit la requête, effectue le routage ou l’équilibrage de charge,
    puis la transmet au serveur d’API.

API Server:
    Le cœur logique du système. Il traite la requête, détermine l’action
    à effectuer et interagit avec la base de données si nécessaire.

Database:
    Stocke les données que l’API peut récupérer ou modifier.

FLOW
----
1. Le client envoie une requête HTTP/HTTPS au Web Server.
2. Le Web Server transmet la requête au API Server.
3. Le API Server traite la requête et interagit avec la base si besoin.
4. Le API Server renvoie la réponse au Web Server.
5. Le Web Server renvoie la réponse finale au client.

Ce schéma représente une architecture typique. Dans des environnements plus
simples, Web Server et API Server peuvent être fusionnés. La séparation
présentée ici illustre les couches possibles dans un système plus complexe.

======================================================================

USAGE
-----
This repository includes an example Python script that consumes a REST API
and writes the results to a CSV file.

Requirements:
- Python 3.8+
- requests library

Run the example script with:

    python3 "task_02_requests copy.py"

The script performs two actions:
- prints the title of each post fetched from the JSONPlaceholder API
- saves the posts to `posts.csv` with id, title, and body fields

If you want to use the script from another module, import the functions:

    from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

Then call the functions directly.

HTTP server example
-------------------

The repository also includes a simple HTTP server example in `task_03_http_server.py`.
Run it with:

    python3 task_03_http_server.py

Then access the endpoints on `http://localhost:8000`:

- `/`       : returns a plain text greeting
- `/data`   : returns sample JSON data
- `/status` : returns a plain text health status
- `/info`   : returns JSON metadata about the server

This script demonstrates how to build a basic API with Python's standard library.
