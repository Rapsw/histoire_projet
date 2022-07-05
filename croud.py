import sqlite3

# création des fonctions de la table Chapter

def creation_chapitre():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    ChapterId = 
    Summry = str(input("Entrer un nom de chapitre"))
    curseur.execute("INSERT INTO   VALUES(?,?,?)(")
    connexion.commit()
    connexion.close()
