======================================================================
JAVASCRIPT - DOM MANIPULATION
======================================================================

DESCRIPTION
-----------
Ce projet introduit la manipulation du DOM (Document Object Model) en
JavaScript. L’objectif est d’apprendre à sélectionner, modifier et mettre
à jour des éléments HTML directement dans le navigateur, sans recharger
la page.

Vous apprendrez également à effectuer des requêtes réseau (XHR, Fetch),
à écouter des événements du DOM et des interactions utilisateur, et à
mettre à jour dynamiquement le contenu d’une page web.

----------------------------------------------------------------------
RESOURCES
---------
What is JavaScript?
Introduction to the DOM
Document Interface
Element Class
Locating DOM elements using selectors
CSS Selectors
CSS Diner – Play with Selectors
DOM Scripting
Network Requests
What went wrong? Troubleshooting JavaScript

----------------------------------------------------------------------
LEARNING OBJECTIVES
-------------------
À la fin de ce projet, vous devez être capable d’expliquer clairement :

How to select HTML elements in JavaScript
    document.getElementById()
    document.getElementsByClassName()
    document.getElementsByTagName()
    document.querySelector()
    document.querySelectorAll()

What are differences between ID, class and tag name selectors
    ID    : unique, rapide, ciblage direct (#id)
    class : groupe d’éléments (.class)
    tag   : type d’élément (div, p, span…)

How to modify an HTML element style
    element.style.property = value

How to get and update an HTML element content
    element.textContent
    element.innerHTML

How to modify the DOM
    createElement()
    appendChild()
    removeChild()
    setAttribute()
    classList.add(), remove(), toggle()

How to make a request with XmlHTTPRequest
    XHR pour requêtes réseau basiques

How to make a request with Fetch API
    fetch(url).then(...).catch(...)

How to listen/bind to DOM events
    element.addEventListener('click', handler)

How to listen/bind to user events
    click, input, change, submit, keydown, mouseover…

----------------------------------------------------------------------
REQUIREMENTS
------------
GENERAL
    - Éditeurs autorisés : tous.
    - Tous les fichiers seront interprétés sur Chrome (version 57.0+)
    - Tous les fichiers doivent se terminer par une nouvelle ligne
    - Un fichier README.md significatif est obligatoire à la racine du projet
    - Le code doit être conforme semistandard
    - Vous n’êtes pas autorisé à utiliser var
    - La page HTML ne doit pas recharger pour chaque action :
          DOM manipulation, mise à jour de valeurs, fetch de données…

----------------------------------------------------------------------
OBJECTIF GLOBAL
---------------
Ce projet vous apprend à :
    - comprendre la structure du DOM,
    - sélectionner et manipuler des éléments HTML,
    - modifier dynamiquement le contenu d’une page,
    - écouter et gérer les événements utilisateur,
    - effectuer des requêtes réseau sans recharger la page,
    - construire des interfaces interactives en JavaScript pur.

======================================================================
