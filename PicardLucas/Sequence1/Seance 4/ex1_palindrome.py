
chaine = input("écriver un mot : ") #demande a l'utilisateur d'entrer un mot et le programme par du principe que sans est un
palindrome = True
for i in range(len(chaine)):
   if chaine[i] != chaine[-i-1]:        #compare les lettres de debut et fin de phrase
       palindrome = False
       break
if palindrome:          #si palindrome est vrai alors c'est un palindrome
   print(chaine, "est un palindrome")

else:
   print(chaine, "n'est pas un palindrome")










