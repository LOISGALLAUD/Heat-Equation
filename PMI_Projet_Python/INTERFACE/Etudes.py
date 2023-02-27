# -*- coding: utf-8 -*-

"""
Etudes.py

Recense les différentes études que l'on propose 
dans le cadre de notre PMI
"""

#----------------------------------------------------------------#

import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from INTERFACE.Graph3D import *
from DONNEES.CalculEcarts import *
from SOLVEUR.AlgorithmesResol import *
from MATRICES.ProfilSource import *
from SOLVEUR.CalculConvergence import *
from DONNEES.EcartOpti import *

#---------------------Choix utilisateur--------------------------#

TAILLE = 50 #taille de la matrice de la simulation dx = 1/(TAILLE - 1) en mètre (correspond à TailleMax pour EQM Spatial)
dt = 10    #pas de temps en seconde
Nt = 10**3  #nombre de répétition temporelle si cas temporel
Pas = 10**1 #pas des graphiques et de l'animation. Entier <= à Nt
PasS = 1  #pas spatiale pour les études d'EQM
F = f5      #fonction génératrice utilisée dans l'étude
Acc = 0.01
a,b,c,d,g,h,k,l = 40,20,-20,40,20,10,30,8 # Coefficient des fonctions étudiées

#----------------Definitions Utiles à l'affichage----------------#

def data(i,L,dessin, ax, x, y):
    n = len(L) #taille
    z = L[i%n] #matrice suivante (l'indice ne peut dépasser la taille de la liste et pour boucler on utilise une division entière.)
    ax.clear() #on vide les graphs
    dessin = ax.plot_surface(x,y,z,cmap=cm.inferno)
    return dessin

#----------------------------------------------------------------#

def ETUDE1():
    print("Etude 1")
    SOURCE1 = MatriceTh(F, TAILLE, a, b, c, d, g, h, k, l)
    #Graphe3D(SOURCE1.matrice)
    SOURCE = SOURCE1.MatriceSource()
    begin = time.time()
    L = ResolStatio(SOURCE) #nouvelle fonction qui fait une liste de matrices au cours du temps.
    end = time.time()
    print(len(L))
    print("EOF, time elapsed during calculus: "+ str(round(end-begin,2)))
    Graphe3D(L)
    
def ETUDE2():
    print("Etude 2")
    SOURCE1 = MatriceTh(F, TAILLE, a, b, c, d, g, h, k, l)
    #Graphe3D(SOURCE1.matrice)
    SOURCE = SOURCE1.MatriceSource()
    begin = time.time()
    L = ResolExplicite(SOURCE, dt, Nt) #nouvelle fonction qui fait une liste de matrices au cours du temps.
    end = time.time()
    print("EOF, time elapsed during calculus: "+ str(round(end-begin,2)))
    Graphe3D(L)
    
def ETUDE3():
    print("Etude 3")
    SOURCE1 = MatriceTh(F, TAILLE, a, b, c, d, g, h, k, l)
    #Graphe3D(SOURCE1.matrice)
    SOURCE = SOURCE1.MatriceSource()
    begin = time.time()
    L = ResolExpliciteL(SOURCE, dt, Nt, pas=Pas) #nouvelle fonction qui fait une liste de matrices au cours du temps.
    end = time.time()
    print("EOF, time elapsed during calculus: "+ str(round(end-begin,2)))
    print(len(L))
    x, y = MatCoord(TAILLE) #matrices coordonées pour le plot_surface
    fig = plt.figure(2) #création de la figure
    ay = fig.add_subplot(121, projection='3d') #pour comparer à la matrice à avoir
    init = ay.plot_surface(x,y,SOURCE1.matrice,cmap=cm.inferno)
    ax = fig.add_subplot(122, projection='3d') #ajout du subplot 3D
    z = L[0] #initialisation de l'animation
    dessin = ax.plot_surface(x,y,z,cmap=cm.inferno) #bis
    ani = animation.FuncAnimation(fig, data, fargs=(L, dessin, ax, x, y), interval=30,blit=False) #création de l'animation avec la fonction data qui selectionne la matrice dans la liste
    plt.show()
    
