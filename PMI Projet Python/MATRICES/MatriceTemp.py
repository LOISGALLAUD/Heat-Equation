# -*- coding: utf-8 -*-

"""
MatriceTemp.py

Solveur de systèmes temporels.
Contient toutes les fonctions nécessaires à la résolution
des systèmes en temporel.

Ce fichier est divisé en deux parties:
    - schéma implicite
    - schéma explicite
"""
#----------------------------------------------------------------#

import numpy as np

#----------------------------------------------------------------# Schéma Implicite

def MatSysTempImpli(N, dx, dt, D=1.19e-4):
    """
    Fonction renvoyant la matrice système (A) pour la
    résolution du problème temporel (AY_(t+1)=(1-4*ALPHA)*Y_(t)+B). 

    Args:
        N (int): Taille de la matrice.
        dx (float): pas spatial
        dt (float): pas temporel
        D (float): Coefficient de diffusion

    Returns:
        A (np.ndarray): Matrice A de l'équation AY_(t+1)=(1-4*ALPHA)*Y_(t)+B
    """
    #Calcul du coefficient Alpha
    ALPHA=(dt*D)/(dx**2)
    
    #Création du premier bloc qui sera répété
    P=np.zeros((N-2,N-2))
    for i in range(N-2):
        for j in range(N-2):
            if i==j:
                P[i,j]=1+4*ALPHA
            elif i==j+1:
                P[i,j]=-ALPHA
            elif j==i+1:
                P[i,j]=-ALPHA
                
   
    #Création du second bloc qui sera répété
    Q=np.zeros((N-2,N-2))
    for i in range(N-2):
        for j in range(N-2):
            if i==j:
                Q[i,j]=-ALPHA

    
    #Remplissage de la matrice à renvoyer
    A=np.zeros(((N-2)**2,(N-2)**2))
    for i in range(N-2):
        for j in range(N-2):
            if i==j:
                A[i*(N-2):i*(N-2)+(N-2),j*(N-2):j*(N-2)+(N-2)]=P
            elif i==j+1:
                A[i*(N-2):i*(N-2)+(N-2),j*(N-2):j*(N-2)+(N-2)]=Q
            elif j==i+1:
                A[i*(N-2):i*(N-2)+(N-2),j*(N-2):j*(N-2)+(N-2)]=Q
    return A

#----------------------------------------------------------------# Schéma Explicite

def MatSysTempExpli(N, dx, dt, D=1.19e-4):
    """
    Fonction renvoyant la matrice système (A) pour la
    résolution du problème temporel (Y_(t+1) = A*Y_(t) + B). 
    
    Args:
        N (int): Taille de la matrice.
        dx (float): Pas spatial.
        dt (float): Pas temporel.
        D (_type_): Coefficient de diffusion.

    Returns:
        np.ndarray: _description_
    """
    
    #Calcul du coefficient Alpha
    ALPHA = (dt*D)/(dx**2)
    #Création du premier bloc qui sera répété
    P = np.zeros((N-2, N-2))
    for i in range(N-2):
        for j in range(N-2):
            if i==j:
                P[i,j]=1-4*ALPHA
            elif i==j+1:
                P[i,j]=ALPHA
            elif j==i+1:
                P[i,j]=ALPHA
    
    #Création du second bloc qui sera répété
    Q=np.zeros((N-2,N-2))
    for i in range(N-2):
        for j in range(N-2):
            if i==j:
                Q[i,j]=ALPHA
    
    #Remplissage de la matrice à renvoyer
    A=np.zeros(((N-2)**2,(N-2)**2))
    for i in range(N-2):
        for j in range(N-2):
            if i==j:
                A[i*(N-2):i*(N-2)+(N-2),j*(N-2):j*(N-2)+(N-2)]=P
            elif i==j+1:
                A[i*(N-2):i*(N-2)+(N-2),j*(N-2):j*(N-2)+(N-2)]=Q
            elif j==i+1:
                A[i*(N-2):i*(N-2)+(N-2),j*(N-2):j*(N-2)+(N-2)]=Q
    return A

def DiffFiniesExp(MatriceSource, dt, Nt, D=1.19e-4):
    """
    Méthode des Différences finies explicite:
    Donne un profil de la température d'une plaque carrée en
    fonction de sa distance à la source.

    Args:
        MatriceSource (np.array): Matrice constante qui sert de source
        dx (int): Pas spatial
        dt (int): Pas temporel
        N (float): Nombre de point dans l'espace
        D (float): Coefficient de diffusion
        
    Returns:
        np.ndarray: Matrice représentant la température 
            en chaque point de l'espace (x, y)
    """
    Mat = MatriceSource
    Nx,Ny = np.shape(Mat)
    dx = 1/(Ny-1)
    Matvide = Mat*1
    Matvide[1:Nx-1,1:Nx-1]
    U = np.zeros(((Nx-2)**2, 1), dtype=float)
    A = MatSysTempExpli(Nx, dx, dt, D)
    Y = VecteurSourceTemp(Matvide, dx, dt,D)
    
    for j in range(Nt):
        U = np.dot(A, U) +Y
    U=np.reshape(U,(Nx-2,Nx-2))
    
    Mat[1:Nx-1,1:Nx-1] += U
    return Mat

#----------------------------------------------------------------# Vecteur Source Temporel

def VecteurSourceTemp(MatriceSource, dx, dt, D=1.19e-4):
    """
    Calcule le vecteur constant stationnaire Y à partir de la
    matrice de Coeur vidé pour la partie temporelle.
    Sans trop de calculs.

    Args:
        MatriceSource (np.ndarray): Matrice constante qui sert de source
        dx (float): pas spacial
        dt (float): pas temporel
        D (float): Coefficient de diffusion

    Returns:
        _type_: _description_
    """
    
    #Calcul du coefficient Alpha
    ALPHA=(dt*D)/(dx**2)
    
    #Calcul du vecteur source
    x,y = np.shape(MatriceSource)
    Y = np.zeros(((y-2)*(y-2),1))
    n = 0
    for i in range(1,x-1):
        for j in range(1,y-1):
            Y[n,0] += ALPHA*MatriceSource[i+1,j]
            Y[n,0] += ALPHA*MatriceSource[i-1,j]
            Y[n,0] += ALPHA*MatriceSource[i,j+1]
            Y[n,0] += ALPHA*MatriceSource[i,j-1]
            n += 1 #comptage des éléments déjà vérifié par les commandes précédentes
    return Y
#EOF