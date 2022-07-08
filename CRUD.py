import sqlite3
from datetime import datetime

from nbformat import read
from psutil import users

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
    if len(curseur.fetchone())<1:
        return True
    else : 
        return False
        
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

def updateUser(userID, username = None, password = None):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    if username is not None:
        curseur.execute("UPDATE User SET username = ? WHERE userID = ?;", (username, userID))
    if password is not None:
        curseur.execute("UPDATE User SET password = ? WHERE userID = ?;", (password, userID))
    connexion.commit()
    connexion.close()

# Création des fonctions de la table Challenge

def addChallenge(userID,paragraphID,text):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    vote = 0
    curseur.execute("INSERT INTO Challenge VALUES(?,?,?,?)",(userID,paragraphID,text,vote))
    connexion.commit()
    connexion.close()

def updateVoteChallenge(paragraphID, userVote):
    """
    Fonction qui modifie le nombre de votes sur un challenge
    :param paragraphID:(int) index du paragraph ayant provoqué un challenge
    :param userVote: (int) vote de l'utilisateur sous la forme d'un +1 ou -1
    :return: (table) tableau modifié
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Vote FROM Challenge WHERE paragraphID = ?", (paragraphID,))
    vote_precedent= curseur.fetchone()[0]
    vote_new = vote_precedent + userVote
    curseur.execute("UPDATE Challenge SET vote = ? WHERE paragraphID = ?",(vote_new, paragraphID))
    connexion.commit()
    connexion.close()

def readChallenge(paragraphID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Challenge.UserID, Challenge.ParagraphID, Challenge.Text, Challenge.Vote FROM Challenge 
                       JOIN Paragraph ON Paragraph.ParagraphID = Challenge.Paragraph.ID
                       WHERE Paragraph.ParagraphID = ?;""",(paragraphID,))
    print(curseur.fetchall())

def exist_Challenge(paragraphID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM Challenge JOIN Paragraph ON Paragraph.ParagraphID = Challenge.ParagraphID WHERE Challenge.ParagraphID=?;",(paragraphID,))
    challenge = curseur.fetchall()
    if len(challenge) == 0:
        print("Il n'y a pas de contestation existante.")
    else: 
        print(len(challenge))

def deleteChallenge(paragraphID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Challenge WHERE ParagraphID = ?;",(paragraphID,))
    connexion.commit()
    connexion.close()

def updateChallenge(userID, paragraphID, text = None, vote = None):
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

# Création des fonctions de la table Paragraph

def addParagraph(ChapterID,UserID,text):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    date = str(datetime.now())
    curseur.execute("INSERT INTO Paragraph VALUES(?,?,?,?,?)",(None,ChapterID,UserID,date,text))
    connexion.commit()
    connexion.close()

def readParagraph(paragraphID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM Paragraph WHERE paragraphID =?;",(paragraphID,))
    print(curseur.fetchall())
    connexion.commit()
    connexion.close()

def readParagraphUser(userID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,date,text FROM Paragraph
                       JOIN User ON User.UserID = Paragraph.UserID
                       JOIN Chapter ON Chapter.ChapterID = Paragraph.ChapterID
    """)
    print(curseur.fetchall())

def allParagraphsFromChapter(chapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,date,text FROM Paragraph
                       JOIN User ON User.UserID =  Paragraph.UserID
                       JOIN Chapter ON Chapter.ChapterID = Paragraph.ChapterID
                       WHERE Paragraph.ChapterID=?;""",(chapterID,))
    return(curseur.fetchall())
    
def allParagraphsIDFromChapter(chapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT ParagraphID FROM Paragraph
                       JOIN User ON User.UserID =  Paragraph.UserID
                       JOIN Chapter ON Chapter.ChapterID = Paragraph.ChapterID
                       WHERE Paragraph.ChapterID=?;""",(chapterID,))
    return(curseur.fetchall())

def get_paragraphid_from_currentChapter():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT paragraphID FROM Paragraph
                       JOIN Chapter ON Chapter.ChapterID = Paragraph.ChapterID
                       WHERE ParagraphID=(SELECT min(ParagraphID) FROM Paragraph);
    """)
    return(curseur.fetchone())

def readLastParagraph():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,date,summary,text FROM Paragraph
                       JOIN User ON User.UserID = Paragraph.UserID
                       JOIN Chapter ON Chapter.ChapterID = Paragraph.ChapterID
                       WHERE ParagraphID=(SELECT max(ParagraphID) FROM Paragraph);
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

# Création des fonctions de la table Comment

def addComment(userID,chapterID,text):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    date = str(datetime.now())
    curseur.execute("INSERT INTO Comment VALUES(?,?,?,?,?)",(None,chapterID,userID,date,text))
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

def Chapter_in_Base(chapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM Chapter WHERE chapterID = ?;",(chapterID,))
    chapter = curseur.fetchall()
    if len(chapter)<1:
        print(True)
    else : 
        print(False)

def read_chapitre(ChapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Summary FROM Chapter WHERE ChapterID = ?;",(ChapterID,))
    print(curseur.fetchall())

def get_chapterid_from_lastChapter():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT ChapterID FROM Chapter
                       WHERE ChapterID=(SELECT max(ChapterID) FROM Chapter);
    """)
    return(curseur.fetchone())

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

#Création des fonctions de la table IsInChapter

def addIsInChapter(CaracterID,ChapterID):

    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO IsInChapter VALUES(?,?)",(CaracterID,ChapterID))
    connexion.commit()
    connexion.close()

def read_IsInChapter(IsInChapter):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute(""" SELECT IsInChapter.ChapterID,FirstName,LastName FROM IsInChapter
                        JOIN Caracter ON Caracter.CaracterID = IsInChapter.CaracterID
                        JOIN Chapter ON Chapter.ChapterID = IsInChapter.ChapterID
                        WHERE Caracter.CaracterID 
                        GROUP BY IsInChapter.ChapterID = ?;""",(IsInChapter,)) 
    if len(curseur.fetchall) == 0:
        print("Ce Personnage n'est présent dans aucun chapitre")
    else : print(curseur.fetchall())


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

def readAllCaracters(chapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Caracter.CaracterID, Caracter.FirstName, Caracter.LastName, Caracter.Resume FROM Caracter
    JOIN IsInChapter ON IsInChapter.CaracterID = Caracter.CaracterID 
    WHERE IsInChapter.ChapterID = ? """,(chapterID,))
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






