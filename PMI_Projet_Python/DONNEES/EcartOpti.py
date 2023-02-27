# -*- coding: utf-8 -*-

"""
CalculEcarts.py

Script contenant les fonctions relatives aux calculs des écarts
"""

#----------------------------------------------------------------#

import numpy as np
import matplotlib.pyplot as plt

from SOLVEUR.AlgorithmesResol import *
from MATRICES.ProfilSource import *
from DONNEES.CalculEcarts import *
import time

#----------------------------------------------------------------#

def CalculEQMSpatialOpti(TailleFinale, pas, F, a, b, c, d, g, h, k, l):
    """
    Ici on calcul les données pour pouvoir afficher l'EQM en fct de dx.
    La boucle interne gère la dimension des matrices carée de 3 à TailleFinale.

    TailleFinale : Dimension finale des Matrices de la boucle.
    """
    
    LEQM = []
    X = []
    X1 = []
    Elap = []
    for k in range(3, TailleFinale):
        start = time.time()
        Mat = MatriceTh(F, k, a, b, c, d, g, h, k, l)
        SOURCE = Mat.MatriceSource()*1
        S = VectSourceStatio(SOURCE)
        MatSys = MatSysStatio(k)
        RES = np.linalg.solve(MatSys, S)
        if k%pas == 0:
            B=RES*1
            B = np.reshape(B, (k-2, k-2))
            SOURCE[1:k-1, 1:k-1] = B
            LEQM.append(EQM(Mat.matrice, SOURCE))
            X.append((1/(k+1)))
        end = time.time()
        X1.append((1/(k+1)))
        Tps = round(end-start,2)
        print(str(int((k/(TailleFinale))*100)) + "%")
        Elap.append(Tps)
        print("elapsed: "+str(Tps))
    plt.figure("EQM fct de dx")
    plt.title("EQM=f(dx)")
    plt.grid()
    plt.xlabel("log(dx)")
    plt.ylabel("Erreur quadratique moyenne")
    plt.loglog(X,LEQM,'+')
    plt.figure("Temps ecoulé en fonction de dx")
    plt.title("TimeElapsed=f(dx)")
    plt.grid()
    plt.xlabel("dx")
    plt.ylabel("Temps Ecoulé (s)")
    plt.plot(X1,Elap,'+')
    plt.show()

def CalculEQMTemporelExpOpti(TempsFinal, TAILLE, pas, dt, F, a, b, c, d, g, h, k, l, D=1.1909e-4):
    """
    Ici on calcul les données pour pouvoir afficher l'EQM en fct de dt.
    On prend une matrice de taille 50.

    TempsFinal : Nombre maximum d'itération de la boucle.
    """
    LEQM = []
    X = []
    X1 = []
    Elap = []
    N = TAILLE
    Mat = MatriceTh(F, N, a, b, c, d, g, h, k, l)
    Nx,Ny = np.shape(Mat.matrice)
    dx = 1/(Nx-1)
    Matvide = Mat.matrice*1
    Matvide[1:Nx-1,1:Ny-1] = 0
    U = np.zeros(((Nx-2)**2, 1), dtype=float)
    A = MatSysTempExpli(Nx, dx, dt, D)
    Y = VecteurSourceTemp(Matvide,dx,dt,D)

    for k in range(TempsFinal):
        print(str(int((k/(TempsFinal))*100)) + "%")
        start = time.time()
        U = np.dot(A, U) +Y
        if k%pas == 0:
            B = U*1
            B=np.reshape(B,(Nx-2,Nx-2))
            Matvide[1:TAILLE-1,1:TAILLE-1] = B
            LEQM.append(EQM(Mat.matrice, Matvide))
            X.append(k)
        end = time.time()
        X1.append(k)
        Tps = round(end-start,5)
        Elap.append(Tps)
        print("elapsed: "+str(round(Tps,2)))
    plt.figure("EQM fct de k")
    plt.title("EQM=f(Nt)")
    plt.grid()
    plt.xlabel("log(Nt)")
    plt.ylabel("log(Erreur quadratique moyenne)")
    plt.loglog(X,LEQM,'+')
    plt.figure("Temps ecoulé en fonction de Nt")
    plt.title("TimeElapsed=f(Nt)")
    plt.grid()
    plt.xlabel("dx")
    plt.ylabel("Temps Ecoulé (s)")
    plt.plot(X1,Elap,'+')
    plt.show()

def CalculEQMTemporelImpOpti(TempsFinal, TAILLE, pas, dt, F, a, b, c, d, g, h, k, l, D=1.1909e-4):
    """
    Ici on calcul les données pour pouvoir afficher l'EQM en fct de dt.
    On prend une matrice de taille 50.

    TempsFinal : Nombre maximum d'itération de la boucle.
    """
    LEQM = []
    X = []
    X1 = []
    Elap = []
    N = TAILLE
    Mat = MatriceTh(F, N, a, b, c, d, g, h, k, l)
    Nx,Ny = np.shape(Mat.matrice)
    dx = 1/(Nx-1)
    Matvide = Mat.matrice*1
    Matvide[1:Nx-1,1:Ny-1] = 0
    Y = np.zeros(((Nx-2)**2, 1), dtype=float)
    MatSys = MatSysTempImpli(N, dx, dt, D)
    MatInv = np.linalg.inv(MatSys)
    S = VecteurSourceTemp(Matvide,dx,dt,D)

    for k in range(TempsFinal):
        print(str(int((k/(TempsFinal))*100)) + "%")
        start = time.time()
        Y=np.dot(MatInv,Y)+np.dot(MatInv,S)
        if k%pas == 0:
            B = Y*1
            B=np.reshape(B,(Nx-2,Nx-2))
            Matvide[1:TAILLE-1,1:TAILLE-1] = B
            LEQM.append(EQM(Mat.matrice, Matvide))
            X.append(k)
        end = time.time()
        Tps = round(end-start,5)
        Elap.append(Tps)
        X1.append(k)
        print("elapsed: "+str(round(Tps,2)))
    plt.figure("EQM fct de k")
    plt.title("EQM=f(Nt)")
    plt.grid()
    plt.xlabel("Nt")
    plt.ylabel("Erreur quadratique moyenne)")
    plt.loglog(X,LEQM,'+')
    plt.figure("Temps ecoulé en fonction de Nt")
    plt.title("TimeElapsed=f(Nt)")
    plt.grid()
    plt.xlabel("dx")
    plt.ylabel("Temps Ecoulé (s)")
    plt.plot(X1,Elap,'+')
    plt.show()