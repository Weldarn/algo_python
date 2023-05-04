# Ecrire un algorithme qui demande un nombre de départ, et qui ensuite écrit la table de multiplication de ce nombre

saisie = int(input('Veuillez écrire un chiffre'))

for i in range(1,11):
    multi = saisie * i
    print(f'{saisie} x {i} = {multi}')