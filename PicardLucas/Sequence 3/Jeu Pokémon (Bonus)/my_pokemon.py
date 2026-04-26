# Attaque

# Salamèche
flameche = Attack("Flammèche", 40, "Feu")
lance_flamme = Attack("Lance-Flamme", 50, "Feu")
draco_soufle = Attack("Draco-Soufle", 60, "Feu")
rugissement = Attack("Rugissement", 55, "Feu")

# Pikashu
eclair = Attack("Eclair", 40, "Electrique")
frotte_frimousse = Attack("Frotte-Frimousse", 50, "Electrique")
vive_attaque = Attack("Vive-Attaque", 45, "Electrique")
etincelle = Attack("Étincelle", 60, "Electrique")

# Carapuce
pistolet_a_O = Attack("Pistolet à O", 40, "Eau")
charge1 = Attack("Charge", 45, "Eau")
tour_rapide = Attack("Tour Rapide", 50, "Eau")
vibraca = Attack("Vibraca", 60, "Eau")

# Bulbizarre
fouet_lianes = Attack("Fouet Lianes", 45, "Plante")
charge = Attack("Charge", 45, "Plante")
tranch_herbe = Attack("Tranch’Herbe", 55, "Plante")
canon_graine = Attack("Canon Graine", 60, "Plante")

# Pokémon
pikashu = Pokemon("Pikashu", 0.4, 6, 60, "Electrique", eclair)
salameche = Pokemon("Salamèche", 0.6, 8.5, 80, "Feu", flameche)
carapuce = Pokemon("Carapuce", 0.5, 9, 80, "Eau", pistolet_a_O)
bulbizarre = Pokemon("Bulbizarre", 0.7, 6.9, 80, "Plante", fouet_lianes)


def salameche_attaque():
    print("--choisissez une attaque--")
    print("1. flameche")
    print("2. lance_flamme")
    print("3. draco_soufle")
    print("4. rugissement ")
    choix = int(input("choisissez: "))
    print("----------------------------------------------------------------------")

    if choix == 1:
        salameche.set_attaque(flameche)
    elif choix == 2:
        salameche.set_attaque(lance_flamme)
    elif choix == 3:
        salameche.set_attaque(draco_soufle)
    elif choix == 4:
        salameche.set_attaque(rugissement)
    else:
        print("Choix incorrect")


def pikashu_attaque():
    print("--choisissez une attaque--")
    print("1. Eclair")
    print("2. Frotte-Frimousse")
    print("3. Vive-Attaque")
    print("4. Étincelle ")
    choix = int(input("choisissez: "))
    print("----------------------------------------------------------------------")

    if choix == 1:
        pikashu.set_attaque(eclair)
    elif choix == 2:
        pikashu.set_attaque(frotte_frimousse)
    elif choix == 3:
        pikashu.set_attaque(vive_attaque)
    elif choix == 4:
        pikashu.set_attaque(etincelle)
    else:
        print("Choix incorrect")


def carapuce_attaque():
    print("--choisissez une attaque--")
    print("1. Pistolet à O")
    print("2. Charge")
    print("3. Tour Rapide")
    print("4. Vibraca ")
    choix = int(input("choisissez: "))
    print("----------------------------------------------------------------------")

    if choix == 1:
        carapuce.set_attaque(pistolet_a_O)
    elif choix == 2:
        carapuce.set_attaque(charge1)
    elif choix == 3:
        carapuce.set_attaque(tour_rapide)
    elif choix == 4:
        carapuce.set_attaque(vibraca)
    else:
        print("Choix incorrect")

def bulbizarre_attaque():
    print("--choisissez une attaque--")
    print("1. Fouet Lianes")
    print("2. Charge")
    print("3. Tranch’Herbe")
    print("4. Canon Graine ")
    choix = int(input("choisissez: "))
    print("----------------------------------------------------------------------")

    if choix == 1:
        bulbizarre.set_attaque(fouet_lianes)
    elif choix == 2:
        bulbizarre.set_attaque(charge)
    elif choix == 3:
        bulbizarre.set_attaque(tranch_herbe)
    elif choix == 4:
        bulbizarre.set_attaque(canon_graine)

