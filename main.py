from click import option
import CRUD as CD
import sqlite3
import main_functions as mf



n=0
fini = False
utilisateur_online=False
liste_chapitre_cloture = []
mega_boucle = False
while mega_boucle == False :
    #############
    # CONNEXION #
    #############
    reponse = input("""Avez vous un compte ? 
                    O pour Oui 
                    N for Non 
                    
                    Réponse : """)
    if reponse == 'N':
        print("Création du compte")
        username = input("Entrer un nom d'utilisateur ")
        alreadyused = CD.User_in_Base(username)
        while alreadyused == False:
            print("Ce nom d'utilisateur est déja pris ")
            username = input("Entrer un nom d'utilisateur ")
            alreadyused = CD.User_in_Base(username)
        password = input("Entrer un mot de passe ")
        CD.addUserInfo(username,mf.chiffrage_password(password))
    elif reponse == 'O': 
            while fini == False:
                    username = input("Entez un nom d'utilisateur ")
                    password = input("Entrez un mot de passe ")
                    fini =mf.authentification(username,password)
            userID=CD.get_userID(username)
            paragraphID = CD.get_lastParagraphID
            ###################
            # MENU PRINCIPAL  #
            ###################
            while utilisateur_online == True:
                CD.lastParagraph()
                user_choice = input(""" 
                ###############################################################################################################
                #                                                                                                             #
                #              Entrez la commande correspondant à votre choix:                                                #
                #              -1 pour lire l'histoire en cours                                                               #
                #              -2 pour laisser un commentaire                                                                 #
                #              -3 pour contester le paragraphe en cours                                                       #
                #              -4 pour écrire un nouveau paragraphe                                                           #
                #              -5 pour se déconnecter                                                                         #
                #                                                                                                             #
                #                                                                                                             #
                ############################################################################################################### 
                    
                """)
                if user_choice == '1':
                    CD.read_chapitre(1)
                elif user_choice == '2':
                ##########################################################
                # CHOIX 2 : LAISSEZ UN COMMENTAIRE DANS UN CHAPITRE      #
                ##########################################################
                    
                    laisser_un_commentaire = False
                    while laisser_un_commentaire == False:
                        affiche_comment = input("""
                ###############################################################################################################
                #                                                                                                             #
                #                           COMMENTAIRES                                                                      #
                #                               -1 Ecrire un commentaire dans un chapitre                                     #
                #                               -2 Affiche les commentaires d'un chapitre                                     #
                #                               -3 Menu précèdent                                                             #
                #                                                                                                             #
                #                                                                                                             #
                ############################################################################################################### 
                """)
                        if affiche_comment == "1":
                            chapterID = int(input("Entrez le numéro du chapitre ou vous voulez commenter "))
                            commentaire = input("Ecrivez votre commentaire : ")
                            CD.addComment(userID[0],chapterID,commentaire)
                            CD.readComment(chapterID)

                        elif affiche_comment == "2":
                            chapterID = int(input("Entrez le numero du chapitre que vous voulez commenter "))
                            CD.readComment(chapterID)
                        elif affiche_comment == "3":
                            laisser_un_commentaire=True 
                        else: 
                            print("Commande invalide")

                elif user_choice == '3':
                    ################################################
                    # CHOIX 3 : CONTESTER UN LE DERNIER PARAGRAPHE #
                    ################################################
                    while contester_paragraphe == False:
                        contest = input("""
                ###############################################################################################################
                #                                                                                                             #
                #                           CONTESTER LE PARAGRAPHE                                                           #
                #                               -1 Ecrire votre contestation                                                  #
                #                               -2 Menu précèdent                                                             #
                #                                                                                                             #
                #                                                                                                             #
                #                                                                                                             #
                ############################################################################################################### 
                """)
                        if contest == "1":
                            challenge = input("Entrez votre argumentation de contestation")
                            CD.addChallenge(userID[0],paragraphID[0],challenge)
                        elif contest == "2":
                            contester_paragraphe = True 
                        else: 
                            print("Commande invalide")

                elif user_choice == '4':
                    #####################
                    # CHOIX 4 : ECRIRE  #
                    #####################
                    option_en_cours = False
                    while option_en_cours == False:
                            writer_choice = input("""
                ###############################################################################################################
                #                                                                                                             #
                #                           ECRIRE UNE HISTOIRE ,CHOISIR UNE OPTION :                                         #
                #                               -1 Clore le chapitre                                                          #
                #                               -2 Ecrire un nouveau paragraphe                                               #
                #                               -3 Personnages                                                                #
                #                               -4 menu précèdent                                                             #
                #                                                                                                             #
                ###############################################################################################################            
                    
                            """)
                            if writer_choice == '1':
                                ###################################
                                # CHOIX 4.1 : CLOTURER UN CHAPITRE  #
                                ###################################
                                chapitre_en_cours = CD.lastChapter()
                                liste_chapitre_cloture.append(chapitre_en_cours[0]) 
                                print("le chapitre ",chapitre_en_cours[0]," est cloturé") 
                            elif writer_choice == '2':
                                ###########################################
                                # CHOIX 4.2 : ECRIRE UN NOUVEAU PARAGRAPHE  #
                                ###########################################
                                chapitre_en_cours = CD.lastChapter()
                                création = False
                                if chapitre_en_cours[0] in liste_chapitre_cloture:
                                    #################################################################
                                    # ECRITURE DU NOUVEAU PARAGRAPHE MAIS LE CHAPITRE EST CLOTURE   #
                                    #################################################################
                                    print("vous ne pouvez pas écrire dans ce chapitre ,il est cloturé il vous faut créer un nouveau chapitre :")
                                    chapter_name = input("Entrez le nom de votre nouveau chapitre ")
                                    while len(chapter_name)>40:
                                        chapter_name = input("Entrez un autre nom celui ci est trop grand :")
                                    CD.creation_chapitre(chapter_name)
                                    new_chapter = CD.lastChapter
                                    en_cours= False
                                    ##########################
                                    # CREATION DU PERSONNAGE #
                                    ##########################
                                    while en_cours ==False:
                                        choisir = input("Voulez vous créer un personnage ? O pour oui N pour Non : ")
                                        if choisir == 'O':
                                            while création == False :
                                                firstname = input("Entrez le prénom de votre nouveau personnage :")
                                                lastname = input("Entrez le nom de votre nouveau personnage :")
                                                resume = input("Ecrire un résumé du personnage :")
                                                CD.createCaracter(firstname,lastname,resume)
                                                personnage = CD.get_lastCaracterID()
                                                CD.addIsInChapter(personnage[0],new_chapter[0])
                                                choix = input("Voulez vous en créer un autre ? O pour Oui N pour Non :")
                                                if choix == 'O':
                                                    création = False
                                                else : création = True
                                    ###########################################
                                    # CREATION DU PARAGRAPHE APRES PERSONNAGE #
                                    ###########################################
                                            new_paragraph = input("Ecrivez un nouveau paragraphe :")
                                            CD.addParagraph(new_chapter[0],userID[0],new_paragraph)
                                            en_cours = True
                                        elif choisir == 'N':
                                    #####################################################################
                                    # RAJOUTER UN PARAGRAPHE DANS L'HISTOIRE SANS AJOUTER DE PERSONNAGE #
                                    #####################################################################
                                            new_paragraph = input("Ecrivez un nouveau paragraphe :")
                                            CD.addParagraph(new_chapter[0],userID[0],new_paragraph)
                                            en_cours = True
                                        else : print("Entre un vrai choix frérot ")
                                else :
                                    #################################################
                                    # ECRIRE UN NOUVEAU PARAGRAPHE DANS UN CHAPITRE #
                                    #################################################
                                    en_cours= False
                                    while en_cours ==False:
                                        choisir = input("Voulez vous créer un personnage ? O pour oui N pour Non : ")
                                        if choisir == 'O':
                                            while création == False :
                                                firstname = input("Entrez le prénom de votre nouveau personnage :")
                                                lastname = input("Entrez le nom de votre nouveau personnage :")
                                                resume = input("Ecrire un résumé du personnage :")
                                                CD.createCaracter(firstname,lastname,resume)
                                                personnage = CD.get_lastCaracterID()
                                                CD.addIsInChapter(personnage[0],chapitre_en_cours[0])
                                                choix = input("Voulez vous en créer un autre ? O pour Oui N pour Non :")
                                                if choix == 'O':
                                                    création = False
                                                else : création = True
                                            new_paragraph = input("Ecrivez un nouveau paragraphe :")
                                            CD.addParagraph(chapitre_en_cours[0],userID[0],new_paragraph)
                                            en_cours = True
                                        elif choisir == 'N':
                                            new_paragraph = input("Ecrivez un nouveau paragraphe :")
                                            CD.addParagraph(chapitre_en_cours[0],userID[0],new_paragraph)
                                            en_cours = True
                                        else : 
                                            print("Entre un vrai choix frérot ")
                            elif writer_choice == '3':
                                pass
                            elif writer_choice == '4':
                            ##########################
                            # CHOIX 4.4 RETOUR MENU  #
                            ##########################
                                option_en_cours = True
                            else : 
                                print("Commande invalide. Veuillez entrer une commande valide!")
                elif user_choice == '5':
                    utilisateur_online = False
                else:
                    print("Commande invalide. Veuillez entrer une commande valide!")
    else :
        print("Commande Invalide, Veuillez réessayez")               
                

    
