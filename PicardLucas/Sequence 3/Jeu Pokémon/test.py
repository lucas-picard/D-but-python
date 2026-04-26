import random
from attack import Attack


class Pokemon:                                                              # création de la class Pokémon
    def __init__(self, nom, taille, poids, pv, type_, attaque):             #  création de la fonction constructrice
        self.niveau = 1
        self._nom = nom
        self._taille = taille
        self._poids = poids
        self._defense = random.randint(0, 50)
        self._pv = pv
        self._type = type_
        self._attaque = attaque

        # Getters
    def get_niveau(self):
        return self.niveau

    def get_nom(self):
        return self._nom

    def get_taille(self):
        return self._taille

    def get_poids(self):
        return self._poids

    def get_defense(self):
        return self._defense

    def get_pv(self):
        return self._pv

    def get_type(self):
        return self._type

    def get_attaque(self):
        return self._attaque


    # Setters
    def set_niveau(self, niveau):
        self.niveau = niveau

    def set_nom(self, nom):
        self._nom = nom

    def set_taille(self, taille):
        self._taille = taille

    def set_poids(self, poids):
        self._poids = poids

    def set_defense(self, defense):
        self._defense = defense

    def set_pv(self, pv):
        self._pv = pv

    def set_type(self, type_):
        self._type = type_

    def set_attaque(self, attaque):
        self._attaque = attaque


    # Méthode pour afficher les informations du Pokémon
    def infos(self):
        print(f"Niveau: {self.niveau}")
        print(f"Nom: {self._nom}")
        print(f"Taille: {self._taille}")
        print(f"Poids:{self._poids}")
        print(f"Défense: {self._defense}")
        print(f"PV: {self._pv}")
        print(f"Type: {self._type}")
        print(f"Attaque: {self._attaque}")

    # Méthode spéciale appelée lors de la destruction de l'objet
    def __del__(self):
        print(f"")


# Attaque

# Salamèche
flameche = Attack("Flammèche", 45, "Feu")
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
pikashu = Pokemon("Pikashu", 0.4, 6, 60, "Electrique", [eclair, frotte_frimousse, vive_attaque, etincelle])
salameche = Pokemon("Salamèche", 0.6, 8.5, 80, "Feu", [flameche, lance_flamme, draco_soufle, rugissement])
carapuce = Pokemon("Carapuce", 0.5, 9, 80, "Eau", [pistolet_a_O, charge1, tour_rapide, vibraca])
bulbizarre = Pokemon("Bulbizarre", 0.7, 6.9, 80, "Plante", [fouet_lianes, charge, tranch_herbe, canon_graine])


def salameche_attaque():
    print("--- Début du Combat !! ---")
    print("--choisissez une attaque--")
    print("1. flameche (40 dégats)")
    print("2. lance_flamme (50 dégats)")
    print("3. draco_soufle (60 dégats)")
    print("4. rugissement (55 dégats)")
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
    print("--- Début du Combat !! ---")
    print("--choisissez une attaque--")
    print("1. Eclair (40 dégats)")
    print("2. Frotte-Frimousse (50 dégats)")
    print("3. Vive-Attaque (45 dégats)")
    print("4. Étincelle (60 dégats)")
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
    print("--- Début du Combat !! ---")
    print("--choisissez une attaque--")
    print("1. Pistolet à O (40 dégats)")
    print("2. Charge (45 dégats)")
    print("3. Tour Rapide (50 dégats)")
    print("4. Vibraca (60 dégats)")
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
    print("--- Début du Combat !! ---")
    print("--choisissez une attaque--")
    print("1. Fouet Lianes (45 dégats)")
    print("2. Charge (50 dégats)")
    print("3. Tranch’Herbe (55 dégats)")
    print("4. Canon Graine (60 dégats)")
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


