age = int(input('Veuillez saisir votre age svp !'))
permis = int(input('Veuillez saisir depuis combien temps vous aviez votre permis !'))
accident = int(input('Votre nombre daccidents !'))
fidélité = int(input('Depuis combien de temps êtes vous chez nous?'))

if fidélité >= 5:
    validé = 1

if age < 25 and permis <= 2:
    if accident == 0:
        if validé == 1: 
            tarif = 'orange'
        else : tarif = 'rouge'
    else: print('Dégagez !')
if (age > 25 and permis <= 2) or (age < 25 and permis > 2 ):
    if accident == 0:
        if validé == 1:
            tarif = 'vert'
        else: tarif = 'orange' 
    elif accident == 1:
        if validé == 1:
            tarif = 'orange'
        else: tarif = 'rouge'
    else: print('Dégagez !')
if age > 25 and permis > 2:
    if accident == 0:
        if validé == 1:
            tarif = 'bleu'
        else: tarif = 'vert'
    elif accident == 1:
        if validé == 1:
            tarif = 'vert'
        else: tarif = 'orange'
    elif accident == 2:
        if validé == 1:
            tarif = 'orange'
        else: tarif = 'rouge'
    else: print('Dégagez')


print (f'Vous pouvez bénéficier du tarif {tarif} car vous avez {age}ans , votre permis est vieux de {permis}ans et vous avez {accident} accident(s) !')

    