#Exercice 2 : Ecrire un algo demandant 2 nombres à un utilisateur et dis si le produit des deux est positif ou negtif SANS FAIRE LE CALCUL

saisie = int(input('Saisir un nombre'))
saisie2 = int(input('Saisir un nombre'))

#if ((saisie and saisie2 > 0)) or ((saisie and saisie2 < 0)):
#    print ('Le produit est positif')
#else:
#    print ('Le produit est négatif')

#Autre méthode
#print('Positif') if ((saisie and saisie2 > 0)) or ((saisie and saisie2 < 0)) else
#print('Negatif')

#Conditions multiple
if saisie > 0 :
    print('Positif')
elif saisie <0 :
    print('Negatif')
else :
    print('Nul')
