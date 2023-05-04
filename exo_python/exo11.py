#Écrire un algorithme qui permette de connaître ses chances de gagner au tiercé, quarté, quinté et autres impôts volontaires.
#On demande à l’utilisateur le nombre de chevaux partants, et le nombre de chevaux joués. Les deux messages affichés devront être :
#Dans l’ordre : une chance sur X de gagner
#Dans le désordre : une chance sur Y de gagner
#X et Y nous sont donnés par la formule suivante, si n est le nombre de chevaux partants et p le nombre de chevaux joués (le signe ! est la factorielle soit la multiplication de tout les entier de 1 au nombre choisi) :
#X = n ! / (n - p) !
#Y = n ! / (p ! * (n – p) !)
import math

n = int(input(('Ecrivez le nombre de chevaux partants :'))) 
p = int(input(('Ecrivez le nombre de chevaux joués :'))) 

x = math.factorial(n) / math.factorial(n - p)
y = math.factorial(n) / math.factorial(p) * math.factorial(n - p)

print(f"Dans l'ordre : il y a une chance sur {x} de gagner")
print(f"Dans le désordre : il y a une chance sur {y} de gagner")