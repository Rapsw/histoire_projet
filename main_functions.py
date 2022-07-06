from re import A
import CRUD as CD
import hashlib
import sqlite3
def chiffrage_password(password):
    
    h = hashlib.new('sha256')
    h.update(password.encode())
    password=h.hexdigest()
    return password

def authentification(username,password):
 
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT * FROM User 
    WHERE Username = ? AND Password = ?;""",(username,password))
    correspond = curseur.fetchall()
    if len(correspond)<0:
        print("Votre mot de passe ou votre nom d'utilisateur ne correspondent pas")
        return False
    else :
        print("Connexion vers le meilleur projet de la promo ")
        return True


