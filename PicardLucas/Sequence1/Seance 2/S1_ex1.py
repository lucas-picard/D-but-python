while (True):
    first_number = float(input("entré un premier nombre: "))
    second_number = float(input("entré un deuxieme nombre: "))
    operator = str(input("entré un opperateur: "))


    if operator == "+":
        print(first_number + second_number)
    elif operator == "-":
        print(first_number - second_number)
    elif operator == "*":
        print(first_number * second_number)
    elif operator == "/":
        print(first_number / second_number)
    elif operator == "**":
        print(first_number ** second_number)
    elif operator == "%":
        print(first_number % second_number)
    elif operator == "//":
        print(first_number // second_number)