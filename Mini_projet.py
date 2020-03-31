# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from tkinter import*
def newfen ():
    fen2=Toplevel(fen1)
    text= Label(side=top,text="Bienvenue , dans le mini-jeu de calcul mental" )
    text.pack()

fen1=Tk()

lanc= Button(fen1, text = "lancer" , command = newfen)
lanc.pack()

fen1.mainloop()
