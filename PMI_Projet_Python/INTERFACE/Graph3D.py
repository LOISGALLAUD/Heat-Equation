# -*- coding: utf-8 -*-

"""
Graph3D.py

Script contenant les fonctions qui créent
les matrices des profils de sources.
"""

#----------------------------------------------------------------#

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

#----------------------------------------------------------------#

def MatCoord(N:int):
    """
    Crée deux matrices de la forme:
    [[0. 0. 0. 0. 0.]   
     [1. 1. 1. 1. 1.]
     [2. 2. 2. 2. 2.]
     [3. 3. 3. 3. 3.]
     [4. 4. 4. 4. 4.]] 
    
    &
    [[0. 1. 2. 3. 4.]
     [0. 1. 2. 3. 4.]
     [0. 1. 2. 3. 4.]
     [0. 1. 2. 3. 4.]
     [0. 1. 2. 3. 4.]]
     
    Elles vont servir à la fonction qui affiche les graphes en 3D.
    
    Arg:
        N (int): Taille de la matrice.
        
    Returns:
        X, Y (tuple): Matrices carrées de taille N.
    """
    X = np.zeros((N, N))
    Y = np.zeros((N, N))
    
    for i in range(N):
        for j in range(N):
            X[i, j] = j
            Y[i, j] = i
    return X, Y

def Graphe3D(MATRICE):
    print("Affichage du graphe 3D...")
    fig = plt.figure(1)
    ax = fig.add_subplot(111, projection='3d')
    N, M = np.shape(MATRICE)
    X, Y = MatCoord(N)
    ax.plot_surface(X, Y, MATRICE, 
                    cmap=cm.inferno, antialiased=False)
    ax.set_xlabel("y", fontsize=15)
    ax.set_ylabel("x", fontsize=15)
    ax.set_zlabel("Température", fontsize=15)
    
    plt.show()

#----------------------------------------------------------------#

if __name__ == "__main__":
    print("Début de l'affichage.")
    
    M, N = MatCoord(5)
    print(N)
    print(M)

    print("Fin du script.")