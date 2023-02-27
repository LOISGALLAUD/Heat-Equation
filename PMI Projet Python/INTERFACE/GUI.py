# -*- coding: utf-8 -*-

"""
GUI.py

Fichier concernant l'interface graphique Tkinter.
"""

#----------------------------------------------------------------#

import  INTERFACE.Etudes as et
import tkinter as tk

#----------------------------------------------------------------#

def clear(canvas):
    for widget in canvas.winfo_children():
        widget.destroy()

def main():
    rootCanvas.pack_forget()
    mainCanvas.pack()

def retourEQM():
    EQMCanvas.pack_forget()
    mainCanvas.pack()
    
def retourGraphe():
    GraphCanvas.pack_forget()
    mainCanvas.pack()

def EQM():
    choixCanvas.pack_forget()
    EQMCanvas.pack()
    clear(EQMCanvas)
    tk.Button(EQMCanvas, text="EQM SPATIAL", font="Helvetica 50 bold", command=et.ETUDE6, fg="white", bg="black").pack()
    tk.Button(EQMCanvas, text="EQM TEMPOREL EXPLICITE", font="Helvetica 50 bold", command=et.ETUDE7, fg="white", bg="black").pack()
    tk.Button(EQMCanvas, text="EQM TEMPOREL IMPLICITE", font="Helvetica 50 bold", command=et.ETUDE8, fg="white", bg="black").pack()
    tk.Button(EQMCanvas, text="CONVERGENCE EXPLICITE", font="Helvetica 50 bold", command=et.ETUDE9, fg="white", bg="black").pack()
    tk.Button(EQMCanvas, text="CONVERGENCE IMPLICITE", font="Helvetica 50 bold", command=et.ETUDE10, fg="white", bg="black").pack()
    tk.Button(EQMCanvas, text="RETOUR", font="Helvetica 50 bold", fg="white", bg="black",command=retourEQM).pack()
    
def Graphe():
    choixCanvas.pack_forget()
    GraphCanvas.pack()
    clear(GraphCanvas)
    tk.Button(GraphCanvas, text="RESOLUTION STATIONNAIRE", font="Helvetica 50 bold", command=et.ETUDE1, fg="white", bg="black").pack()
    tk.Button(GraphCanvas, text="RESOLUTION EXPLICITE", font="Helvetica 50 bold", command=et.ETUDE2, fg="white", bg="black").pack()
    tk.Button(GraphCanvas, text="RESOLUTION EXPLICITE ANIMATION", font="Helvetica 50 bold", command=et.ETUDE3, fg="white", bg="black").pack()
    tk.Button(GraphCanvas, text="RESOLUTION IMPLICITE", font="Helvetica 50 bold", command=et.ETUDE4, fg="white", bg="black").pack()
    tk.Button(GraphCanvas, text="RESOLUTION IMPLICITE ANIMATION", font="Helvetica 50 bold", command=et.ETUDE5, fg="white", bg="black").pack()
    tk.Button(GraphCanvas, text="RETOUR", font="Helvetica 50 bold", fg="white", bg="black",command=retourGraphe).pack()
    
def Suivant():
    for widget in mainCanvas.winfo_children():
        if type(widget) == type(tk.Entry()):
            if widget.get() == "":
                return
    
    et.TAILLE = int(entryTaille.get())
    et.dt = int(entryDt.get())
    et.Nt = int(entryNt.get())
    et.Pas = int(entryPas.get())
    et.PasS = int(entryPasS.get())
    et.F = int(entryF.get())
    et.Acc = float(entryAcc.get())
    et.a = int(entryA.get())
    et.b = int(entryB.get())
    et.c = int(entryC.get())
    et.d = int(entryD.get())
    et.g = int(entryG.get())
    et.h = int(entryH.get())
    et.k = int(entryK.get())
    et.l = int(entryL.get()) 
    
    match et.F:
        case 1:
            et.F = et.f1
        case 2:
            et.F = et.f2
        case 3:
            et.F = et.f3
        case 4:
            et.F = et.f4
        case 5:
            et.F = et.f5
    
    mainCanvas.pack_forget()
    choixCanvas.pack()
    btnEQM.grid(row=0, column=0)
    btnGraph.grid(row=0, column=1)

