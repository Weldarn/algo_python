def afficher_carre():
    taille = int(input("Entrez la taille du carré : "))
    
    for i in range(taille):
        for j in range(taille):
            if j == 0 or j == taille-1 or i == 0 or i == taille-1:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()


afficher_carre()
