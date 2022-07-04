import Storytelling
import sqlite3
from datetime import datetime
"""Création des fonctions de la table User
"""
def addUserInfo():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    username = str(input("Entrez un nom d'utilisateur"))
    password = str(input("Entrez un mot de passe"))
    curseur.execute("INSERT INTO Username VALUES(?,?,?)",(None,username,password))
    connexion.commit()
    connexion.close()

def readUserInfo():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Username,Password FROM User GROUP BY Username")
    curseur.fetchall()

""" Création des fonctions de la table Comment
"""
def addComment(UserID,ChapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    date = str(datetime.now())
    text = str(input("Ecrivez un commentaire"))
    curseur.execute("INSERT INTO Comment UserID,ChapterID ")
    curseur.execute("INSERT INTO Comment VALUES(?,?,?,?,?)",(None,UserID,ChapterID,date,text))
    connexion.commit()
    connexion.close()
def readComment():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,date,text FROM User 
                       JOIN User ON User.UserID = Comment.UserID
                       GROUP BY Username

                       """)
    curseur.fetchall()

"""Création des fonctions de la table Challenge
"""
def addChallenge(UserID,ParagraphID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    text = str(input("Ecrivez un Challenge"))
    button = input("Entrer 'J' pour J'aime ou 'JP' pour  j'aime pas")
    vote = 0
    if button == 'j':
        vote-=1
    else : vote+=1
    
    curseur.execute("INSERT INTO Comment VALUES(?,?,?,?)",(UserID,ParagraphID,text,vote))
    connexion.commit()
    connexion.close()

def readChallenge():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,text,vote FROM Challenge 
                       JOIN User ON User.UserID = Challenge.UserID
                       GROUP BY Username

                       """)
    curseur.fetchall()

""" Création des fonctions de la table Paragraph
"""
def addParagraph(ChapterID,UserID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    text = str(input("Ecrivez un paragraphe"))
    date = str(datetime.now())
    curseur.execute("INSERT INTO Comment VALUES(?,?,?,?,?)",(None,ChapterID,UserID,date,text))





