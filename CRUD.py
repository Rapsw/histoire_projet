import sqlite3
from datetime import datetime


#Création des fonctions de la table Caracter
def createCaracter(first_name, last_name, resume):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES(?,?,?,?)", (None,first_name,last_name, resume))
    connexion.commit()
    connexion.close()

def readCaracter(caracterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM Caracter WHERE CaracterID = ?;",(caracterID,))
    print(curseur.fetchall())

def updateCaracter(caracterID, first_name = None, last_name = None, resume = None):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    if first_name is not None:
        curseur.execute("UPDATE Caracter SET firstname = ? WHERE caracterID = ?;", (first_name, caracterID))
    if last_name is not None:
        curseur.execute("UPDATE Caracter SET lastname = ? WHERE caracterID = ?;", (last_name, caracterID))
    if resume is not None:
        curseur.execute("UPDATE Caracter SET resume = ? WHERE caracterID = ?;", (resume, caracterID))
    connexion.commit()
    connexion.close()

def deleteCaracter(caracterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Caracter WHERE CaracterID = ?;", (caracterID,))
    connexion.commit()
    connexion.close()

def updateUser(userID, username = None, password = None):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    if username is not None:
        curseur.execute("UPDATE User SET username = ? WHERE userID = ?;", (username, userID))
    if password is not None:
        curseur.execute("UPDATE User SET password = ? WHERE userID = ?;"), (password, userID)
    connexion.commit()
    connexion.close()

def updateParagraph(userID, chapterID, paragraphID, date = None, text = None):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    if date is not None:
        curseur.execute("""UPDATE Paragraph SET date = ? 
                        WHERE userID = ? AND chapterID = ? AND paragraphID = ?;"""), (date, userID, chapterID, paragraphID)
    if text is not None:
        curseur.execute("""UPDATE Paragraph SET text = ?
                        WHERE userID = ? AND chapterID = ? AND paragraphID = ?;"""), (text, userID, chapterID, paragraphID)
    connexion.commit()
    connexion.close()

def updateChallenge(userID, paragraphID, text = None, vote = None):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    if text is not None:
        curseur.execute("""UPDATE Challenge SET text = ?
                        WHERE userID = ? AND paragraphID = ?;"""), (text, userID, paragraphID)
    if vote is not None:
        curseur.execute("""UPDATE Challenge SET vote = ?
                        WHERE userID = ? AND paragraphID = ?;"""), (vote, userID, paragraphID)
    connexion.commit()
    connexion.close()