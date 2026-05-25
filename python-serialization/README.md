======================================================================
README - Python Serialization & Marshaling
======================================================================

INTRODUCTION
------------
La sérialisation et le marshaling sont deux concepts fondamentaux en
informatique. Ils permettent de transformer des données en un format
transportable ou stockable, afin de faciliter la communication entre
systèmes ou la persistance d’informations.

Dans ce projet, vous explorerez en profondeur comment les données peuvent
être converties, transmises et reconstruites dans des environnements
réels : applications web, bases de données, systèmes distribués, etc.

----------------------------------------------------------------------
WHAT IS MARSHALING?
-------------------
Le marshaling consiste à transformer des objets en mémoire en un format
standardisé pouvant être transmis ou stocké.
Il s’agit souvent d’un format binaire compact.

Utilisations typiques :
- appels de procédures distantes (RPC),
- communication entre plateformes hétérogènes,
- transfert d’objets complexes via un réseau.

Le marshaling garantit que les objets et leurs attributs peuvent être
représentés de manière cohérente, quel que soit l’environnement.

----------------------------------------------------------------------
WHAT IS SERIALIZATION?
----------------------
La sérialisation est un cas particulier du marshaling : elle convertit
l’état d’un objet ou d’une structure de données en un format pouvant être
sauvegardé ou transmis.

Objectif principal :
- préserver l’état d’un objet pour le recréer ultérieurement à l’identique.

Applications courantes :
- persistance de données,
- communication réseau,
- stockage dans des fichiers,
- échanges entre composants logiciels.

Formats de sérialisation fréquents :
- JSON (lisible, universel),
- XML (structuré, verbeux),
- formats binaires (rapides, compacts).

----------------------------------------------------------------------
LEARNING OBJECTIVES
-------------------

À la fin de ce projet, vous serez capable de :

1. Expliquer les différences et similitudes entre marshaling et sérialisation.
2. Implémenter la sérialisation dans un programme Python.
3. Comprendre comment les données sérialisées sont utilisées dans :
   - les applications web,
   - les bases de données,
   - les communications réseau.
4. Évaluer les implications de performance selon le format choisi :
   JSON, XML, binaire, etc.

----------------------------------------------------------------------
CONCLUSION
----------
La sérialisation est un pilier des systèmes modernes : elle permet aux
données de voyager, de survivre à l’exécution d’un programme et d’être
partagées entre composants ou machines.

Maîtriser ces techniques vous prépare à aborder des sujets avancés comme
les APIs, les microservices, les systèmes distribués ou encore les
pipelines de données.

======================================================================
