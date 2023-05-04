saisie = int(input('Saisie de votre âge'))

if saisie <= 5:
    print ('Sort !')

elif saisie == 6 or saisie == 7:
    print ('Vous êtes un Poussin !')

elif saisie == 8 or saisie == 9:
    print ('Vous êtes un Pupille !')

elif saisie == 10 or saisie == 11:
    print ('Vous êtes un Minimoys')

elif saisie >= 12:
    print ('Vous êtes un Cadet')

else: print ('Bizarre ça')