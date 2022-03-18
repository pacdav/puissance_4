import numpy as np
import random as rdm

def comptage(table):
    total = 0
    point1 = 0
    point2 =0
    #comptage des points en ligne
    for haut in range(4):
        for x in range(4):
            total = total + table[haut, x]
        if total == 4:
            point1 = point1+1
        elif total == 8:
            point2 = point2+1
        total = 0
    #comptage des points en collone
    for large in range(4):
        for y in range(4):
            total = total + table[y, large]
        if total == 4:
            point1 = point1+1
        elif total == 8:
            point2 = point2+1
        total = 0
    #comptage des diagonales
    largeur = 0        
    for x in range(4):
        total = total + table[x, largeur]
        largeur +=1
    if total == 4:
        point1 = point1+1
    elif total == 8:
        point2 = point2+1
    total = 0
    largeur = 0
    longeur = 3
    for y in range(4):
        total = total +table[largeur, longeur]
        longeur -=1
        largeur+=1
    if total == 4:
        point1 = point1+1
    elif total == 8:
        point2 = point2+1
    total = 0

    print("Le joueur 1 a ", point1, "points")
    print("Le joueur 2 a ", point2, "points")

def passage(tour, j1, j2, table):
    coup = int(input("Dans quel colonne voulait vous jouez ? "))
    while coup > 4 or coup <=0 :
        print("Ce coup n'est pas possible. Rejouez s'il vous plait")
        coup = int(input("Dans quel colonne voulait vous jouez ? "))
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
                else:
                    table[y, coup-1]= 2
                print(table)
                
        else:
            print("Ce ne peux pas être joué. Veuillez choisir une autre colonne")
            possible = True
            passage(tour,j1, j2, table)

y=3
print("Ce jeux est le jeu du puissance 4. Les regles sont simples: aligné 4 pions de même couleur à la suite")
print("Le plateu de jeu commence vide")
table =np.zeros((4,4))
print(table)
print("Quels sont les noms des deux joueurs : ")
j1 ="a"
j2 = "a"
while j1 == j2:
    j1 = input("Le joueurs 1 s'appelle: ") #1 dans le tableau
    j2 = input("Et le joueurs 2 s'appelle: ") #2 dans le tabelau
    if j1 == j2:
        print("Les noms sont les mêmes veuillez recommencer")
print(j1, ", tu seras noté 1 dans le tableau")
print(j2, ", tu seras noté 2 dans le tableau")
tour = rdm.choice([j1, j2])
print("Suite au tirage au sort, c'est",tour, "qui va commencer à jouer")
for x in range(16):
    passage(tour, j1, j2, table)
    if tour == j1:
        tour = j2
        print("C'est à", j2, "de jouer")
    else :
        tour = j1
        print("C'est à", j1, "de jouer")
comptage(table)
print("fin du jeu")