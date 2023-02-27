# -*- coding: utf-8 -*-

"""
ProfilsSource.py

Script contenant les fonction qui crée les matrices des profils de sources.
"""

#----------------------------------------------------------------#

import numpy as np

#----------------------------------------------------------------#

class MatriceTh:
    def __init__(self, f, N, *args):
        """
        Crée une matrice qui représente un profil de
        température qui vérifie l'équation de la chaleur.

        Args:
            N (int): Taille de la matrice carrée
            f (lambda func): Fonction de répartition 
                de la température sur la plaque (dépend de x et y)
        """
        self.taille = N # La matrice est carrée donc on peut stocker uniquement dans N
        self.fonction = f
        
        self.matrice = np.zeros((N, N), dtype=float)
        dx = 1/(N-1)
        dy = 1/(N-1)
        
        # Création de la matrice
        for i in range(N):
            for j in range(N):
                self.matrice[i,j] = self.fonction(dx*i, dy*j, *args)
                
        self.ligneHaut = self.matrice[0, :]
        self.colonneDroite = self.matrice[:, self.taille-1]
        self.ligneBas = self.matrice[self.taille-1, :]
        self.colonneGauche = self.matrice[:, 0]
                
    def ExtraireSources(self):
        """
        Etrait les vecteurs sources d'une matrice théorique (ses vecteurs-côtés):   
        [[x x x x x x] 
         [x o o o o x] 
         [x o o o o x] 
         [x o o o o x] 
         [x o o o o x] 
         [x x x x x x]]

        Returns:
            (np.array, ...): tuple contenant les vecteurs colonnes des côtés de la matrice.
        """
        return self.ligneHaut, self.colonneDroite, self.ligneBas, self.colonneGauche
        
    def MatriceSource(self):
        """
        Créer une matrice source associée à la matrice théorique:
        [[x x x x x x] 
         [x 0 0 0 0 x] 
         [x 0 0 0 0 x] 
         [x 0 0 0 0 x] 
         [x 0 0 0 0 x] 
         [x x x x x x]]
        Cette matrice sera utilisée comme terme de source constant.

        Returns:
            np.array: Matrice avec uniquement ses bords non-nuls
        """
        A = self.matrice.copy() # Pour éviter les effets de bords
        
        A[1:self.taille-1, 1:self.taille-1] = 0
        self.source = A
        
        return self.source

    def Afficher(self):
        print(self.matrice)    

#----------------------------------------------------------------# Différents profils de température

def f1(x, y, a, b, c, d, f, g, k, l):
    f, g, k, l = 0, 0, 0, 0
    return a*x+b*y+c*x*y+d

def f2(x, y, a, b, c, d, f, g, k, l):
    a, b, c, d, k, l = 0, 0, 0, 0, 0, 0
    return f*np.sin(g*x)*np.exp(-g*y)

def f3(x, y, a, b, c, d, f, g, k, l):
    a, b, c, d, f, g = 0, 0, 0, 0, 0, 0
    return k*np.sin(l*y)*np.exp(-l*x)

def f4(x, y, a, b, c, d, f, g, k, l):
    k, l = 0, 0
    return f1(x, y, a, b, c, d, f, g, k, l) + f2(x, y, a, b, c, d, f, g, k, l)

def f5(x, y, a, b, c, d, f, g, k, l):
    return f1(x, y, a, b, c, d, f, g, k, l) + f2(x, y, a, b, c, d, f, g, k, l) +f3(x, y, a, b, c, d, f, g, k, l)

#----------------------------------------------------------------# Définition des matrices théoriques

#N=10
#M1 = MatriceTh(f1, N, 5 , 5, 10, 5)
#M2 = MatriceTh(f2, N, 5 , 5, 10, 5)
#M3 = MatriceTh(f3, N, 5 , 5, 10, 5)
#M4 = MatriceTh(f4, N, 5 , 5, 10, 5)

#----------------------------------------------------------------#

if __name__ == "__main__":
    pass

#EOF