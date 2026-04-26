'''#Ex 2 avec for
N = int(input("enter a number: "))
for i in range(2, N):
    if N % i == 0:
        print(N, " n'est pas un nombre premier car ", i)
'''

#Ex 2 avec for
premier = True
N = int(input("enter a number: "))
for i in range(2, N):
    if N % i == 0:
        premier = False
        print(N, " n'est pas un nombre premier car il est divisible par ", i)
if premier == True :
    print(N, "est un nombre premier car il est que divisible par 1 et lui meme ")








