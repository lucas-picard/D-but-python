import random
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-[]*~_#?!@"
password = ""
for i in range(12):
    password += random.choice(characters)
print(password)



