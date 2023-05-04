# Ecrire un algorithme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite quel était le plus grand parmi ces 20 nombres
maximum = 0
for i in range(20):
    nombre = int(input('Veuillez SAISIR les 20 chiffres !'))

    if nombre > maximum:
        maximum = nombre

print(f'Le nombre le plus grand est {maximum} !')
