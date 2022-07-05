import sqlite3

from sympy import Id

# création des fonctions de la table Chapter

def creation_chapitre():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    Summary = str(input("Entrer un nom de chapitre"))
    curseur.execute("INSERT INTO Chapter VALUES(?,?)",(None, Summary))
    connexion.commit()
    connexion.close()

# fonction pour suprimer chapitres

def supprimer_chapitre():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Chapter WHERE ChapterID = ?;", (Id,))
    connexion.commit()
    connexion.close()

# fonction pour mettre à jour chapitre

def maj_chapitre():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Chapter SET Summary = ? WHERE ChapterID = ?", (id))
    connexion.commit()
    connexion.close()

