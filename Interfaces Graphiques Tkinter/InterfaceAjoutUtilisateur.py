from tkinter import *
import tkinter as tkinter
class AjoutUtilisateur():
    def __init__(self):
        AU=Tk()
        AU.title("Agence De Location De Voiture - Ajouter Utilisateur")
        AU.geometry("950x550+180+50")

        logo=Canvas(AU,width=200,height=700)
        logo.place(x=0,y=0)

        AU.minsize(height=700,width=200)
        AU.resizable(height=False,width=False)
        img=PhotoImage(file="a.png")
        back=Label(image=img)
        back.place(x=0,y=0)

        log=Label(text="LOGIN",font=('arial',17,'bold'),fg="grey")
        log.place(x=675,y=270)
         
        mdp=Label(text="MOT DE PASSE",font=('arial',17,'bold'),fg="grey")
        mdp.place(x=640,y=350)


        mail=Label(text="EMAIL",font=('arial',17,'bold'),fg="grey")
        mail.place(x=680,y=425)

        logEntry=Entry(width=30,relief=FLAT,font=('arial',20),fg="grey")
        logEntry.place(x=490,y=305)

        mdpEntry=Entry(width=30,show="*",relief=FLAT,font=('arial',20),fg="grey")
        mdpEntry.place(x=490,y=390)

        mailEntry=Entry(width=30,relief=FLAT,font=('arial',20),fg="grey")
        mailEntry.place(x=490,y=460)


        submit=Button(text="Ajouter Utilisateur",bg="grey",fg="#fff",relief=FLAT,font=('arial',12),width=20)
        submit.place(x=640,y=515)




        AU.mainloop()
