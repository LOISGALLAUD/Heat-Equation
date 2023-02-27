# -*- coding: utf-8 -*-
 
""" 
CalculConvergence.py

Fichier contenant les algorithmes de calcul de convergence
en régime temporel.
"""

#----------------------------------------------------------------#

import numpy as np

import scipy as sp

from MATRICES.MatriceStatio import *

from MATRICES.MatriceTemp import *

from DONNEES.CalculEcarts import *

from INTERFACE.Graph3D import *

#----------------------------------------------------------------#


def ResolExpliciteConv(MatriceSource, dt, Acc, D=1.19e-4):
    """
    Méthode des Différences finies explicite:
    Donne un profil de la température d'une plaque carrée en
    fonction de sa distance à la source.

    Args:
        MatriceSource (np.array): Matrice théorique à vider
        dx (float): Pas spatial
        dt (float): Pas temporel
        Nt (int): Nombre de points dans le temps
        D (float): Coefficient de diffusion
        
    Returns:
        np.ndarray: Matrice représentant la température 
        en chaque point de l'espace (x, y)
    """
    Mat = MatriceSource
    Nx,Ny = np.shape(Mat)
    dx = 1/(Nx-1)
    Matvide = Mat*1
    Matvide[1:Nx-1,1:Ny-1] = 0
    U = np.zeros(((Nx-2)**2, 1), dtype=float)
    A = MatSysTempExpli(Nx, dx, dt, D)
    Y = VecteurSourceTemp(Matvide,dx,dt,D)
    test=1
    Nt=0
    while test > Acc:
        U = np.dot(A, U) +Y
        B= U*1
        B=np.reshape(B,(Nx-2,Nx-2))
        Matvide[1:Nx-1,1:Nx-1] = B
        test = EQM(Mat, Matvide )
        Nt += 1
        print(round(test,5))
    U=np.reshape(U,(Nx-2,Nx-2))
    return Matvide, Nt 


def ResolImpliciteConv(MatriceTh, dt, Acc, D=1.19e-4):
    """
    Méthode de résolution implicite de l'équation de la chaleur.

    Args:
        MatriceTh (np.ndarray): Matrice théorique
        dt (float): pas temporel
        D (float): coefficient de diffusion
        Acc (int): précision sur le laplacien attendue.

    Returns:
        np.ndarray: Matrice solution de l'équation de la chaleur
    """
    Mat = MatriceTh
    N,M = np.shape(MatriceTh)
    dx = 1/(M-1)
    Matvide = Mat*1
    Matvide[1:N-1,1:M-1] = 0
    Nt = 0
    MatSys = MatSysTempImpli(N, dx, dt, D)
    MatInv = np.linalg.inv(MatSys)
    
    S = VecteurSourceTemp(Matvide, dx, dt, D)
    
    Y=np.zeros((((N-2)**2),1))

    Test = 1
    while Test > Acc:
        Y=np.dot(MatInv,Y)+np.dot(MatInv,S)
        B = Y*1
        B=np.reshape(B,(N-2,M-2))
        Matvide[1:N-1,1:M-1] = B
        Test = EQM(Mat, Matvide)
        print(round(Test,5))
        Nt += 1
    return Matvide,Nt


#----------------------------------------------------------------#

if __name__ == "__main__":
    pass

#EOF  