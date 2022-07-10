import CRUD as CD
import hashlib
import sqlite3

def chiffrage_password(password):
    """ parameters : password qui prend un str en paramètre
    cette fonction prend le mot de passe donné en paramètre et le renvoie en chiffré
    """
    h = hashlib.new('sha256')
    h.update(password.encode())
    chiffred_password=h.hexdigest()
    return chiffred_password

def authentification(username,password):
    """ parameters : username et password qui sont de types str
    cette fonction prend le pseudo et le mot de passe donne en paramètre et verifie qu'elle corresponde bien à la base de donné
    avec la conditon du WHERE dans notre curseur execute si elle ne trouve pas le mdp dans la base de donné elle renvoie un message d'erreur
    sinon elle renvoie un message de connexion et renvoie True
    """
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

