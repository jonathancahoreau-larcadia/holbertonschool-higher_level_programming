======================================================================
PYTHON - SERVER-SIDE RENDERING (SSR)
======================================================================

DESCRIPTION
-----------
Ce projet introduit le Server-Side Rendering (SSR) en Python, une technique
où les pages web sont générées côté serveur avant d’être envoyées au client
sous forme de HTML complet.

Contrairement au client-side rendering (CSR), où le navigateur construit la
page via JavaScript, le SSR permet :
    - un rendu plus rapide,
    - une meilleure indexation SEO,
    - une structure plus stable,
    - une gestion simplifiée des données.

Vous utiliserez Flask et le moteur de templates Jinja pour créer des pages
dynamiques basées sur des données provenant de JSON, CSV ou SQLite.

----------------------------------------------------------------------
RESOURCES
---------
MDN Server-Side Web Development
Client-side vs. Server-side vs. Pre-rendering for Web Apps
Flask Official Documentation
Python JSON Documentation
Python CSV Documentation
Python SQLite Documentation
Jinja2 Documentation

----------------------------------------------------------------------
LEARNING OBJECTIVES
-------------------
À la fin de ce projet, vous devez être capable d’expliquer clairement :

Understand the concepts of server-side rendering and how it differs from client-side rendering
    SSR : HTML généré côté serveur
    CSR : HTML généré via JavaScript dans le navigateur

Learn the benefits of using server-side rendering in web development
    - SEO amélioré
    - Temps de chargement initial plus rapide
    - Moins de dépendance au JavaScript
    - Structure plus robuste

Implement SSR in Python using the Flask framework
    Créer des routes, renvoyer des templates, gérer les requêtes HTTP.

Utilize Jinja templating engine to dynamically generate HTML pages
    Utiliser {{ variables }} et {% blocks %} pour générer du contenu dynamique.

Read and display data from various sources including JSON, CSV, and SQLite databases
    Charger des données, les transformer, les injecter dans les templates.

Handle dynamic content and user inputs in web applications
    Gérer les formulaires, les paramètres de requête, les interactions utilisateur.

----------------------------------------------------------------------
WHAT TO EXPECT
--------------
Dans ce projet, vous allez :

    - créer une application Flask,
    - construire des templates Jinja,
    - intégrer des données dynamiques,
    - lire des fichiers JSON et CSV,
    - interagir avec une base SQLite,
    - afficher des pages HTML générées côté serveur,
    - manipuler des routes et des contextes de rendu.

À la fin, vous aurez une compréhension complète du SSR et serez capable de
créer des applications web efficaces, scalables et faciles à maintenir.

----------------------------------------------------------------------
OBJECTIF GLOBAL
---------------
Ce projet vous apprend à :
    - comprendre les différences SSR / CSR,
    - structurer une application Flask,
    - utiliser Jinja pour générer du HTML dynamique,
    - intégrer plusieurs sources de données,
    - gérer des interactions utilisateur côté serveur,
    - produire des pages web optimisées pour le SEO.

======================================================================