def attaque_pokemon(pokemon1, pokemon2):                        # création de la fonction qui définie se qu'il faut faire pour attaquer
    types_faiblesse = {"Eau": ["Eau", "Plante"], "Electrique": ["Plante", "Electrique"], "Feu": ["Eau", "Feu"], "Plante": ["Eau", "Plante"]}        # définie la faiblesse pour chaque types
    types_force = {"Eau": ["Feu"], "Electrique": ["Eau"], "Feu": ["Plante"], "Plante": ["Eau"]}             # définie la force d'un type sur un autres type

    if pokemon2.get_defense() > random.randint(0, 100):         # ont créer les esquive sur les Pokémon d'une manière aléatoire
        print(pokemon2.get_nom(), "a esquivé l'attaque")

    else:                                       # si le Pokémon n'esquive pas il vérifie les forces et les faiblesses des Pokémon
        coefficient_attaque = 1
        # Vérification des faiblesses
        for i in range(len(types_faiblesse[pokemon1.get_attaque().get_type()])):         # boucle qui parcours type_faiblesse du pokemon1
            if types_faiblesse[pokemon1.get_attaque().get_type()][i] == pokemon2.get_type():        # si le pokémon n'a pas de faiblesse contre l'autre pokémon
                coefficient_attaque = 0.5                                       # ont applique un coefficiant d'attaque de 0,5

        # Vérification des forces
        for i in range(len(types_force[pokemon1.get_attaque().get_type()])):                    # boucle qui parcours types_forces du pokemon1
            if types_force[pokemon1.get_attaque().get_type()][i] == pokemon2.get_type():        # si le pokémon1 est un type force contre l'autre, ont ajoute un coefficient d'attaque a 2
                coefficient_attaque = 2

        print(pokemon2.get_nom(), "subit", (coefficient_attaque * pokemon1.get_attaque().get_puissance()), 'dégâts')        # ont affiche se que subit le Pokémon
        pokemon2.set_pv(pokemon2.get_pv() - (coefficient_attaque * pokemon1.get_attaque().get_puissance()))
        if pokemon2.get_pv() < 0:       # si le pokemon2 a moin de 0 pv ont change les pv du pokémon en les mettant a 0
            pokemon2.set_pv(0)


