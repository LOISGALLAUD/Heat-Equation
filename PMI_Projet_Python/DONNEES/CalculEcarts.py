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
import time

#----------------------------------------------------------------#

def EQM(MatriceTheorique:np.array, MatriceCalculee:np.array):
    """
    Méthode de l'écart quadratique moyen.

    Args:
        MatriceTheorique (np.array): _description_
        MatriceCalculee (np.array): _description_

    Returns:
        float: Ecart quadratique moyen
    """
    
    sum = 0
    N,M = np.shape(MatriceTheorique)
    
    for i in range(N):
        for j in range(M):
            sum += (MatriceTheorique[i, j] - MatriceCalculee[i, j])**2
    return sum/N**2

def testCalculEQM(tailleFinale):
    """
    Ici on calcul les données pour pouvoir afficher l'EQM en fct de dx.
    La boucle interne gère la dimension des matrices carée de 3 à TailleFinale.
    

    Args:
        tailleFinale (int): Dimension finale des Matrices de la boucle.
    """
    LEQM = []
    X = []
    for k in range(3, tailleFinale+1):
        N = k
        M1 = MatriceTh(f1, k, 10, 20, 5, 20, 30, 6, 15, 12)
        SOURCE = M1.MatriceSource()
        SOURCE[1:N-1,1:N-1] = 0
        #Matriceth = DiffFiniesExp(SOURCE,0.1,0.1,1e-4,10000)
        Matriceth = ResolStatio(SOURCE)
        LEQM.append(EQM(Matriceth, M1.matrice))
        X.append((1/(k+1)))
    plt.figure("EQM fct de N")
    plt.plot(X, LEQM)
    plt.grid()
    plt.show()
    
def CalculEQMSpatial(TailleFinale, pas, F, a, b, c, d, g, h, k, l):
    """
    Ici on calcul les données pour pouvoir afficher l'EQM en fct de dx.
    La boucle interne gère la dimension des matrices carée de 3 à TailleFinale.

    TailleFinale : Dimension finale des Matrices de la boucle.
    """
    
    LEQM = []
    X = []
    for k in range(3, TailleFinale, pas):
        print(str(int((k/(TailleFinale))*100)) + "%")
        start = time.time()
        M = MatriceTh(F, k, a, b, c, d, g, h, k, l)
        SOURCE = M.MatriceSource()
        SOURCE[1:k-1,1:k-1] = 0
        Matriceth = ResolStatio(SOURCE)
        LEQM.append(EQM(Matriceth, M.matrice))
        X.append((1/(k+1)))
        end = time.time()
        print("elapsed: "+str(round(end-start,2)))
    plt.figure("EQM fct de dx")
    plt.title("EQM=f(dx)")
    plt.grid()
    plt.xlabel("log(dx)")
    plt.ylabel("Erreur quadratique moyenne")
    plt.loglog(X,LEQM,'+')
    plt.show()
    
def CalculEQMTemporelExp(TempsFinal, TAILLE, pas, F, a, b, c, d, g, h, k, l):
    """
    Ici on calcul les données pour pouvoir afficher l'EQM en fct de dt.
    On prend une matrice de taille 30.

    TempsFinal : Nombre maximum d'itération de la boucle.
    """
    LEQM = []
    X = []
    N = TAILLE
    for k in range(1, TempsFinal, pas):
        print(str(int((k/(TempsFinal))*100)) + "%")
        start = time.time()
        M = MatriceTh(F, N, a, b, c, d, g, h, k, l)
        SOURCE = M.MatriceSource()
        SOURCE[1:N-1,1:N-1] = 0
        Matriceth = ResolExplicite(SOURCE, 0.1, k)
        LEQM.append(EQM(Matriceth, M.matrice))
        X.append(k)
        end = time.time()
        print("elapsed: "+str(round(end-start,2)))
    plt.figure("EQM fct de k")
    plt.title("EQM=f(dt)")
    plt.grid()
    plt.xlabel("log(dt)")
    plt.ylabel("Erreur quadratique moyenne")
    plt.plot(X,LEQM,'+')
    plt.show()


def CalculEQMTemporelImp(TempsFinal, TAILLE, pas, F, a, b, c, d, g, h, k, l):
    """
    Ici on calcul les données pour pouvoir afficher l'EQM en fct de dt.
    On prend une matrice de taille 30.

    TempsFinal : Nombre maximum d'itération de la boucle.
    """
    LEQM = []
    X = []
    N = TAILLE
    for k in range(1, TempsFinal, pas):
        print(str(int((k/(TempsFinal))*100)) + "%")
        start = time.time()
        M = MatriceTh(F, N, a, b, c, d, g, h, k, l)
        SOURCE = M.MatriceSource()
        SOURCE[1:N-1,1:N-1] = 0
        Matriceth = ResolImplicite(SOURCE, 0.1, k) 
        LEQM.append(EQM(Matriceth, M.matrice))
        X.append(k)
        end = time.time()
        print("elapsed: "+str(round(end-start,2)))
    plt.figure("EQM fct de k")
    plt.title("EQM=f(dt)")
    plt.grid()
    plt.xlabel("log(dt)")
    plt.ylabel("Erreur quadratique moyenne")
    plt.plot(X,LEQM,'+')
    plt.show()
#----------------------------------------------------------------#

if __name__=="__main__":
    print(EQM(np.array([[1, 2, 3], 
                        [1, 2, 3], 
                        [1, 2, 3]]),
              np.array([[1, 2, 3],
                        [1, 2, 3], 
                        [1, 2, 3]])))
    
#EOF