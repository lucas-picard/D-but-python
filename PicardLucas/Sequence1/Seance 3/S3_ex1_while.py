'''
#Question numero 3
first_number = int(input("Enter a first number: "))
second_number = int(input("Enter a second number: "))

total = 0
while first_number <= second_number:
    total += first_number
    first_number += 1
print(total)

'''
#Question numero 4
first_number = 0

second_number = int(input("enter a number: "))
first_number = (second_number * (second_number + 1)) / 2
print("la somme de se nombre est", first_number)