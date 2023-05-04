# Ecrire un algorithme qui demande un nombre de départ, et qui calcule la somme des entiers jusqu’à ce nombre.

saisie = int(input("Entrez un nombre : "))

somme = 0

for i in range(1, saisie+1):
    somme += i

print("La somme des entiers jusqu'à", saisie, "est", somme)