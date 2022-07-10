from datetime import datetime
import CRUD as CD
import main_functions as mf


liste_chapitre_cloture = []
challenge_encours = []
liste_voteurs = []
nb_utilisateurs = []
vote = 0
mega_boucle = False

""" liste des variables qu'on a pas envie de modifié lorsqu'un nouveau utilisateur se connecte elle sont alors définies en dehors de la megaboucle
"""
while mega_boucle == False :
    #############
    # CONNEXION #
    #############
    """"Simple demande à l'utilisateur d'envoyer une reponse pour savoir si il a un compte si non il en crée un et est renvoyé au à cette demande et si oui il se connecte
        les variable fini sont pour l'authentification et utilisateur_online pour la boucle quand l'utilisateur est connecté
        ces variables sont bien en dehors de leurs boucleurs respectives pour ne passe causer de boucle infinis ou d'erreurs.
    """
    reponse = None
    fini = False
    utilisateur_online=True
    
    reponse = input(""" 
                ###############################################################################################################
                #                                                                                                             #
                #              AVEZ VOUS UN COMPTE ?                                                                          #
                #              -O pour Oui                                                                                    #
                #              -N pour Non                                                                                    #
                #                                                                                                             #
                ############################################################################################################### 
                """)
    if reponse == 'N':
    ######################
    # CREATION DU COMPTE #
    ######################
        print("Création du compte")
        username = input("Entrer un nom d'utilisateur ")
        alreadyused = CD.User_in_Base(username)
        while alreadyused == False:
            print("Ce nom d'utilisateur est déja pris ")
            username = input("Entrer un nom d'utilisateur ")
            alreadyused = CD.User_in_Base(username)
        password = input("Entrer un mot de passe ")
        CD.addUserInfo(username,mf.chiffrage_password(password))
        nb_utilisateurs=CD.selectUserInfo()
        """ on demande à l'utilisateur de de créer un pseudo et un mot de passe et tant que ce pseudo n'est pas déja utilisé elle lui demande d'en taper un nouveau
        quand le pseudo donné est nouveau on ajoutre l'utilisateur à l'a pas de donné
        à chaque fois qu'un utilisateur est rentré dans la base de donné on va changer la longueur de la liste nb_utilisateurs
        """
    elif reponse == 'O': 
    ##################################
    # UTILISATEUR ENTRE DANS LA BASE #
    ##################################
        while fini == False:
            
            username = input("Entez un nom d'utilisateur ")
            password = input("Entrez un mot de passe ")
            fini =mf.authentification(username,password)
        userID=CD.get_userID(username)
        paragraphID = CD.get_lastParagraphID()
        """ tant que fini est faux faux on demande à l'utilisateur qui a compte de rentrer des identifiants correctes
            les variables userID et paragraphID sont importants elle recupérent l'ID de l'utilisateurs et du dernier paragraphe ce sont des liste de 1 tuple
            donc pour les utiliser on devra mettre un [0] après les avoir appelés
        """
        while utilisateur_online == True:
            """tant que utilisateur online est vrai on boucle
            """
            ###################
            # MENU PRINCIPAL  #
            ###################
            CD.lastParagraph()
            if len(challenge_encours)>0:
                print(CD.selectChallenge(paragraphID[0]))
            """ avec lastParagraph on affiche le dernier paragraphe si il existe un challenge on l'affiche aussi
            """
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
            ####################################
            # CHOIX 1 : LECTURE D'UNE HISTOIRE #
            ####################################
                """Variable du menu principale du choix "menu" qui va nous permettre de boucler et aussi de sortir de cette boucle
                """
                menu = False 
                while menu == False :
                    user_choice = input(""" 
                ###############################################################################################################
                #                                                                                                             #
                #              LIRE L'HISTOIRE EN COURS                                                                       #
                #              -1 Lire le chapitre en cours                                                                   #
                #              -2 Lire un autre chapitre                                                                      #
                #              -3 Menu précèdent                                                                              #
                #                                                                                                             #
                #                                                                                                             #
                ############################################################################################################### 
                    
                """)
                    if user_choice == '1':
                    #######################################
                    # CHOIX 1.1 LIRE LE CHAPITRE EN COURS #
                    #######################################
                        liste_paragraphes=[]
                        chapitre_actuel = CD.lastChapterID()
                        liste_paragraphes.append(CD.allParagraphsFromChapter(chapitre_actuel[0]))
                        menu2 = False
                        i = 0
                        """initialisation des variables importantes du choix 1.1 elle sont en dehors de la boucle pour les utiliser sans aucune réaffection plus tard
                            lastchapter nous renvoie une liste de 1 tuple contenat l'ID du chapitre en cours
                            liste_paragraphes est une liste de liste des paragraphes du chapitre en cours
                        """
                        while menu2 == False:
                            
                            print(liste_paragraphes[0][0])
                            #"affichage du premier élément du premier paragraphe liste_paragraphe étant une liste de liste le deuxième [] va permettre de passer ou de revenir à une page"
                            user_choice = input(""" 
                ###############################################################################################################
                #                                                                                                             #
                #              LIRE CHAPITRE EN COURS                                                                         #
                #              -1 Paragraphe suivant                                                                          #
                #              -2 Laissez un commentaire                                                                      #
                #              -3 Menu précèdent                                                                              #
                #                                                                                                             #
                ############################################################################################################### 
                    
                """)      
                            if user_choice == '1':
                            ###################################
                            # CHOIX 1.1.1 PARAGRAPHE SUIVANTE #
                            ###################################
                                if len(liste_paragraphes[0])>1:
                                    i +=1
                                    print(liste_paragraphes[0][i])
                                else :
                                    print("c'est la première et derniere page")
                                menu3 = False
                                while menu3 == False:
                                    user_choice = input(""" 
                ###############################################################################################################
                #                                                                                                             #
                #              LIRE CHAPITRE EN COURS                                                                         #
                #              -1 Paragraphe suivant                                                                          #
                #              -2 Paragraphe précèdent                                                                        #
                #              -3 Menu précèdent                                                                              #
                #                                                                                                             #
                ############################################################################################################### 
                """)                
                                    if user_choice == "1":
                                        if i < len(liste_paragraphes[0])-1:
                                            i += 1
                                            print(liste_paragraphes[0][i])
                                        else : 
                                            print("vous etes au dernier chapitre")     
                                    elif user_choice =="2":
                                        if i > 0 : 
                                            i-=1
                                            print(liste_paragraphes[0][i])
                                        else : 
                                            
                                            menu3 = True
                                    elif  user_choice =="3":
                                        menu3 = True
                                    else:
                                        print("Commande invalide. Veuillez entrer une commande valide!")
                                    """ si l'utlisateur choisit 1 on incrémente i de plus 1 et on print le paragraph suivant tant que i est bien inférieur à la longueur de la liste -1 c'est à dire
                                    tant qu'on est bien à al derniere page sinon elle nous renvoie en boucle que l'on est à la dernière page
                                    si l'utilisateur choisit 2 on décremente i de moins 1 tant que i est supérieur à 0 c'est à dire tant qu'on à la deuxième sinon elle nous renvoie au menu principal à 
                                    la première page
                                    """
                            elif user_choice == '2':
                            ######################################
                            # CHOIX 1.1.2 LAISSER UN COMMENTAIRE #
                            ######################################
                                text_user = input("Ecrivez votre commentaire : ")
                                CD.addComment(userID[0] ,chapitre_actuel[0],text_user)
                                
                            elif user_choice == '3':
                            ##############################
                            # CHOIX 1.1.3 MENU PRECEDENT #
                            ##############################
                                menu2 = True
                            else:
                                print("Commande invalide. Veuillez entrer une commande valide!")
                    elif user_choice == '2':
                    ################################
                    # CHOIX 1.2 LIRE UN AUTRE CHAPITRE #
                    #################################
                        menu2 = False
                        i = 0
                        chapter_choice = int(input("Entrez le numéro du chapitre: "))
                        while CD.chapter_in_Base(chapter_choice) == 0:
                            chapter_choice = int(input("Entrez un autre numéro , ce chapitre n'existe pas : "))
                        liste_paragraphes=[]
                        liste_paragraphes.append(CD.allParagraphsFromChapter(chapter_choice))
                        first_paragraph = liste_paragraphes[0][0]
                        """ lire un autre chapitre ressemble à lire un chapitre en cours sauf qu'on demande à l'utilisateur un chapterID particulier 
                        on doit ainsi donc changer également la liste paragraphes en lui ajoutant bien une liste de paragraphes correspondant bien au chapitre choisi
                        """
                        while menu2 == False:                  
                            print(first_paragraph)
                            user_choice = input(""" 
                ###############################################################################################################
                #                                                                                                             #
                #              LIRE UN AUTRE CHAPITRE                                                                         #
                #              -1 Paragraphe suivant                                                                          #
                #              -2 Laissez un commentaire                                                                      #
                #              -3 Menu précèdent                                                                              #
                #                                                                                                             #
                #                                                                                                             #
                ############################################################################################################### 
                    
                """)
                            if user_choice == '1':
                            #################################
                            # CHOIX 1.2.1 PARAGRAPE SUIVANT #
                            #################################
                                if len(liste_paragraphes[0])>1:
                                    i+=1
                                    print(liste_paragraphes[0][i])
                                else :
                                    print("c'est la première et derniere page")
                                
                                menu3 = False
                                while menu3 == False:
                                    user_choice = input(""" 
                ###############################################################################################################
                #                                                                                                             #
                #              LIRE CHAPITRE EN COURS                                                                         #
                #              -1 Paragraphe suivant                                                                          #
                #              -2 Paragraphe précèdent                                                                        #
                #              -3 Menu précèdent                                                                              #
                #                                                                                                             #
                ############################################################################################################### 

                """)                
                                    if user_choice == "1":
                                        if i < len(liste_paragraphes[0])-1:
                                            i += 1
                                            print(liste_paragraphes[0][i])
                                        else : 
                                            print("vous etes au dernier chapitre")
                                    elif user_choice == "2":
                                        if i > 1 : 
                                            i-= 1
                                            print(liste_paragraphes[0][i])
                                        else :
                                            print("Vous etes retournés au premier paragraphe")
                                            menu3 = True
                                    elif  user_choice == "3":
                                        menu3 = True
                                    else :
                                         print("commande invalide")
                            elif user_choice == '2':
                            ######################################
                            # CHOIX 1.1.2 LAISSER UN COMMENTAIRE #
                            ######################################
                                text_user = input("Ecrivez votre commentaire : ")
                                CD.addComment(userID[0] ,chapter_choice[0],text_user)
                            elif user_choice == '3':
                            ##############################
                            # CHOIX 1.2.3 MENU PRECEDENT #
                            ##############################
                                menu2 = True
                            else:
                                print("Commande invalide. Veuillez entrer une commande valide!")
                    elif user_choice == '3':
                    #############################
                    # CHOIX 1.3 MENU PRECEDENT  #
                    #############################
                        menu = True
                    else:
                        print("Commande invalide. Veuillez entrer une commande valide!")
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
                    elif affiche_comment == "2":
                        chapterID = int(input("Entrez le numero du chapitre dont vous voulez voir les commentaires "))
                        CD.readComment(chapterID)
                    elif affiche_comment == "3":
                        laisser_un_commentaire=True 
                    else: 
                        print("Commande invalide")

            elif user_choice == '3':
                ################################################
                # CHOIX 3 : CONTESTER UN LE DERNIER PARAGRAPHE #
                ################################################
                contester_paragraphe = False 
                while contester_paragraphe == False:

                    contest = input("""
                ###############################################################################################################
                #                                                                                                             #
                #                           CONTESTER LE PARAGRAPHE                                                           #
                #                               -1 Ecrire votre contestation                                                  #
                #                               -2 Lire la contestation en cours                                              #
                #                               -3 Voter                                                                      #
                #                               -4 Menu précèdent                                                             #
                #                                                                                                             #
                ############################################################################################################### 
                """)
                    if contest == "1":
                    ####################################
                    # CHOIX 3.1 ECRIRE LA CONTESTATION #
                    ####################################
                        """ Si il y'a un challenge en cours on renvoie l'utilisateur au menu principal lui disant qu'il y'en a déja un sinon 
                        on un crée un et Très IMPORTANT on ajoute ce challenge à notre variable challenge_encours
                        """
                        if len(challenge_encours) == 0:
                            challenge = input("Entrez votre argumentation de contestation : ")
                            CD.addChallenge(userID[0],paragraphID[0],challenge)
                            challenge_encours.append(CD.selectChallenge(paragraphID[0]))
                        else : 
                            print("Une contestation est déja en cours : retour au menu précèdent ")
                    elif contest == "2":
                    ##################################
                    # CHOIX 3.2 LIRE LA CONTESTATION #
                    ##################################
                        if len(challenge_encours) > 0:
                            CD.lastParagraph()
                            print(CD.selectChallenge(paragraphID[0]))
                        else : 
                            print("Il n'y a aucun constestation en cours : retour au menu précedent")
                        #"si un challenge est en cours on l'affiche avec le dernier paragraph sinon on lui envoie un message d'erreur"
                    elif contest == "3":
                        ###################
                        # CHOIX 3.3 VOTER #
                        ###################
                        """ Le vote fonctionne de la mnière suivante , un utilisateur ne peut voter qu'une fois , tous les utilisateurs doivent voté 
                        si le vote final est positif ou égale à 0 le challenge gagne et on supprime le paragraphe sinon il est supprimé
                        """
                        if userID in liste_voteurs:
                            print("Vous avez déja voter : retour au menu précèdent")
                        else :
                            bouton = input("Entrer 1 pour j'aime ou 2 pour j'aime pas : ")
                            if bouton == "1":
                                vote +=1
                                CD.voteChallenge(vote)
                                liste_voteurs.append(userID)
                                if len(liste_voteurs)==len(nb_utilisateurs):
                                    if vote < 0 :
                                        CD.deleteChallenge()
                                        liste_voteurs.clear()
                                        challenge_encours.clear()
                                    else:
                                        CD.deleteChallenge()
                                        CD.deleteParagraph(paragraphID[0])
                                        liste_voteurs.clear()
                                        challenge_encours.clear()
                            elif bouton == "2":
                                vote -=1
                                CD.voteChallenge(vote)
                                liste_voteurs.append(userID)
                                if len(liste_voteurs)== len(nb_utilisateurs):
                                    if vote < 0 :
                                        CD.deleteChallenge()
                                        liste_voteurs.clear()
                                        challenge_encours.clear()
                                    else:
                                        CD.deleteChallenge()
                                        CD.deleteParagraph(paragraphID[0])
                                        liste_voteurs.clear()
                                        challenge_encours.clear()
                            else :
                                print("choix invalide")
                    elif contest == "4":
                        contester_paragraphe = True 
                    else: 
                        print("Commande invalide")

            elif user_choice == '4':
                #####################
                # CHOIX 4 : ECRIRE  #
                #####################
                option_en_cours = False
                if len(challenge_encours) > 0 :
                    print("""
                VOUS NE POUVEZ PAS ECRIRE OU MODIFIER UN PERSONNAGE LORSQU'UNE CONTESTATION EST EN COURS 

                                            RETOUR AU MENU PRINCIPAL

                ALLEZVOTER!ALLEZVOTER!ALLEZVOTER!ALLEZVOTER!ALLEZVOTER!ALLEZVOTER!ALLEZVOTER!
                            
                            """)
                else :
                    while option_en_cours == False:
                        writer_choice = input("""
                ###############################################################################################################
                #                                                                                                             #
                #                           ECRIRE UNE HISTOIRE ,CHOISIR UNE OPTION :                                         #
                #                               -1 Clore le chapitre                                                          #
                #                               -2 Ecrire un nouveau paragraphe                                               #
                #                               -3 Personnages                                                                #
                #                               -4 Modifier un paragraphe                                                     #
                #                               -5 Menu précèdent                                                             #
                ###############################################################################################################            
                    
                            """)
                        if writer_choice == '1':
                            ###################################
                            # CHOIX 4.1 : CLOTURER UN CHAPITRE  #
                            ###################################
                            chapitre_en_cours = CD.lastChapterID()
                            liste_chapitre_cloture.append(chapitre_en_cours[0]) 
                            print("le chapitre ",chapitre_en_cours[0]," est cloturé") 
                            #POUR cloturer un chapitre on récuperer l'ID du chapitre et on le mets dans une liste de chapitre cloturés qu'on va utlisé plus tard"
                        elif writer_choice == '2':
                            ###########################################
                            # CHOIX 4.2 : ECRIRE UN NOUVEAU PARAGRAPHE  #
                            ###########################################
                            chapitre_en_cours = CD.lastChapterID()
                            création = False
                            #on initialise nos variables importantes 
                            if chapitre_en_cours[0] in liste_chapitre_cloture:
                                #################################################################
                                # ECRITURE DU NOUVEAU PARAGRAPHE MAIS LE CHAPITRE EST CLOTURE   #
                                #################################################################
                                print("vous ne pouvez pas écrire dans ce chapitre ,il est cloturé il vous faut créer un nouveau chapitre :")
                                chapter_name = input("Entrez le nom de votre nouveau chapitre ")
                                while len(chapter_name)>60:
                                    chapter_name = input("Entrez un autre nom celui ci est trop grand :")
                                CD.creation_chapitre(chapter_name)
                                new_chapter = CD.lastChapterID()
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
                            menu = False
                            while menu == False:
                                choix = input("""
                ###############################################################################################################
                #                                                                                                             #
                #                           PERSONNAGES                                                                       #
                #                               -1 Afficher tous les personnages                                              #
                #                               -2 Chercher un personnage                                                     #
                #                               -3 Modifier un personnage                                                     #
                #                               -4 menu précèdent                                                             #
                #                                                                                                             #
                ###############################################################################################################            
                    
                            """)
                                if choix == "1":
                                    CD.printAllCaracter()
                                elif choix == "2":
                                    firstname = input("Entrer le nom du personnage que vous voulez chercher : ")
                                    CD.verifyIsInChapter(firstname)  
                                elif choix == "3":
                                    menu2 = False
                                    while menu2 == False :
                                        choix = input("""
                ###############################################################################################################
                #                                                                                                             #
                #                           MODIFIER UN PERSONNAGE                                                            #
                #                               -1 Modfier un personnage                                                      #
                #                               -2 Mettre à jour les personnages figurant dans un chapitre                    #
                #                               -3 Menu précèdent                                                             #
                #                                                                                                             #
                ###############################################################################################################            
                    
                            """)
                                        if choix =='1':
                                            character_name = input("Entrez le prénom du personnage que vous voulez modifier :  ")
                                            caracterID = CD.get_CaracterID(character_name)
                                            update_firstname = input("Voulez vous modifier le prénom du personnage ? Entrez O pour Oui et N pour Non")
                                            if update_firstname == '0':
                                                new_firstname = input("Entrez le nouveau prénom du personnage : ")
                                            elif update_firstname == "N":
                                                new_firstname = None
                                            else : 
                                                print("commande invalide")
                                            update_lastname = input("Voulez vous modifier le nom du personnage ? Entrez O pour Oui et N pour Non")
                                            if update_lastname == '0':
                                                new_lastname = input("Entrez le nouveau nom du personnage : ")
                                            elif update_lastname == "N":
                                                new_lastname = None
                                            else : 
                                                print("commande invalide")
                                            update_resume = input("Voulez vous modifier le résumé du personnage ? Entrez O pour Oui et N pour Non")
                                            if update_resume == '0':
                                                new_resume = input("Entrez le nouveau résumé du personnage : ")
                                            elif update_resume == "N":
                                                new_resume = None
                                            else : 
                                                print("commande invalide")
                                            CD.updateCaracter(caracterID[0,new_firstname,new_lastname,new_resume])
                                            print("Le personnage a été modifié ")
                                        elif choix =="2":
                                            firstname = input("Entrer le nom du personnage")
                                            chapter = input("Entrer le numéro du nouveau chapitre ou vous avez mentionné un personnage existant ")
                                            caracterID = CD.get_CaracterID(firstname)
                                            CD.addIsInChapter(caracterID[0],chapter)
                                        elif choix =="3":
                                            menu2 = True
                                        else:
                                            print("Commande invalide. Veuillez entrer une commande valide!")
                                else:
                                    print("Commande invalide. Veuillez entrer une commande valide!")      
                        elif writer_choice == "4":
                            writerID = CD.getUserIDfromLastParagraph()
                            chapitre_en_cours = CD.lastChapterID()
                            if userID[0]== writerID[0]:
                                newtext=input("Veuillez entrer les modifications que vous voulez apporter à votrer paragraphe")
                                CD.updateParagraph(userID[0],chapitre_en_cours[0],paragraphID[0],str(datetime.now()),newtext)
                            else :
                                print("Vous n'êtes pas l'auteur du dernier paragraphe vous ne pouvez pas en conséquence le modifier: retour au menu précèdent ")
                        elif writer_choice == '5':
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
                

    
