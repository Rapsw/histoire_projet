import sqlite3
from datetime import datetime

from more_itertools import first

"""Toutes les fonctions n'ont pas été utilisé par manque de temps : certaines ont été crées pour optimiser ce brief (la partie facultatif)
   
"""
# Création des fonctions de la table User

def addUserInfo(username,password):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User VALUES(?,?,?);",(None,username,password))
    connexion.commit()
    connexion.close()
def User_in_Base(username):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM User WHERE Username = ?;", (username,))
    if len(curseur.fetchall())==0:
        return True
    else : 
        return False
        
def selectUserInfo():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM User")
    return curseur.fetchall()

def deleteUserInfo(userID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute(""" DELETE FROM User WHERE UserID = ?;""",(userID,))
    connexion.commit()
    connexion.close()

def updateUser(userID, username = None, password = None):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    if username is not None:
        curseur.execute("UPDATE User SET username = ? WHERE userID = ?;", (username, userID))
    if password is not None:
        curseur.execute("UPDATE User SET password = ? WHERE userID = ?;", (password, userID))
    connexion.commit()
    connexion.close()
def get_userID(username):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT UserID FROM User WHERE Username = ?;",(username,))
    return curseur.fetchall()[0]
def get_password(username):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Password FROM User WHERE Username = ?;",(username,))
    return curseur.fetchone()

# Création des fonctions de la table Challenge

def addChallenge(userID,paragraphID,text):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    vote = 0
    curseur.execute("INSERT INTO Challenge VALUES(?,?,?,?)",(userID,paragraphID,text,vote))
    connexion.commit()
    connexion.close()

def selectChallenge(paragraphID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,date,Challenge.Text,Vote FROM Challenge 
                       JOIN Paragraph ON Paragraph.ParagraphID = Challenge.ParagraphID
                       JOIN User ON User.UserID = Challenge.UserID
                       WHERE Paragraph.ParagraphID = ?;""",(paragraphID,))
    return curseur.fetchall()

def exist_Challenge(paragraphID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM Challenge JOIN Paragraph ON Paragraph.ParagraphID = Challenge.ParagraphID WHERE Challenge.ParagraphID=?;",(paragraphID,))
    challenge = curseur.fetchall()
    if len(challenge) == 0:
        print("Il n'y a pas de contestation existante.")
    else: 
        print(len(challenge))

def deleteChallenge():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Challenge ")
    connexion.commit()
    connexion.close()

def updateChallenge(userID, paragraphID, text, vote):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    if text is not None:
        curseur.execute("""UPDATE Challenge SET text = ?
                        WHERE userID = ? AND paragraphID = ?""", (text, userID, paragraphID))
    if vote is not None:
        curseur.execute("""UPDATE Challenge SET vote = ?
                        WHERE userID = ? AND paragraphID = ?""", (vote, userID, paragraphID))
    connexion.commit()
    connexion.close()
def voteChallenge(vote):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""UPDATE Challenge SET vote = ?;""",(vote))
    connexion.commit()
    connexion.close()



# Création des fonctions de la table Paragraph

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

def deleteParagraph(paragraphID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute(""" DELETE FROM Paragraph WHERE ParagraphID = ?;""",(paragraphID,))
    connexion.commit()
    connexion.close()
  
def updateParagraph(paragraphID, date = None, text = None):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    if date is not None:
        curseur.execute("""UPDATE Paragraph SET date = ? WHERE paragraphID = ?;""", (date, paragraphID))
    if text is not None:
        curseur.execute("""UPDATE Paragraph SET text = ? WHERE paragraphID = ?;""", (text, paragraphID))
    connexion.commit()
    connexion.close()
def lastParagraph():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,date,summary,text FROM Paragraph
                       JOIN User ON User.UserID =  Paragraph.UserID
                       JOIN Chapter ON Chapter.ChapterID = Paragraph.ChapterID
                       WHERE ParagraphID=(SELECT max(ParagraphID) FROM Paragraph);
    """)
    print(curseur.fetchall())
def get_lastParagraphID():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT ParagraphID FROM Paragraph
                       WHERE ParagraphID=(SELECT max(ParagraphID) FROM Paragraph);
    """)
    return curseur.fetchone()
def allParagraphsFromChapter(chapterID):
    
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT summary[0] FROM Paragraph
                       JOIN User ON User.UserID =  Paragraph.UserID
                       JOIN Chapter ON Chapter.ChapterID = Paragraph.ChapterID
                       WHERE Paragraph.ChapterID=?;""",(chapterID,))
    print("""                                """,
    
    
                        curseur.fetchone() ,"""
                                                      """)
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,date,text FROM Paragraph
                       JOIN User ON User.UserID =  Paragraph.UserID
                       JOIN Chapter ON Chapter.ChapterID = Paragraph.ChapterID
                       WHERE Paragraph.ChapterID=?;""",(chapterID,))
    return (curseur.fetchall())
