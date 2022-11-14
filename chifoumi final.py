#DEBUT

#On importe la librarie random pour pouvoir utiliser l'aléatoire dans le programme
import random

# On demande si le joueur veut bien jouer au jeu avec un input (réponse: y/n)
choice=input("Hello user!\nWould you like to play with me? (y/n) ")

# Si il a répondu non ('n')
if choice=="n":
    # On arrête le programme
    exit()

#On défini le score comme une table de 2 zéros
score = [0, 0]

#On défini les trois mouvements dans une table mouv
mouv = ["rock", "paper", "cissor"]

# On défini un bool canStart qui défini si le jeu pourra démarer sans problème
canStart = True

# On demande au joueur avec un input si il veut jouer avec le puit et la dynamite
choice = input("Would you like to implement the well and the bomb? (y/n) ")
# Si il a répondu non ('n')
if choice=="n":
    #La valeur well est défini sur False
    well = False
# Sinon
else:
    #La valeur well est défini sur False
    well = True
    #On ajoute les mouvements du puit et de la dynamite à la table des mouvements avec la méthode append()
    mouv.append("well")
    mouv.append("bomb")


#Démarre la boucle inifinie avec while True
while True:
    # Défini une string attribué à wellText qui contient soit ", 4-well, 5-bomb" si la variable well est vrai ou aucun texte si elle est false, tout ça dans une condition en une ligne car ça fait gagner de la place :D
    wellText = well and ", 4-well, 5-bomb" or ""
    
    #Demande au joueur de faire son choix entre 1-papier, 2-pierre ou 3-cisseaux et concatene le contenu de wellText pour ajouter les indications pour le puit et la bombe si ce mode est activé. La valeur retourné par le input est attribué à playerChoice
    playerchoice = input("\nChoose your move, user!\n(1-rock, 2-paper, 3-cissor"+wellText+")\n")
    
    #Utiliser random.randint(1, well and 5 or 3) pour faire en sorte que l'ordi choisisse un mouvement entre 1 et 3 si well est False ou 1 et 5 si well est True qui sera attribué à la variable aiChoice. Aussi en une ligne car c'est pratique
    aiChoice = random.randint(1, well and 5 or 3)


    # Si playerChoice est "rock"
    if playerchoice=="rock":
        # Changer playerChoice pour 1
        playerchoice = 1
    # Sinon si playerChoice est "paper"
    elif playerchoice=="paper":
        # Changer playerChoice pour 2
        playerchoice = 2
    # Sinon si playerChoice est "cissor"
    elif playerchoice=="cissor":
        # Changer playerChoice pour 3
        playerchoice = 3
    # Sinon si well est True et playerChoice est "well"
    elif well and playerchoice=="well":
        # Changer playerChoice pour 4
        playerchoice = 4
    # Sinon si well est True et playerChoice est "bomb"
    elif well and playerchoice=="bomb":
        # Changer playerChoice pour 5
        playerchoice = 5
    # Sinon
    else:
        # On essaye de changer playerChoice en integer
        try:
            playerchoice = int(playerchoice)
            #Si playerChoice est plus grand que la taille de la table de mouvements
            if playerchoice>len(mouv):
                # On change la variable canStart à False
                canStart = False
                # On affiche un message d'erreur sans arrêter le jeu
                print("ERROR: The choice made by the user is not valid.\n\n")
        # Dans le cas où ça marche pas:
        except:
            # la variable canStart devient alors False
            canStart = False
            # Et on affiche un message d'erreur sans arrêter le programme
            print("ERROR: The choice made by the user is not valid.\n\n")

    # Si canStart est vrai
    if canStart:

        #On affiche le choix du joueur et celui de l'ordi
        print("USER: " + mouv[playerchoice-1] + "\nORDI: " + mouv[aiChoice-1] + "\n")

        #Si playchoice et aiChoice sont les mêmes valeurs
        if playerchoice==aiChoice:
            # On affiche un message pour annoncer que c'est une équalité!
            print("Oh, it's a tie!")
        #Sinon si le joueur a choisi papier et l'ordi pierre ou puit si il est présent
        #Ou le joueur a choisi pierre et l'ordi cisseau ou bombe si elle est présente
        #Ou le joueur a choisi cisseau et l'ordi papier ou bombe si elle est présente
        #Ou si well est True, le joueur a choisi bombe et l'ordi papier ou le puit
        #Ou si well est True, le joueur a choisi puit et l'ordi pierre ou cisseaux
        elif (mouv[playerchoice-1]=="paper" and (mouv[aiChoice-1]=="rock" or (well and mouv[aiChoice-1]=="well"))) or (mouv[playerchoice-1]=="rock" and (mouv[aiChoice-1]=="cissor"or (well and mouv[aiChoice-1]=="bomb"))) or (mouv[playerchoice-1]=="cissor" and (mouv[aiChoice-1]=="paper" or (well and mouv[aiChoice-1]=="bomb"))) or well and ((mouv[playerchoice-1]=="bomb" and (mouv[aiChoice-1]=="paper" or mouv[aiChoice-1]=="well"))) or well and ((mouv[playerchoice-1]=="well" and (mouv[aiChoice-1]=="rock" or mouv[aiChoice-1]=="cissor"))):
            #On incrémente le score du joueur de 1
            score[0]=score[0]+1
            # On affiche un message pour annoncer que l'ordi a perdu
            print("Aw... I lost..")
        #Sinon
        else:
            #On incrémente le score de l'ordi de 1
            score[1]=score[1]+1
            # On affiche un message pour annoncer que l'ordi a gagné
            print("Hey! I won, yay!")

        # On marque un temps de pause avec un input mentionnant que l'utilisateur peut presser Entrée pour continuer
        input("(Press Enter key to continue)")

        # On demande si le joueur veut rejouer via un input()
        choice = input("Hey hey! Wanna play again? (y/n) ")
        # Si il a répondu non ('n')
        if choice=="n":
            # On sort de la boucle
            break
    # canStart est remis à true pour la prochaine intération de la boucle
    canStart = True

#On affiche un message d'au revoir qui est complétement inutile mais j'ai envie de donner de la personnalité à l'ordi. Yep.
print("Aww, alright. See you later!")
#On affiche les scores finaux en concatenant les valeurs de la table score
print(f"\n\nFINAL SCORE:\n\nUSER: {score[0]}\nORDI: {score[1]}")
#Si le score du joueur est supérieur à celui de l'ordi
if score[0]>score[1]:
    #On annonce que le joueur a gagné
    print("The user won.")
#Sinon si le score du joueur est inférieur à celui de l'ordi
elif score[0]<score[1]:
    #On annonce que l'ordi a gagné
    print("The ORDI won.")
#Sinon, c'est que le score du joueur et de l'ordi sont égaux
else:
    #On annonce l'égalité
    print("It's a tie.")

#END
