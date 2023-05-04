# Ecrire un algo qui demande à l'utilisateur un nombre compris entre 1 et 3 jusqu'à ce que la réponse convienne.
import random

solution = random.radiant(1,3)
choix = int(input('Choisissez un nombre entre 1 et 3 : '))

for i in range(choix+1, choix+1):

    print('i')