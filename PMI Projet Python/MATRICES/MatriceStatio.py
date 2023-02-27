# -*- coding: utf-8 -*-
 
""" 
MatriceSatio.py

Fichier contenant toutes les fonctions relatives à la création des 
matrices qui représentent le problème en régime stationnaire.
"""

#----------------------------------------------------------------#

import numpy as np

#----------------------------------------------------------------#

def MatSysStatio(N:int):
    """
    Fonction renvoyant la matrice système (A) pour la
    résolution du problème stationnaire (A*X=Y). 
    
    Args:
        N (int): Taille de la matrice A

    Returns:
        A (np.ndarray): Matrice A de l'équation A*X=Y
    """
    #Création du premier bloc qui sera répété
    P=np.zeros((N-2,N-2))
    for i in range(N-2):
        for j in range(N-2):
            if i==j:
                P[i,j]=4
            elif i==j+1:
                P[i,j]=-1
            elif j==i+1:
                P[i,j]=-1
                
    #Création du second bloc qui sera répété
    Q=np.zeros((N-2,N-2))
    for i in range(N-2):
        for j in range(N-2):
            if i==j:
                Q[i,j]=-1

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

#----------------------------------------------------------------# Vecteur Source Temporel

def VectSourceStatio(A:np.ndarray):
    """
    Calcule le vecteur constant stationnaire Y à partir de la matrice de Coeur vidé pour la partir stationnaire.
    Sans trop de calculs.
    
    Args: 
        A (np.ndarray): Matrice source avec un coeur vidé.
        
    Returns:
        Y (np.ndarray): Vecteur colonne Y
    """
    N, M = np.shape(A)
    Y = np.zeros(((N-2)*(N-2),1), dtype=float)
    n = 0
    
    for i in range(1, N-1):
        for j in range(1, N-1):
            Y[n, 0] += A[i+1, j]
            Y[n, 0] += A[i-1, j]
            Y[n, 0] += A[i, j+1]
            Y[n, 0] += A[i, j-1]
            n += 1 #comptage des éléments déjà vérifié par les commandes précédentes
    return Y
#EOF