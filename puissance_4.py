import numpy as np
import random as rdm

def passage(tour):
    print(tour)
    coup = int(input("Dans quel colonne voulait vous jouez ? "))
    if coup > 4 or coup <=0 :
        print("Ce coup n'est pas possible. Rejouez s'il vous plait")
        passage(tour)
    else:
        y=3
        possible = False
        while possible != True:
            if y>=0 :
                if table[y, coup-1] != 0:
                    y=y-1  
                else:
                    print("coup possible", y)
                    possible = True
                    if tour == j1: 
                        table[y, coup-1]= 1
                        tour = j2
                    elif tour == j2:
                        table[y, coup-1]= 2
                        tour = j1
                    print(table)
                    print(tour)
                    return(tour)
                    
            else:
                print("Ce ne peux pas être joué. Veuillez choisir une autre colonne")
                passage(tour)

table =np.zeros((4,4))
y=3
print("Ce jeux est le jeu du puissance 4. Les regles sont simples: aligné 4 pions de même couleurs à la suite")
print("Le plateu de jeu commence vide")
table =np.zeros((4,4))
print(table)
print("Quels sont les noms des deux joueurs : ")
j1 = input("Le joueurs 1 s'appelle: ") #1 dans le tableau
j2 = input("Et le joueurs 2 s'appelle: ") #2 dans le tabelau
print(j1, ", tu seras noter X dans le tabelau")
print(j2, ", tu seras noter O dans le tabelau")
tour = rdm.choice([j1, j2])
print("Suite au tirage au sort, c'est",tour, "qui va commencer à jouer")
for x in range(16):
    tour = passage(tour)
print("fin du jeu")