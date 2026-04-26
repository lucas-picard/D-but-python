number = 0
phrase = input("entrer un mot: ")       #defini se qu'est la lettre e et demande a l'utilisateur d'ecrire un mot(phrase)
lettre = "e"
for i in range(len(phrase)):
    if phrase[i] in lettre:         #si il y a un e dans la phrase ou mots ont ajoute 1 au compteur
        number += 1
if number == 0:
    print("il n'y a pas de E dans cette phrase")        #si il y a 0 au compteur ont affiche qu'il n'y a pas de e dans la phrase
else:
    print("il y a", number, "dans cette phrase")        #sinon ont affiche le nombre de e dans la phrase







