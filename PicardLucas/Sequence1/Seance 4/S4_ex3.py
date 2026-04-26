nb_mots = 1
phrase = input("entrer une phrase: ")           # demander a l'utilisateur d'ecrire une phrase
code = ""                                       # defini se qu'est un espace
for i in phrase:
    if i == ' ':
        nb_mots += 1                            # ajouter 1 a chaque espace dans la phrase

print("il y a", nb_mots, "mots dans cette phrase")      # affiche le resultat
