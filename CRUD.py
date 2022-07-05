import sqlite3

#Création des fonctions de la table Caracter
def createCaracter():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    FirstName = input("Entrez le prénom du personnage: ")
    LastName = input("Entrez le nom du personnage: ")
    Resume = input("Décrivez succinctement l'histoire du personnage: ")
    curseur.execute("INSERT INTO Caracter VALUES(?,?,?,?)", (None,FirstName,LastName, Resume))
    connexion.commit()
    connexion.close()

def readCaracter():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT FirstName, LastName, Resume FROM Caracter GROUP BY CaracterID")
    curseur.fetchall()

def updateCaracter(FirstName = None, LastName = None, Resume = None):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    NewFirstName= input("Entrez le nouveau prénom du personnage: ")
    NewLastName = input("Entrez le nouveau nom du personnage: ")
    curseur.execute("""UPDATE Caracter 
    if FirstName is not None:
        SET FirstName = NewFirstName""")
    curseur.execute("""UPDATE Caracter 
    if LastName is not None:
        SET LastName = NewLastName""")
    connexion.commit()
    connexion.close()

def deleteCaracter():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    CaracterToBeDeleted = int(input("Entrez l'ID du personnage à supprimer: "))
    curseur.execute("DELETE FROM Caracter WHERE CaracterID = CaracterToBeDeleted")
    connexion.commit()
    connexion.close()


