import CRUD as CD
import sqlite3

userID = 1
utilisateur_online = False 

while utilisateur_online == False:
    CD.readLastParagraph()
    user_choice = input("""Entrez la commande correspondant à votre choix. 
        1 pour lire l'histoire en cours
        2 pour laisser un commentaire
        3 pour contester le paragraphe en cours
        4 pour écrire un nouveau paragraphe
        5 pour se déconnecter
        
    """)
    #################
    # Menu histoire #
    #################


    ### Si user veut lire l'histoire en cours ###
    if user_choice == '1':
        menu = False
        
        while menu == False :
            user_choice = input("""Entrez la commande correspondant à votre choix. 
            1 pour lire le chapitre actuel
            2 pour lire un autre chapitre
            3 pour retourner au menu précédent

            """)

            ### Si user veut lire chapitre en cours ###
            if user_choice == '1':
                menu2 = False
                liste_paragraphes = []
                chapitre_actuel = CD.get_chapterid_from_lastChapter()
                liste_paragraphes.insert(0,CD.allParagraphsFromChapter(chapitre_actuel[0]))
                print(liste_paragraphes[0][0][2])
                i= 0
                
                while menu2 == False:
                    user_choice = input("""Entrez la commande correspondant à votre choix. 
                    1 pour lire les paragraphes suivants
                    2 pour laisser un commentaire
                    3 pour lire les paragraphes précédents
                    4 pour revenir au menu précédent

                    """)

                    ### Si user veut lire les paragraphes suivants ### 
                    if user_choice == '1':
                        menu3 = False
                        while menu3 == False:
                            if i < len(liste_paragraphes):
                                i+=1
                                print(liste_paragraphes[0][i][2]) 
                            else:
                                
                                print(input("Vous êtes au dernier paragraphe.")) 
                                i = i-1 
                            menu3 = True

                    ### Si user veut laisser un commentaire sur le chapitre ###
                    elif user_choice == '2':
                       
                        menu3 = False
                        while menu3 == False:
                            text_user = input("Commencez l'écriture...")
                            CD.addComment(userID=userID, chapterID=chapitre_actuel[0],text=text_user)
                            menu3 = True

                    ### Si user veut lire les paragraphes précédents ###  ==> A CORRIGER
                    elif user_choice == '3':
                        
                        menu3 = False
                        while menu3 == False:
                            if i >= 0:
                                i-=1
                                print(liste_paragraphes[0][i-1][2]) #ordre à vérifier
                            else:
                                print(input("Vous êtes au premier paragraphe."))
                                i+=1
                            menu3 = True
                    
                    ### Si user veut revenir au menu précédent ###
                    elif user_choice == '4':
                        menu2 = True

            ### Si user veut lire un autre chapitre que celui en cours ###
            elif user_choice == '2':
                menu2 = False
                chapter_choice = int(input("Entrez le numéro du chapitre: "))
                liste_paragraphes = []
                chapitre_actuel = CD.get_chapterid_from_lastChapter()
                liste_paragraphes.insert(0,CD.allParagraphsFromChapter(chapitre_actuel[0]))
                print(liste_paragraphes[0][0][2])
                i= 0
                
                while menu2 == False:
                    user_choice = input("""Entrez la commande correspondant à votre choix. 
                    1 pour lire les paragraphes suivants
                    2 pour laisser un commentaire
                    3 pour lire les paragraphes précédents
                    4 pour revenir au menu précédent

                    """)

                    ### Si user veut lire les paragraphes suivants ### 
                    if user_choice == '1':
                        menu3 = False
                        while menu3 == False:
                            if i < len(liste_paragraphes):
                                i+=1
                                print(liste_paragraphes[0][i][2]) 
                            else:
                                
                                print(input("Vous êtes au dernier paragraphe.")) 
                                i = i-1 
                            menu3 = True

                    ### Si user veut laisser un commentaire sur le chapitre ###
                    elif user_choice == '2':
                       
                        menu3 = False
                        while menu3 == False:
                            text_user = input("Commencez l'écriture...")
                            CD.addComment(userID=userID, chapterID=chapitre_actuel[0],text=text_user)
                            menu3 = True

                    ### Si user veut lire les paragraphes précédents ###  ==> A CORRIGER
                    elif user_choice == '3':
                        
                        menu3 = False
                        while menu3 == False:
                            if i >= 0:
                                i-=1
                                print(liste_paragraphes[0][i-1][2]) #ordre à vérifier
                            else:
                                print(input("Vous êtes au premier paragraphe."))
                                i+=1
                            menu3 = True
                    
                    ### Si user veut revenir au menu précédent ###
                    elif user_choice == '4':
                        menu2 = True

            ### Si user veut retourner au menu principal ###
            elif user_choice == '3':
                menu = True
            



    elif user_choice == '2':
        CD.addComment(userID=userID[0])
    elif user_choice == '3':
        CD.addChallenge()
    elif user_choice == '4':
        CD.addParagraph()
    elif user_choice == '5':
        utilisateur_online = True
    else:
        print("Commande invalide. Veuillez entrer une commande valide!")
