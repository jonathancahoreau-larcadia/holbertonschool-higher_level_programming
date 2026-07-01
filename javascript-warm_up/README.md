======================================================================
JAVASCRIPT - WARM UP
======================================================================

DESCRIPTION
-----------
Ce projet introduit les bases du langage JavaScript à travers des scripts
simples exécutés en ligne de commande. L’objectif est de comprendre les
fondamentaux du langage avant de l’utiliser dans des projets web plus
complexes (comme rendre AirBnB dynamique avec JavaScript et jQuery).

JavaScript est utilisé ici pour deux raisons :
    - Scripting (comme Python)
    - Web front-end (plus tard dans le cursus)

Ce projet se concentre uniquement sur le scripting pour apprendre les
concepts essentiels du langage.

----------------------------------------------------------------------
RESOURCES
---------
Writing JavaScript Code
Variables
Data Types
Operators
Operator Precedence
Controlling Program Flow
Functions
Objects and Arrays
Intrinsic Objects
Module patterns
var, let and const
JavaScript Tutorial
Modern JS

----------------------------------------------------------------------
LEARNING OBJECTIVES
-------------------
À la fin de ce projet, vous devez être capable d’expliquer clairement :

Why JavaScript programming is amazing
    Langage polyvalent, rapide, omniprésent dans le web.

How to run a JavaScript script
    Exécution via Node.js : node script.js

How to create variables and constants
    Utiliser var, let, const.

What are differences between var, const and let
    var   : portée fonction, ancien comportement
    let   : portée bloc, moderne
    const : valeur non réassignable

What are all the data types available in JavaScript
    string, number, boolean, object, array, null, undefined, symbol, bigint

How to use the if, if ... else statements
    Contrôler le flux d’exécution.

How to use comments
    // commentaire
    /* commentaire */

How to affect values to variables
    let x = 10;

How to use while and for loops
    Boucles pour répéter des instructions.

How to use break and continue statements
    break    : sortir d’une boucle
    continue : passer à l’itération suivante

What is a function and how do you use functions
    Déclarer, appeler, retourner des valeurs.

What does a function that does not use any return statement return
    undefined

Scope of variables
    global, fonction, bloc

What are the arithmetic operators and how to use them
    +, -, *, /, %, **

How to manipulate dictionary
    En JS : objets { key: value }

How to import a file
    require('./file.js')

----------------------------------------------------------------------
REQUIREMENTS
------------
GENERAL
    - Éditeurs autorisés : vi, vim, emacs
    - Tous les fichiers seront interprétés sur Ubuntu 20.04 LTS avec Node 14.x
    - Tous les fichiers doivent se terminer par une nouvelle ligne
    - Tous les fichiers doivent être exécutables
    - La première ligne de tous les fichiers doit être exactement :
          #!/usr/bin/node
    - Un fichier README.md est obligatoire à la racine du projet
    - Le code doit être conforme semistandard (version 16.x.x)
      (Standard + points-virgules)
      Référence : AirBnB style
    - La longueur des fichiers sera testée avec wc

----------------------------------------------------------------------
INSTALLATION
------------
Install Node 14 :
    $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    $ sudo apt-get install -y nodejs

Install semi-standard :
    $ sudo npm install semistandard --global

----------------------------------------------------------------------
OBJECTIF GLOBAL
---------------
Ce projet vous apprend à :
    - écrire du JavaScript propre et moderne,
    - comprendre les bases du langage avant d’aborder le front-end,
    - manipuler les variables, fonctions, objets et tableaux,
    - contrôler le flux d’exécution,
    - structurer des scripts exécutables avec Node.js,
    - préparer les compétences nécessaires pour les projets web dynamiques.

======================================================================