def ETUDE4():
    print("Etude 4")
    SOURCE1 = MatriceTh(F, TAILLE, a, b, c, d, g, h, k, l)
    #Graphe3D(SOURCE1.matrice)
    SOURCE = SOURCE1.MatriceSource()
    begin = time.time()
    L = ResolImplicite(SOURCE, dt, Nt) #nouvelle fonction qui fait une liste de matrices au cours du temps. (Val. fonc.: SOURCE, 0.9, 10**5)
    end = time.time()
    print("EOF, time elapsed during calculus: "+ str(round(end-begin,2)))
    Graphe3D(L)
    
def ETUDE5():
    print("Etude 5")
    SOURCE1 = MatriceTh(F, TAILLE, a, b, c, d, g, h, k, l)
    #Graphe3D(SOURCE1.matrice)
    SOURCE = SOURCE1.MatriceSource()
    begin = time.time()
    L = ResolImpliciteL(SOURCE, dt, Nt, pas = Pas) #nouvelle fonction qui fait une liste de matrices au cours du temps.
    end = time.time()
    print(len(L))
    x,y = MatCoord(TAILLE) #matrices coordonées pour le plot_surface
    fig = plt.figure(2) #création de la figure
    ay = fig.add_subplot(121, projection='3d') #pour comparer à la matrice à avoir
    init = ay.plot_surface(x,y,SOURCE1.matrice,cmap=cm.inferno)
    ax = fig.add_subplot(122, projection='3d') #ajout du subplot 3D
    z = L[0] #initialisation de l'animation
    dessin = ax.plot_surface(x,y,z,cmap=cm.inferno) #bis
    ani = animation.FuncAnimation(fig, data, fargs=(L, dessin, ax, x,y), interval=30,blit=False) #création de l'animation avec la fonction data qui selectionne la matrice dans la liste
    print("EOF, time elapsed during calculus: "+ str(round(end-begin,2)))
    plt.show()

def ETUDE6():
    print("Etude 6")
    begin = time.time()
    CalculEQMSpatialOpti(TAILLE,PasS, F, a, b, c, d, g, h, k, l)
    end = time.time()
    print("EOF, time elapsed during calculus: "+ str(round(end-begin,2)))

def ETUDE7():
    print("Etude 7")
    begin = time.time()
    CalculEQMTemporelExpOpti(Nt, TAILLE, Pas, dt, F, a, b, c, d, g, h, k, l)
    end = time.time()
    print("EOF, time elapsed during calculus: "+ str(round(end-begin,2)))

def ETUDE8():
    print("Etude 8")
    begin = time.time()
    CalculEQMTemporelImpOpti(Nt, TAILLE, Pas, dt, F, a, b, c, d, g, h, k, l)
    end = time.time()
    print("EOF, time elapsed during calculus: "+ str(round(end-begin,2)))

def ETUDE9():
    print("Etude 9")
    SOURCE1 = MatriceTh(F, TAILLE, a, b, c, d, g, h, k, l)
    #Graphe3D(SOURCE1.matrice)
    begin = time.time()
    L,Nt = ResolExpliciteConv(SOURCE1.matrice, dt, Acc) #nouvelle fonction qui fait une liste de matrices au cours du temps. (Val. fonc.: SOURCE, 0.9, 10**5)
    end = time.time()
    print("Nt=",Nt)
    print("EOF, time elapsed during calculus: "+ str(round(end-begin,2)))
    Graphe3D(L)

def ETUDE10():
    print("Etude 10")
    SOURCE1 = MatriceTh(F, TAILLE, a, b, c, d, g, h, k, l)
    #Graphe3D(SOURCE1.matrice)
    begin = time.time()
    L,Nt = ResolImpliciteConv(SOURCE1.matrice, dt, Acc) #nouvelle fonction qui fait une liste de matrices au cours du temps. (Val. fonc.: SOURCE, 0.9, 10**5)
    end = time.time()
    print("Nt=",Nt)
    print("EOF, time elapsed during calculus: "+ str(round(end-begin,2)))
    Graphe3D(L)