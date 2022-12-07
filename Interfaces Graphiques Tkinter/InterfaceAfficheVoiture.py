from tkinter import *
import tkinter as tkinter
from ClasseListeVoiture import ListeVoiture
class AfficherVoiture():
    def __init__(self):
        interface=Tk()
        interface.title("Agence De Location De Voiture - Ajouter Voiture")
        interface.geometry("950x550+180+50")

        logo=Canvas(interface,width=200,height=700)
        logo.place(x=0,y=0)


        interface.minsize(height=700,width=200)
        interface.resizable(height=False,width=False)
        img=PhotoImage(file="a.png")
        back=Label(image=img)
        back.place(x=0,y=0)

         c=20
        for i in ListeVoiture:
            c+=40
            log=Label(text=i,font=('arial',17,'bold'),fg="grey")
            log.place(x=100,y=c)
    
        interface.mainloop()
