import random
un = 0
deux = 0
trois = 0
quatre = 0
cinq = 0
six = 0

for i in range(1000):
    nb = random.randint(1,7)
    if nb == 1:
        un += 1
    if nb == 2:
        deux += 2
    if nb == 3:
        trois += 3
    if nb == 4:
        quatre += 4
    if nb == 5:
        cinq += 5
    if nb == 6:
        six += 6

un == (un * 100) / 1000
deux == (deux * 100) / 1000
trois == (trois * 100) / 1000
quatre == (quatre * 100) / 1000
cinq == (cinq * 100) / 1000
six == (six * 100) / 1000

print("le pourcentage de 1 est", un, "celui de 2 est", deux, "celui de 3 est", trois, "celui de 4 est", quatre, "celui de 5 est", cinq, "et celui de 6 est", six)





