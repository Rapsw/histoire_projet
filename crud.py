import sqlite3
from datetime import datetime
"""Création des fonctions de la table User
"""
def addUserInfo(username,password):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User VALUES(?,?,?);",(None,username,password))
    connexion.commit()
    connexion.close()

def readUserInfo(userID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Username,Password FROM User WHERE UserID = ?;",(userID,))
    print(curseur.fetchall())
def deleteUserInfo(userID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute(""" DELETE FROM User WHERE UserID = ?;""",(userID,))
    connexion.commit()
    connexion.close()


""" Création des fonctions de la table Comment
"""
def addComment(userID,chapterID,text):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    date = str(datetime.now())
    curseur.execute("INSERT INTO Comment VALUES(?,?,?,?,?)",(None,userID,chapterID,date,text))
    connexion.commit()
    connexion.close()
def readComment(chapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,date,text FROM Comment 
                       JOIN User ON User.UserID = Comment.UserID
                       JOIN Chapter ON Chapter.ChapterID = Comment.ChapterID
                       WHERE Chapter.ChapterID = ?;""",(chapterID,))
    print(curseur.fetchall())
def deleteComment(CommentID):
    connexion = sqlite3.connect("bdd.db")   
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Comment WHERE CommentID = ?;",(CommentID,))
    connexion.commit()
    connexion.close()



"""Création des fonctions de la table Challenge
"""
def addChallenge(userID,paragraphID,text,button):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    vote = 0
    while button != "J" or "JP":
        print("Rentrer ")
    if button == 'J':
        vote+=1
    else : vote-=1
    curseur.execute("INSERT INTO Comment VALUES(?,?,?,?)",(userID,paragraphID,text,vote))
    connexion.commit()
    connexion.close()

def readChallenge():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,Challenge.text,vote FROM Challenge 
                       JOIN User ON User.UserID = Challenge.UserID
                       JOIN Paragraph ON Paragraph.ParagraphID=Challenge.Paragraph.ID
                       WHERE Paragraph.ParagraphID=Challenge.Paragraph.ID
                       

                       """)
    print(curseur.fetchall())
def exist_Challenge(paragraphID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute(""" SELECT *
                        FROM Challenge
                        WHERE Paragraph.ParagraphID=?;""",(paragraphID,))
    if len(curseur.fetchone()) == 0:
        print("Ce Challenge n'existe pas")
    else : return curseur.fetchone()

def deleteChallenge(paragraphID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Challenge WHERE Paragraph.ParagraphID=?;",(paragraphID,))
    connexion.commit()
    connexion.close()




""" Création des fonctions de la table Paragraph
"""

def addParagraph(ChapterID,UserID,text):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    date = str(datetime.now())
    curseur.execute("INSERT INTO Paragraph VALUES(?,?,?,?,?)",(None,ChapterID,UserID,date,text))
    connexion.commit()
    connexion.close()

def readParagraph():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,date,text FROM Paragraph
                       JOIN User ON User.UserID = Paragraph.UserID
                       JOIN Chapter ON Chapter.ChapterID = Paragraph.ChapterID
                       
    """)
    print(curseur.fetchall())
def readParagraphUser(username):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,date,Summary,Paragraph.text,vote,Challenge.text FROM Paragraph
                       JOIN User ON User.UserID = Paragraph.UserID
                       JOIN Chapter ON Chapter.ChapterID = Paragraph.ChapterID
                       JOIN Challenge ON Challenge.ParagraphID = Paragraph.ParagraphID
                       WHERE Username == ? """, (username,))
    print(curseur.fetchall())
def deleteParagraph(paragraphID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute(""" DELETE FROM Paragraph WHERE ParagraphID = ?;""",(paragraphID,))
    connexion.commit()
    connexion.close()


"""Création des fonctions IsInChapter
"""
def addIsInChapter(CaracterID,ChapterID):

    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Comment VALUES(?,?)",(CaracterID,ChapterID))
    connexion.commit()
    connexion.close()

def verifyIsInChapter(CaracterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute(""" SELECT IsInChapter.ChapterID,FirstName,LastName FROM IsInChapter
                        JOIN Caracter ON Caracter.CaracterID = IsInChapter.CaracterID
                        JOIN Chapter ON Chapter.ChapterID = IsInChapter.ChapterID
                        WHERE Caracter.CaracterID = IsInChapter.CaracterID
                        GROUP BY IsInChapter.ChapterID
                        """)
    if len(curseur.fetchall) == 0:
        print("Ce Personnage n'est présent dans aucun chapitre")
    else : print(curseur.fetchall())

def creation_chapitre(Summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES(?,?)",(None, Summary))
    connexion.commit()
    connexion.close()


readParagraph()