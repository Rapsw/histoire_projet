import CRUD as CD
import main_functions
en_cours = 0
while en_cours < 5:
    reponse = input("Avez vous un compte ? O pour Oui N for Non ")
    if reponse == 'N':
        print("Création du compte")
        username = input("Entrer un nom d'utilisateur")
        alreadyused = CD.User_in_Base(username)
        while alreadyused == False:
            print("Ce nom d'utilisateur est déja pris ")
        password = input("Entrer un mot de passe")
        CD.addUserInfo(username,password)
    elif reponse == 'O': 

        emptyfile = CD.chapter_in_Base
        if emptyfile == False:
            choix = input("Voulez vous créer une nouvelle histoire ? Entrer O pour Oui ou N pour Non")
            while choix != 'O':
                print("Fais pas chier , c'est vide tu vas rien lire ou faire! Ecris une histoire bordel")
            nom_du_chapitre = input("Enter le nom du  premier chapitre de l'histoire communautaire ")
            CD.creation_chapitre(nom_du_chapitre)
            paragraph =  input("Ecrivez votre histoire. ")
            CD.addParagraph(1,CD.get_userID(username),paragraph)

                
                

    
