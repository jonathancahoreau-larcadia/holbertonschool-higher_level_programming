======================================================================
README - Python, MySQL & SQLAlchemy ORM
======================================================================

INTRODUCTION & CONTEXTE
-----------------------
Dans ce projet, vous allez relier deux mondes essentiels du développement :
les bases de données et Python.

1) Première partie : utilisation du module MySQLdb
   - Connexion à une base MySQL
   - Exécution de requêtes SQL
   - Récupération et affichage des résultats

2) Deuxième partie : utilisation de SQLAlchemy
   - ORM (Object Relational Mapper)
   - Plus besoin d'écrire de SQL
   - Manipulation d'objets Python au lieu de tables SQL
   - Indépendance vis-à-vis du type de stockage

Exemple SANS ORM :
------------------
conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                       passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()

Exemple AVEC ORM :
------------------
engine = create_engine('mysql+mysqldb://root:root@localhost/my_db',
                       pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()

DIFFERENCE :
------------
Sans ORM : vous devez connaître et écrire du SQL.
Avec ORM : vous manipulez des objets Python, pas des requêtes SQL.

La difficulté principale : la syntaxe de l’ORM.
Lisez des tutoriels, pas toute la documentation d’un coup.

----------------------------------------------------------------------
RESSOURCES
----------
Object-relational mappers
mysqlclient/MySQLdb documentation
MySQLdb tutorial
SQLAlchemy tutorial
SQLAlchemy
mysqlclient/MySQLdb
Introduction to SQLAlchemy
Flask SQLAlchemy
10 common stumbling blocks for SQLAlchemy newbies
Python SQLAlchemy Cheatsheet
SQLAlchemy ORM Tutorial for Python Developers
SQLAlchemy Tutorial

----------------------------------------------------------------------
OBJECTIFS PEDAGOGIQUES
-----------------------
A la fin de ce projet, vous devez être capable de :

- Se connecter à une base MySQL depuis un script Python
- Sélectionner des lignes dans une table MySQL
- Insérer des lignes dans une table MySQL
- Expliquer ce qu’est un ORM
- Mapper une classe Python sur une table MySQL
- Manipuler des objets Python représentant des lignes SQL

----------------------------------------------------------------------
EXIGENCES DU PROJET
-------------------
- Éditeurs autorisés : vi, vim, emacs
- Exécution sur Ubuntu 20.04 LTS avec Python 3.8.5
- Utilisation de MySQLdb 2.0.x
- Utilisation de SQLAlchemy 1.4.x
- Tous les fichiers doivent se terminer par une nouvelle ligne
- Première ligne obligatoire : #!/usr/bin/python3
- README.md obligatoire à la racine du projet
- Code conforme à pycodestyle 2.7.*
- Tous les fichiers doivent être exécutables
- La longueur des fichiers sera testée avec wc
- Tous les modules doivent avoir une documentation
- Toutes les classes doivent avoir une documentation
- Toutes les fonctions doivent avoir une documentation
- Une documentation = une vraie phrase complète
- Interdiction d’utiliser execute() avec SQLAlchemy

----------------------------------------------------------------------
CONCLUSION
----------
Ce projet vous apprend à :
- comprendre la différence entre SQL direct et ORM,
- manipuler des données via Python plutôt que via SQL,
- structurer proprement vos modèles,
- préparer des projets plus avancés (API, frameworks, etc.).

======================================================================
