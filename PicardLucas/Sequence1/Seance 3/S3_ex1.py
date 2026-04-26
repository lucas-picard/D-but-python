def compter_mots(phrase):
    mots = phrase.split()
    return len(mots)

print("Nombre de mots:", compter_mots(input("Entrez une phrase : ")))

