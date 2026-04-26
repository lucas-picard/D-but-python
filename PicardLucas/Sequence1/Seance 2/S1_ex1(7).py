formule = input("entrez votre calcul :")
if "+" in formule:
    premier_nombre = int(formule.split("+")[0])
    deuxieme_nombre = int(formule.split("+")[1])
    print(premier_nombre, "+", deuxieme_nombre, "est", premier_nombre + deuxieme_nombre)
if "-" in formule:
    premier_nombre = int(formule.split("-")[0])
    deuxieme_nombre = int(formule.split("-")[1])
    print(premier_nombre, "-", deuxieme_nombre, "est", premier_nombre - deuxieme_nombre)
if "*" in formule:
    premier_nombre = int(formule.split("*")[0])
    deuxieme_nombre = int(formule.split("*")[1])
    print(premier_nombre, "*", deuxieme_nombre, "est", premier_nombre * deuxieme_nombre)
if "/" in formule:
    premier_nombre = int(formule.split("/")[0])
    deuxieme_nombre = int(formule.split("/")[1])
    print(premier_nombre, "/", deuxieme_nombre, "est", premier_nombre / deuxieme_nombre)
if "//" in formule:
    premier_nombre = int(formule.split("//")[0])
    deuxieme_nombre = int(formule.split("//")[1])
    print(premier_nombre, "//", deuxieme_nombre, "est", premier_nombre // deuxieme_nombre)
if "**" in formule:
    premier_nombre = int(formule.split("**")[0])
    deuxieme_nombre = int(formule.split("**")[1])
    print(premier_nombre, "**", deuxieme_nombre, "est", premier_nombre ** deuxieme_nombre)
if "%" in formule:
    premier_nombre = int(formule.split("%")[0])
    deuxieme_nombre = int(formule.split("%")[1])
    print(premier_nombre, "%", deuxieme_nombre, "est", premier_nombre % deuxieme_nombre)
