class Attack:
    def __init__(self, nom, puissance, type_):
        self._nom = nom
        self._puissance = puissance
        self._type = type_

    def get_nom(self):
        return self._nom

    def get_puissance(self):
        return self._puissance

    def get_type(self):
        return self._type


    def set_nom(self, nom):
        self._nom = nom

    def set_puissance(self, puissance):
        self._puissance = puissance

    def set_type(self, type_):
        self._type = type_

    def infos(self):
        print(f"Nom: {self._nom}")
        print(f"Puissance: {self._puissance}")
        print(f"Type: {self._type}")

    def __del__(self):
        print(f"Le Pokémon {self._nom} a attaquer")
