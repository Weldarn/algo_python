#Un magasin de reprographie facture 0,10 E les dix premières photocopies, 
#0,09 E les vingt suivantes et 0,08 E au-delà. 
#Ecrivez un algorithme qui demande à l’utilisateur le nombre de photocopies effectuées et qui affiche la facture correspondante.

saisie = int(input('Veuillez saisir le nombre de photocopies !'))

if saisie <= 10:
    facture = saisie * 0.1

elif saisie <= 30:
    facture = 10 * 0.1 + (saisie - 10) * 0.09

else: facture = 10 * 0.1 + 20 * 0.09 + (saisie - 30) * 0.08

print (f'La facture total est de : {facture}E')