#----------------------------------------------------------------#

root = tk.Tk()
root.title("EQUATION DE LA CHALEUR PMI")
root.state("zoomed")
root.configure(bg='black')
x0 = root.winfo_screenwidth()
y0 = root.winfo_screenheight()

rootCanvas = tk.Canvas(root, width=x0, height=y0, bg="black")
mainCanvas = tk.Canvas(root, width=x0, height=y0, bg="black")
choixCanvas = tk.Canvas(root, width=x0, height=y0, bg="black")
EQMCanvas = tk.Canvas(root, width=x0, height=y0, bg="black")
GraphCanvas = tk.Canvas(root, width=x0, height=y0, bg="black")

entryTaille = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryDt = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryNt = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryPas = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryPasS = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryF = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryAcc = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryA = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryB = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryC = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryD = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryG = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryH = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryK = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")
entryL = tk.Entry(mainCanvas, font="Helvetica 25 bold", fg="white", bg="black")

entryTaille.insert(0, 50)
entryDt.insert(0, 10)
entryNt.insert(0, 10**3)
entryPas.insert(0, 10)
entryPasS.insert(0, 1)
entryF.insert(0, 5)
entryAcc.insert(0, "0.01")
entryA.insert(0, 1)
entryB.insert(0, 1)
entryC.insert(0, 10)
entryD.insert(0, 1)
entryG.insert(0, 20)
entryH.insert(0, 10)
entryK.insert(0, 30)
entryL.insert(0, 8)

btnSuivant = tk.Button(mainCanvas, text="SUIVANT", command=Suivant, font="Helvetica 25 bold", fg="white", bg="black")
btnEQM = tk.Button(choixCanvas, text="EQM", font="Helvetica 50 bold", command=EQM, fg="white", bg="black")
btnGraph = tk.Button(choixCanvas, text="Graphe", font="Helvetica 50 bold", command=Graphe, fg="white", bg="black")

#----------------------------------------------------------------#

rootCanvas.pack()
tk.Label(rootCanvas, text="PMI\nEquation de la chaleur", font="Helvetica 80 bold", fg="white", bg="black", background="black").grid(row=0, column=0)
tk.Button(rootCanvas, text="SUIVANT", font="Helvetica 30 bold", fg="white", bg="black", border=0,command=main).grid(row=1, column=0)

tk.Label(mainCanvas, text="TAILLE :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=0, column=0)
entryTaille.grid(row=0, column=1)
tk.Label(mainCanvas, text="dt :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=1, column=0)
entryDt.grid(row=1, column=1)
tk.Label(mainCanvas, text="Nt :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=2, column=0)
entryNt.grid(row=2, column=1)
tk.Label(mainCanvas, text="Pas :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=3, column=0)
entryPas.grid(row=3, column=1)
tk.Label(mainCanvas, text="PasS :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=4, column=0)
entryPasS.grid(row=4, column=1)
tk.Label(mainCanvas, text="F :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=5, column=0)
entryF.grid(row=5, column=1)
tk.Label(mainCanvas, text="Acc :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=6, column=0)
entryAcc.grid(row=6, column=1)
tk.Label(mainCanvas, text="A :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=7, column=0)
entryA.grid(row=7, column=1)
tk.Label(mainCanvas, text="B :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=8, column=0)
entryB.grid(row=8, column=1)
tk.Label(mainCanvas, text="C :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=9, column=0)
entryC.grid(row=9, column=1)
tk.Label(mainCanvas, text="D :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=10, column=0)
entryD.grid(row=10, column=1)
tk.Label(mainCanvas, text="G :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=11, column=0)
entryG.grid(row=11, column=1)
tk.Label(mainCanvas, text="H :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=12, column=0)
entryH.grid(row=12, column=1)
tk.Label(mainCanvas, text="K :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=13, column=0)
entryK.grid(row=13, column=1)
tk.Label(mainCanvas, text="L :", font="Helvetica 20 bold", fg="white", bg="black").grid(row=14, column=0)
entryL.grid(row=14, column=1)
btnSuivant.grid(row=15, column=0)
#EOF