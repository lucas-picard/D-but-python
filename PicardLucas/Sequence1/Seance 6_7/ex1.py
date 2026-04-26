alfa = "abcdefghijklmnopqrstuvwxyz"
sortie = ""
entree= input("entrez une phrase: ")
deca = int(input("entrez un chiffre: "))
for i in range (len(entree)):
    if entree[i] in alfa:
        for j in range (len(alfa)):
            if entree[i] == alfa[j]:
                sortie += alfa[(j + deca) % 26]
    else:
        sortie += entree[i]
print(sortie)





































