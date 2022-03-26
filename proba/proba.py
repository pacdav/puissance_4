import numpy as np
import random as rdm
total_win = 0
total_game = 0
total_eg =0
def comptage(table, first_tour, j1, j2):
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
    if point1<point2:
        #print("winner 2")
        winner = j2
    elif point1 > point2:
        #print("winner 1")
        winner = j1
    else :
        #print("no winner")
        winner = "no"
        return("=")
    if winner == first_tour:
        return("1st win")
    else:
        return("1st lose")
        


def passage(tour, j1, j2, table):
    coup = rdm.choice([1,2,3,4])
    y=3
    possible = False
    while possible != True:
        if y>=0 :
            if table[y, coup-1] != 0:
                y=y-1  
            else:
                possible = True
                if tour == j1: 
                    table[y, coup-1]= 1
                else:
                    table[y, coup-1]= 2
                
        else:
            possible = True
            passage(tour,j1, j2, table)

for jeu in range(1000000):
    y=3
    table =np.zeros((4,4))
    j1 ="a"
    j2 = "b"
    first_tour = rdm.choice([j1, j2])
    tour = first_tour
    for x in range(16):
        passage(tour, j1, j2, table)
        if tour == j1:
            tour = j2
        else :
            tour = j1
    goal = comptage(table, first_tour, j1, j2)
    if goal == "1st win" :
        total_win +=1
    elif goal == "=":
        total_eg +=1
    total_game +=1
    print(jeu/10000,"%")
print("1st_win :",total_win/10000,"%")
print("egalité: ",total_eg/10000, "%")
print("lose",(total_game-(total_eg+total_win))/10000, "%")
print("total", total_game)