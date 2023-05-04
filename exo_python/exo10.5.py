#Réécrire l’algorithme précédent, mais cette fois-ci on ne connaît pas d’avance combien l’utilisateur souhaite saisir de nombres. La saisie des nombres s’arrête lorsque l’utilisateur entre un zéro.

maximum = 0
nombre = None

while nombre != 0:
    nombre = float(input("Entrez un nombre (0 pour stop) : "))
    
    if nombre > maximum:
        maximum = nombre 

if maximum != 0:
    print("Le plus grand des nombres est : ", maximum)
else:
    print("J'ai rien !")