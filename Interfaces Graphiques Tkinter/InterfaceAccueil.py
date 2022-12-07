from tkinter import *
import tkinter as tkinters

from InterfaceAjoutUtilisateur import AjoutUtilisateur
from InterfaceAjoutVoiture import AjoutVoiture
from InterfaceAjoutClient import AjoutClient
from InterfaceAjoutLocation import AjoutLocation
class acceuil:
    def __init__(self):
        acceuil=Tk()
        acceuil.title("Agence De Location De Voiture - Acceuil")
        acceuil.geometry("950x550+180+50")
                
        logo=Canvas(acceuil,width=200,height=700)
        logo.place(x=0,y=0)

        acceuil.minsize(height=700,width=200)
        img1=PhotoImage(file="a.png")
        back=Label(image=img1)
        back.place(x=0,y=0)
        menu=Menu(acceuil)

        def cmdAJU():
            AjoutUtilisateur()
        def cmdAJV():
            AjoutVoiture()
        def cmdAJC():
            AjoutClient()
        def cmdAJL():
            AjoutLocation()


        def cmdAFU():
            AfficherLocation()
        def cmdAFV():
            AfficherVoiture()
        def cmdAFC():
            AfficherClient()
        def cmdAFL():
            AfficherLocation()

        utilisateur=Menu(menu,tearoff=0)
        utilisateur.add_command(label="Ajouter Utilisateur",command=cmdAJU)
        utilisateur.add_command(label="Afficher Utilisateur",command=cmdAFU)
        menu.add_cascade(label="Gestion Utilisateur",menu=utilisateur)

        client=Menu(menu,tearoff=0)
        client.add_command(label="Ajouter Client",command=cmdAJC)
        client.add_command(label="Afficher Client",command=cmdAFC)
        menu.add_cascade(label="Gestion Client",menu=client)

        voiture=Menu(menu,tearoff=0)
        voiture.add_command(label="Ajouter Voiture",command=cmdAJV)
        voiture.add_command(label="Afficher Voiture",command=cmdAFV)
        menu.add_cascade(label="Gestion Voiture",menu=voiture)

        location=Menu(menu,tearoff=0)
        location.add_command(label="Ajouter Location",command=cmdAJL)
        location.add_command(label="Afficher Location",command=cmdAL)
        menu.add_cascade(label="Gestion Locations",menu=location)



        acceuil.config(menu=menu)

        acceuil.mainloop()


