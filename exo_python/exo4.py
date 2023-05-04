heures = int(input('Saisie les heures'))
minutes = int(input('Saisie les minutes'))
secondes = int(input('Saisie les secondes'))


if secondes == 60:
    secondes = 0
    minutes += 1
else: secondes +=1


if minutes == 60:
    minutes = 0
    heures += 1
        
if heures == 24:
    heures = 0


print(f"Dans une seconde, il sera {heures} heure(s), {minutes} minute(s) et {secondes} seconde(s).")
