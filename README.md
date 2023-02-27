<img src="IMAGES/tps-logo.png">

# **PROJET MATHEMATIQUES INFORMATIQUE**
# ***Equation de la chaleur***


Ce fichier README est un tutoriel d'utilisation pour l'interface graphique du projet.

---

## **Interface graphique**

L'interface graphique est codée grâce à la bibliothèque tkinter. Elle est structurée comme suit:

* ### **Menu principal**

    Pour poursuivre la navigation dans le projet, il suffit d'apuyer sur ***SUIVANT***.

---

* ### **Menu de saisie des constantes**

    Un tableau de donnée est affiché. Les lignes du tableaux sont déjà remplies, ce sont des valeurs choisies arbitrairement que l'utilisateur peut changer à sa guise.

    Voici un inventaires des constantes de leur utilisation dans la code:

    * ***TAILLE***:
        Taille des matrices sur lesquelles les calculs seront effectués. Plus la taille des matrices est grande, plus les graphiques 3D auront l'air lisses.
    * ***dt***:
        Pas temporel des calculs.
    * ***Nt***:
        Nombre de subdivision de temps.
    * ***Pas***:
        Intervalle entre deux points des graphiques d'EQM ou de matrices dans les animations temporelles.
    * ***PasS***:
        Intervalle entre deux points des graphiques d'EQM spatial.
    * ***F***:
        Correspond au profil de température étudié lors des simulations. Le profil de température 4 et 5 sont des combinaisons linéaires des profils 1,2 et 3.
    * ***Acc***:
        Condition de précision sur les calculs de temps de convergence.
    * ***a, b, ..., l***:
        Constantes utilisése dans les différents profils de température (voir l'énoncé du PMI).

---

* ### **Menu type de simulation**

    Deux boutons sont affichés, ***EQM*** et ***Graphes***.
    Si l'utilisateur clique sur ***EQM***, il accédera aux différents types d'EQM disponibles. 
    Si l'utilisateur clique sur ***Graphes***, il accédera aux différents types de simulations 3D et animation 3D disponibles (Résolution Spatiale, Temporelle implicite ou explicite)

---
---

***Groupe de PMI:***

* Benjamin DEMONSANT
* Emilie FERREIRA
* Loïs GALLAUD
* Nathan GRILLET-NIESS