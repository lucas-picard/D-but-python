import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"   #defini tous les caracter possible pour le mot de passe

phrase = input("ecrivez votre phrase: ")        #demande a l'utilisateur d'ecrire une phrase
code = ""

for i in phrase:            # defini se qu'est et se que deviens un espace
    if i == ' ':
        code += '_'
    else:
        code += random.choice(characters)

print("votre mot de passe sera:", code)