def combat(pokemon1, pokemon2):                     # ont créer la fonction qui permais de combattre
    # affiche le nom et la vie des 2 Pokémon
    print("----------------------------------------------------------------------")
    print("-Chaque pokemon a des faiblaisse celon le pokemon qu'il combat")
    print("-----------------------------------------------------------------------")
    print(pokemon1.get_nom(), ":", pokemon1.get_pv(), "pv")
    print(pokemon2.get_nom(), ":", pokemon2.get_pv(), "pv")
    print("-----------------------------------------------------------------------")
    tour = 0                    # innitialise le tour a 0


    # boucle qui nous permais de continuer le combat tant que les personnages ont des pv > 0
    while pokemon1.get_pv() > 0 and pokemon2.get_pv() > 0:

        if tour % 2 == 0:
            if pokemon1 == pikashu:
                pikashu_attaque()
            elif pokemon1 == salameche:
                salameche_attaque()
            elif pokemon1 == carapuce:
                carapuce_attaque()
            elif pokemon1 == bulbizarre:
                bulbizarre_attaque()

        else:
            attaque_aleatoire = random.randint(0, 3)

            if pokemon2 == pikashu:
                if attaque_aleatoire == 0:
                    pokemon2.set_attaque(eclair)
                elif attaque_aleatoire == 1:
                    pokemon2.set_attaque(frotte_frimousse)
                elif attaque_aleatoire == 2:
                    pokemon2.set_attaque(vive_attaque)
                elif attaque_aleatoire == 3:
                    pokemon2.set_attaque(etincelle)

            elif pokemon2 == salameche:
                if attaque_aleatoire == 0:
                    pokemon2.set_attaque(flameche)
                elif attaque_aleatoire == 1:
                    pokemon2.set_attaque(lance_flamme)
                elif attaque_aleatoire == 2:
                    pokemon2.set_attaque(draco_soufle)
                elif attaque_aleatoire == 3:
                    pokemon2.set_attaque(rugissement)

            elif pokemon2 == carapuce:
                if attaque_aleatoire == 0:
                    pokemon2.set_attaque(pistolet_a_O)
                elif attaque_aleatoire == 1:
                    pokemon2.set_attaque(charge1)
                elif attaque_aleatoire == 2:
                    pokemon2.set_attaque(tour_rapide)
                elif attaque_aleatoire == 3:
                    pokemon2.set_attaque(vibraca)

            elif pokemon2 == bulbizarre:
                if attaque_aleatoire == 0:
                    pokemon2.set_attaque(fouet_lianes)
                elif attaque_aleatoire == 1:
                    pokemon2.set_attaque(charge)
                elif attaque_aleatoire == 2:
                    pokemon2.set_attaque(tranch_herbe)
                elif attaque_aleatoire == 3:
                    pokemon2.set_attaque(canon_graine)

            # si le nombre de tour est impaire, ses au pokémon1 d'attaquer, sinon c'est au pokémon2 d'attaquer
        if tour % 2 == 0:
            print(pokemon1.get_nom(), "attaque", pokemon2.get_nom(), "avec", pokemon1.get_attaque().get_nom())
            attaque_pokemon(pokemon1, pokemon2)
        else:
            print(pokemon2.get_nom(), "attaque", pokemon1.get_nom(), "avec", pokemon2.get_attaque().get_nom())
            attaque_pokemon(pokemon2, pokemon1)

        # affiche le nom et la vie des 2 Pokémon
        print("-----------------------------------------------------------------------")
        print(pokemon1.get_nom(), ":", pokemon1.get_pv(), "pv")
        print(pokemon2.get_nom(), ":", pokemon2.get_pv(), "pv")
        print("-----------------------------------------------------------------------")

        # si le pokémon1 arrive a 0 pv alors ses le pokémon2 qui gagne, sinon si pokémon2 arrive a 0 pv alors ses le pokémon1 qui gagne
        if pokemon1.get_pv() == 0:
            print(pokemon2.get_nom(), "a gagné !!")


        elif pokemon2.get_pv() == 0:
            print(pokemon1.get_nom(), "a gagné !!")

        # ont ajoute 1 tour a la fin de la manche
        tour += 1
        # clique sur entrer pour continuer le combat si il n'est pas terminer
        continu = input("entrez pour continuer: ")

# Lancer le combat



def choix_pokemon():
    print("--choix du Pokémon--")
    print("1. Pikachu")
    print("2. Salameche")
    print("3. Carapuce")
    print("4. Bulbizarre")

    first_choice = int(input("choisissez une premier Pokémon: "))
    second_choice = int(input("choisissez un deuxieme Pokémon: "))


    if first_choice == 1 and second_choice == 2:
        combat(pikashu, salameche)
    elif first_choice == 1 and second_choice == 3:
        combat(pikashu, carapuce)
    elif first_choice == 1 and second_choice == 4:
        combat(pikashu, bulbizarre)

    if first_choice == 2 and second_choice == 1:
        combat(salameche, pikashu)
    elif first_choice == 2 and second_choice == 3:
        combat(salameche, carapuce)
    elif first_choice == 2 and second_choice == 4:
        combat(salameche, bulbizarre)

    if first_choice == 3 and second_choice == 1:
        combat(carapuce, pikashu)
    elif first_choice == 3 and second_choice == 2:
        combat(carapuce, salameche)
    elif first_choice == 3 and second_choice == 4:
        combat(carapuce, bulbizarre)

    if first_choice == 4 and second_choice == 1:
        combat(bulbizarre, pikashu)
    elif first_choice == 4 and second_choice == 2:
        combat(bulbizarre, salameche)
    elif first_choice == 4 and second_choice == 3:
        combat(bulbizarre, carapuce)

choix_pokemon()