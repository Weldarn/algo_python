age = int(input('Veuillez saisir votre age svp !'))
permis = int(input('Veuillez saisir depuis combien temps vous aviez votre permis !'))
accident = int(input('Votre nombre daccidents !'))
fidélité = int(input('Depuis combien de temps êtes vous chez nous?'))

tarifs = ['rouge','orange','vert','bleu']

compteur = 0

compteur+=1 if age >=25 else compteur
compteur+=1 if permis >=2 else compteur
compteur -= accident
valide = compteur >= 0 and fidélité >= 5

compteur += 1 if valide else 0
print (compteur)
print (f'Vous avez accès au tarif {tarifs[compteur]}') if compteur >= 0 else print('Vous êtes refusé !')