def getUserIDfromLastParagraph():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT UserID FROM Paragraph
                       WHERE ParagraphID=(SELECT max(ParagraphID) FROM Paragraph);
    """)
    return curseur.fetchone()

    

# Création des fonctions de la table Comment

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

def maj_comment(CommentID, new_comment, new_text):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    if new_comment is not None:
        curseur.execute("UPDATE Comment SET Date = ? WHERE CommentID = ?", (str(datetime.now()), CommentID))
    if new_text is not None:
        curseur.execute("UPDATE Comment SET Text = ? WHERE CommentID = ?", (new_text, CommentID))
    connexion.commit()
    connexion.close()

def deleteComment(CommentID):
    connexion = sqlite3.connect("bdd.db")   
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Comment WHERE CommentID = ?;",(CommentID,))
    connexion.commit()
    connexion.close()

# création des fonctions de la table Chapter

def creation_chapitre(Summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES(?,?)",(None, Summary))
    connexion.commit()
    connexion.close()


def read_chapitre(ChapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Summary FROM Chapter WHERE ChapterID = ?;",(ChapterID,))
    print(curseur.fetchall())

def maj_chapitre(ChapterID, new_summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Chapter SET Summary = ? WHERE ChapterID = ?", (new_summary, ChapterID))
    connexion.commit()
    connexion.close()

def supprimer_chapitre(ChapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Chapter WHERE ChapterID = ?;",(ChapterID,))
    connexion.commit()
    connexion.close()
def chapter_in_Base(ChapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT * from Chapter 
                       WHERE ChapterID = ?;""",(ChapterID,))
    chapter = curseur.fetchall()
    return len(chapter)
def lastChapterID():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT ChapterID FROM Chapter
                       
                       WHERE ChapterID=(SELECT max(ChapterID) FROM Chapter);
    """)
    return curseur.fetchone()




#Création des fonctions de la table IsInChapter

def addIsInChapter(CaracterID,ChapterID):

    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO IsInChapter VALUES(?,?)",(CaracterID,ChapterID))
    connexion.commit()
    connexion.close()


def verifyIsInChapter(firstname):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute(""" SELECT ChapterID,FirstName,LastName,Summary FROM IsInChapter
                        JOIN Caracter ON Caracter.CaracterID = IsInChapter.CaracterID
                        JOIN Chapter ON Chapter.ChapterID = IsInChapter.ChapterID
                        WHERE FirstName = ?,""",(firstname,))
    liste_personnage = curseur.fetchall()           
    if len(liste_personnage) == 0:
        print("Ce Personnage n'est présent dans aucun chapitre")
    else : 
        for i in liste_personnage :
            print(i)


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
    curseur.execute("SELECT FirstName,LastName,Resume FROM Caracter WHERE CaracterID = ?;",(caracterID,))
    personnages = curseur.fetchall()

    for i in personnages():
        print(i)
def printAllCaracter():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT FirstName,LastName,Resume,ChapterID From Caracter
                        JOIN IsInChapter ON Caracter.CaracterID = IsInChapter.CaracterID
                        GROUP BY FirstName
    """)
    liste = curseur.fetchall()
    for i in liste:
        print(i)
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

def get_lastCaracterID():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT CaracterID FROM Caracter
                       WHERE CaracterID=(SELECT max(CaracterID) FROM Caracter);
    """)
    return curseur.fetchone()

def get_CaracterID(firstname):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT CaracterID FROM Caracter
    
                       WHERE FirstName =?;""",(firstname,))
    caracterID = curseur.fetchone()
    return caracterID


