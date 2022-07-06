import CRUD as CD
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
    else : 
        
        choix = input("Vous ")
    
