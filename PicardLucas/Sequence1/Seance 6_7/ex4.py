from math import pi

def menu():
    print("quelle forme voulez vous: ")
    print("1. Carré")
    print("2. Rectangle")
    print("3. Cercle")
    print("4. Triangle")

print(menu())
choix = input("quel forme voulez vous (1-4): ")

def cercle():
    rayon = int(input("quel est le rayon: "))
    perimetre = 2 * pi * rayon
    aire = pi * rayon**2
    print("le perimetre est", perimetre, "cm et l'aire est de", aire, "cm²")



def carre():
    cote = int(input("quel taille fais le coté: "))
    perimetre1 = cote * 4
    aire2 = cote * cote
    print("le perimetre est", perimetre1, "cm et l'aire est de", aire2, "cm²")



def rectangle():
    longeur = int(input("de quel longeur est le rectangle: "))
    largeur = int(input("de quel largeur est le rectangle: "))
    aire3 = longeur * largeur
    perimetre3 = (longeur + largeur) * 2
    print("le perimetre est", perimetre3, "cm et l'aire est de", aire3, "cm²")


def triangle():
    first_cote = int(input("quel est la taille du premier cote "))
    second_cote = int(input("quel est la taille du deuxieme cote "))
    three_cote = int(input("quel est la taille du troixieme cote "))
    base = float(input("Entrez la base du triangle : "))
    hauteur = float(input("Entrez la hauteur du triangle : "))
    perimetre4 = first_cote + second_cote + three_cote
    aire4 = (base * hauteur) / 2
    print("le perimetre est", perimetre4, "cm et l'aire est de", aire4, "cm²")





if choix == 1:
    carre()

if choix == 2:
    rectangle()

if choix == 3:
    cercle()

else:
    triangle()




