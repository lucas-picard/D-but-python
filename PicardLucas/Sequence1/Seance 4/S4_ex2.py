nb_v = 0
chaine = input("entrer un mot: ")
voyelle = ["a", "e", "i", "o", "u", "y"]           #determine se qu'est une voyelle
for i in range(len(chaine)):
    if chaine[i] in voyelle :           #regarde si il y a une voyelle de la variable dans la phrase
        nb_v += 1
if nb_v == 0:           #affiche si oui ou non il y a une ou plusieurs voyelle
    print("il n'y a aucune voyelle dans le mot", chaine)
else:
    print("il y a", nb_v, "voyelle dans le mot", chaine)

