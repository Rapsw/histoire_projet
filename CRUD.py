import sqlite3

#Création des fonctions de la table Caracter
def createCaracter():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    FirstName = str(input("Entrez le prénom du personnage: "))
    LastName = str(input("Entrez le nom du personnage: "))
    Resume = str(input("Décrivez succinctement l'histoire du personnage: "))
    curseur.execute("INSERT INTO Caracter VALUES(?,?,?,?)", (None,FirstName,LastName, Resume))
    connexion.commit()
    connexion.close()

def readCaracter():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT FirstName, LastName, Resume FROM Caracter GROUP BY CaracterID")


