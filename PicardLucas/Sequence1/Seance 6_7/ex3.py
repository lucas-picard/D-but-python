listeProbabilite = [0]*13   # dire qu'il est impossible d'obtenir 13 ou plus
listePourcentage = [0]*13

# ont va jusqu'a 7 car ses de 1 a 7 exclu
for De1 in range(1, 7):         # ont lance le premier dés
    for De2 in range(1, 7):         # ont lance le deuxieme dés
        listeProbabilite[De1 + De2] += 1

nbDepossibilite = sum(listeProbabilite)    # ont additionne le resultat des 2 dés

for i in range(len(listeProbabilite)):
    listePourcentage[i] = listeProbabilite[i]*100/nbDepossibilite       # ont calcul le pourcentage de chance d'obtenir le nombre obtenue
# pourcentage pour chaque élément de la liste
    print("la probabilité d'obtenir", i, "est de", round(listePourcentage[i], 2), "%, (", listeProbabilite[i], "apparition(s))")        # ont arondie le resultat au plus proche avec la fonction round



# se code sers a lancer 2 dés egal et connaitre la probabilité d'obtenir des nombres (1, 2, 3, etc...)
















