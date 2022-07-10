# histoire_projet

README

# Logiciel participatif d'écriture d'histoires

Il s’agit d'écrire une histoire où de nombreux internautes participent à la création de celle-ci. Ce programme (en console pour le moment) permettant à plusieurs utilisateurs d'écrire une histoire en collaborant. Chaque utilisateur pouvant écrire un paragraphe à la fois.

## Pré-requis

- MySQL
- Git
- Python

## Démarrage

Exécutez le programme avec **VSCODE**. Ensuite, dans la console, entrez le *nom d’utilisateur* et le *mot de passe*. Une fois dans le programme, vous pouvez ***lire l’histoire***, ***contester le dernier message***, ***écrire la suite*** ou ***se déconnecter***. Le programme se divide en 3 parties principales :

1. Dans ***lire l’histoire*** vous pouvez : *aller à la page suivante*, *aller à la page précédente*, *choisir un chapitre*, *retourner au menu précédent* ou 

2. Dans ***contester le message*** vous pouvez : *contester le dernier paragraphe* ou *retourner au menu précédent*. 

3. Dans ***écrire la suite***, vous pouvez : *écrire la suite*, *retourner au menu précédent*, *ajouter un personnage existant*, *créer un nouveau personnage* ou *clore le chapitre*. 
4. Dans ***lire les commentaires***,vous pouvez : *écrire un commentaire*, *lire tous les commentaires dans un chapitre*
## Fabriqué avec

- **Visual Studio Code** - Editeur de code
- **Git** - Logiciel de gestion.
- **GitHub** - Site web et service de cloud pour stocker et gérer le code.
- **SQL** - Langage informatique servant à exploiter des bases de données relationnelles.
- **SQLite** - Bibliothèque écrite qui propose un moteur de base de données relationnelle accessible par le langage SQL.
- **Python** - Langage de programmation interprété.

## Versions

Dernière version : 1.0

## Auteurs

- Jeffrey NGUYEN alias <JynMoriarty> 
- Nina NUSBAUMER alias <NinaNusb>
- Rapsw CALAPSU alias <Rapsw> 

## Problème
Problème lié au main : au début du main on a initialisé des variables qui sont en dehors de notre programme et qui ont une certaine importance 
si par malheur quelqu'un s'amuse à sortir du programme , les variables lors du deuxième lancement du programme seront remis à zero , il se pourrait que le lecteur puisse continuer à écrire meme si une contestation est en cours puisque les paramètres du main ont été remis à zéro.