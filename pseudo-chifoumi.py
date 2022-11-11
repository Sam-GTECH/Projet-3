#DEBUT

#On importe la librarie random pour pouvoir utiliser l'aléatoire dans le programme

# On demande si le joueur veut bien jouer au jeu avec un input (réponse: y/n)

# Si il a répondu non ('n')
    # On arrête le programme

#On défini le score comme une table de 2 zéros

#On défini les trois mouvements dans une table mouv

# On défini un bool canStart qui défini si le jeu pourra démarer sans problème

# On demande au joueur avec un input si il veut jouer avec le puit et la dynamite
# Si il a répondu non ('n')
    #La valeur well est défini sur False
# Sinon
    #La valeur well est défini sur False
    #On ajoute les mouvements du puit et de la dynamite à la table des mouvements avec la méthode append()


#Démarre la boucle inifinie avec while True
    # Défini une string attribué à wellText qui contient soit ", 4-well, 5-bomb" si la variable well est vrai ou aucun texte si elle est false, tout ça dans une condition en une ligne car ça fait gagner de la place :D
    
    #Demande au joueur de faire son choix entre 1-papier, 2-pierre ou 3-cisseaux et concatene le contenu de wellText pour ajouter les indications pour le puit et la bombe si ce mode est activé. La valeur retourné par le input est attribué à playerChoice
    
    #Utiliser random.randint(1, well and 5 or 3) pour faire en sorte que l'ordi choisisse un mouvement entre 1 et 3 si well est False ou 1 et 5 si well est True qui sera attribué à la variable aiChoice. Aussi en une ligne car c'est pratique


    # Si playerChoice est "paper"
        # Changer playerChoice pour 1
    # Sinon si playerChoice est "rock"
        # Changer playerChoice pour 2
    # Sinon si playerChoice est "cissor"
        # Changer playerChoice pour 3
    # Sinon si well est True et playerChoice est "well"
        # Changer playerChoice pour 4
    # Sinon si well est True et playerChoice est "bomb"
        # Changer playerChoice pour 5
    # Sinon
        # On essaye de changer playerChoice en integer
            #Si playerChoice est plus grand que la taille de la table de mouvements
                # On change la variable canStart à False
                # On affiche un message d'erreur sans arrêter le jeu
        # Dans le cas où ça marche pas:
            # la variable canStart devient alors False
            # Et on affiche un message d'erreur sans arrêter le programme

    # Si canStart est vrai

        #On affiche le choix du joueur et celui de l'ordi

        #Si playchoice et aiChoice sont les mêmes valeurs
            # On affiche un message pour annoncer que c'est une équalité!
        #Sinon si le joueur a choisi papier et l'ordi pierre ou puit si il est présent
        #Ou le joueur a choisi pierre et l'ordi cisseau ou bombe si elle est présente
        #Ou le joueur a choisi cisseau et l'ordi papier ou bombe si elle est présente
        #Ou si well est True, le joueur a choisi bombe et l'ordi papier ou le puit
        #Ou si well est True, le joueur a choisi puit et l'ordi pierre ou cisseaux
            #On incrémente le score du joueur de 1
            # On affiche un message pour annoncer que l'ordi a perdu
        #Sinon
            #On incrémente le score de l'ordi de 1
            # On affiche un message pour annoncer que l'ordi a gagné

        # On marque un temps de pause avec un input mentionnant que l'utilisateur peut presser Entrée pour continuer

        # On demande si le joueur veut rejouer via un input()
        # Si il a répondu non ('n')
            # On sort de la boucle
    # canStart est remis à true pour la prochaine intération de la boucle

#On affiche un message d'au revoir qui est complétement inutile mais j'ai envie de donner de la personnalité à l'ordi. Yep.

#On affiche les scores finaux en concatenant les valeurs de la table score

#Si le score du joueur est supérieur à celui de l'ordi
    #On annonce que le joueur a gagné
#Sinon si le score du joueur est inférieur à celui de l'ordi
    #On annonce que l'ordi a gagné
#Sinon, c'est que le score du joueur et de l'ordi sont égaux
    #On annonce l'égalité

#END
