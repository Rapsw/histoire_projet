import CRUD as CD
import hashlib
import sqlite3

def chiffrage_password(password):
    
    h = hashlib.new('sha256')
    h.update(password.encode())
    chiffred_password=h.hexdigest()
    return chiffred_password

def authentification(username,password):
    
    chiffred_password = chiffrage_password(password)
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT * FROM User 
    WHERE Username = ? AND Password = ?;""",(username,chiffred_password,))
    correspond = curseur.fetchall()
    if len(correspond) < 1:
        print("Votre mot de passe ou votre nom d'utilisateur ne correspondent pas")
        return False
    else :
        print(""" 
                ###############################################################################################################
                #                                                                                                             #
                #              CONNEXION VERS LE MEILLEUR PROJET DE LA PROMO                                                  #
                #                                                                                                             #
                #                                                                                                             #
                ############################################################################################################### 
            """)
        return True
