# -*- coding: utf-8 -*-
 
""" 
AlgorithmesResol.py

Fichier contenant les algorithmes de calcul de la diffusion thermique
en regime permament et en temporel.
"""

#----------------------------------------------------------------#

import numpy as np

import scipy as sp

from MATRICES.MatriceStatio import *

from MATRICES.MatriceTemp import *

#----------------------------------------------------------------#

def ResolStatio(SOURCE, *args):
    """
    Méthode de résolution stationnaire 
    de l'équation de la chaleur.

    Args:
        SOURCE (np.ndarray): Matrice source constante

    Returns:
        np.ndarray: Matrice qui vérifie l'équation de la chaleur.
    """
    N, M = np.shape(SOURCE)
    MatSys = MatSysStatio(N)
    S = VectSourceStatio(SOURCE)
    RES = np.linalg.solve(MatSys, S)
    RES = np.reshape(RES, (N-2, N-2))
    SOURCE[1:N-1, 1:N-1] = np.reshape(RES, (N-2,N-2))
    return SOURCE

def ResolExplicite(MatriceSource, dt, Nt, D=1.19e-4):
    """
    Méthode des Différences finies explicite:
    Donne un profil de la température d'une plaque carrée en
    fonction de sa distance à la source.

    Args:
        MatriceSource (np.array): Matrice constante qui sert de source
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
    Matvide[1:Nx-1,1:Ny-1]
    U = np.zeros(((Nx-2)**2, 1), dtype=float)
    A = MatSysTempExpli(Nx, dx, dt, D)
    Y = VecteurSourceTemp(Matvide,dx,dt,D)
    
    for j in range(Nt):
        U = np.dot(A, U) +Y
        print(str(int((j/(Nt))*100)) + "%")
    U=np.reshape(U,(Nx-2,Nx-2))
    
    Mat[1:Nx-1,1:Nx-1] += U
    return Mat

def ResolExpliciteL(MatriceSource, dt, Nt, D=1.19e-4,pas=10):
    """
    Méthode des Différences finies explicite:
    Donne un profil de la température d'une plaque carrée en
    fonction de sa distance à la source.

    Args:
        MatriceSource (np.array): Matrice constante qui sert de source
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
    L = []
    Matvide = Mat*1
    Matvide[1:Nx-1,1:Ny-1]
    U = np.zeros(((Nx-2)**2, 1), dtype=float)
    A = MatSysTempExpli(Nx, dx, dt, D)
    Matres = Mat*1

    Y = VecteurSourceTemp(Matvide,dx,dt,D)
    
    for j in range(Nt):
        U = np.dot(A, U) +Y
        if j%pas == 0:
            B = U*1
            Matres[1:Nx-1, 1:Nx-1] = np.reshape(B, (Nx-2,Nx-2))
            L.append(Matres*1)
            print(str(int((j/(Nt))*100)) + "%")
    U=np.reshape(U,(Nx-2,Nx-2))

    return L

def ResolImplicite(SOURCE, dt, Nt, D=1.19e-4):
    """
    Méthode de résolution implicite de l'équation de la chaleur.

    Args:
        SOURCE (np.ndarray): Matrice source constante
        dx (float): pas spatial
        dt (float): pas temporel
        D (float): coefficient de diffusion
        Nt (int): Nombre d'itérations temporelle

    Returns:
        np.ndarray: Matrice solution de l'équation de la chaleur
    """
    N,M = np.shape(SOURCE)
    dx = 1/(M-1)
    MatSys = MatSysTempImpli(N, dx, dt, D)
    MatInv = np.linalg.inv(MatSys)
    ALPHA = (dt*D)/(dx**2)
    
    S = VecteurSourceTemp(SOURCE, dx, dt, D)
    
    Y=np.zeros((((N-2)**2),1))
    for j in range(Nt):
        Y=np.dot(MatInv,Y)+np.dot(MatInv,S)
        print(str(int((j/(Nt))*100)) + "%")
    SOURCE[1:N-1, 1:N-1] = np.reshape(Y, (N-2,N-2))
    return SOURCE

def ResolImpliciteL(SOURCE, dt, Nt, D=1.19e-4,pas = 10):
    """
    Méthode de résolution implicite de l'équation de la chaleur et retourne un resutat sous forme de liste.

    Args:
        SOURCE (np.ndarray): Matrice source constante
        dx (float): pas spatial
        dt (float): pas temporel
        D (float): coefficient de diffusion
        Nt (int): Nombre d'itérations temporelle
        pas : détermine le nombre de matrice renvoyé par la liste.

    Returns:
        np.ndarray: Matrice solution de l'équation de la chaleur
    """
    N,M = np.shape(SOURCE)
    dx = 1/(M-1)
    L = []
    MatSys = MatSysTempImpli(N, dx, dt, D)
    MatInv = np.linalg.inv(MatSys)
    ALPHA = (dt*D)/(dx**2)
    Matres = SOURCE*1
    S = VecteurSourceTemp(SOURCE, dx, dt, D)
    
    Y=np.zeros((((N-2)**2),1))
    for j in range(Nt):
        Y=np.dot(MatInv,Y)+np.dot(MatInv,S)
        if j%pas == 0:
            U = Y*1
            Matres[1:N-1, 1:N-1] = np.reshape(U, (N-2,N-2))
            L.append(Matres*1)
            print(str(int((j/(Nt))*100)) + "%")
    return L


def ResolImpliciteConvMarchePas(SOURCE, dt, Acc, D=1.19e-4):
    """
    Méthode de résolution implicite de l'équation de la chaleur.

    Args:
        SOURCE (np.ndarray): Matrice source constante
        dx (float): pas spatial
        dt (float): pas temporel
        D (float): coefficient de diffusion
        Acc (int): précision sur le laplacien attendue.

    Returns:
        np.ndarray: Matrice solution de l'équation de la chaleur
    """
    N,M = np.shape(SOURCE)
    dx = 1/(M-1)
    Nt = 0
    MatSys = MatSysTempImpli(N, dx, dt, D)
    MatInv = np.linalg.inv(MatSys)
    ALPHA = (dt*D)/(dx**2)
    
    S = VecteurSourceTemp(SOURCE, dx, dt, D)
    
    Y=np.zeros((((N-2)**2),1))

    Test = 1
    while Test>= Acc:
        Y=np.dot(MatInv,Y)+np.dot(MatInv,S)
        B = Y*1
        if Nt%10 == 1000:
            SOURCE[1:N-1, 1:N-1] = np.reshape(B, (N-2,N-2))
            Test = np.sum(sp.ndimage.laplace(SOURCE))
        print(Nt)
        Nt += 1
    SOURCE[1:N-1, 1:N-1] = np.reshape(Y, (N-2,N-2))
    return SOURCE,Nt


#----------------------------------------------------------------#

if __name__ == "__main__":
    pass

#EOF  