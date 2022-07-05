import sqlite3
from datetime import datetime

# création des fonctions de la table Chapter

def creation_chapitre(Summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES(?,?)",(None, Summary))
    connexion.commit()
    connexion.close()

def read_chapitre():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Summary FROM Chapter")
    curseur.fetchall()


# fonction pour suprimer chapitres

def supprimer_chapitre(ChapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Chapter WHERE ChapterID = ?;", (ChapterID,))
    connexion.commit()
    connexion.close()

# fonction pour mettre à jour chapitre

def maj_chapitre(ChapterID, new_summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Chapter SET Summary = ? WHERE ChapterID = ?", (new_summary, ChapterID))
    connexion.commit()
    connexion.close()

# fonction pour metre à jour comment

def maj_comment(CommentID, new_comment, new_text):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
        if new_comment is not None
            curseur.execute("UPDATE Comment SET Date = ? WHERE CommentID = ?", (new_comment, CommentID))
        if new_text is not None
            curseur.execute("UPDATE Comment SET Text = ? WHERE CommentID = ?", (new_text, CommentID))
        connexion.commit()
        connexion.close()

