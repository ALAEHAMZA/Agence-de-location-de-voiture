from tkinter import *
from tkinter import messagebox
import tkinter as tkinter

from InterfaceAccueil import acceuil

interface=Tk()
interface.title("Agence De Location De Voiture - Connexion")
interface.geometry("950x550+180+50")

logo=Canvas(interface,width=200,height=700)
logo.place(x=0,y=0)

interface.minsize(height=700,width=200)
interface.resizable(height=False,width=False)
img=PhotoImage(file="a.png")
back=Label(image=img)
back.place(x=0,y=0)

log=Label(text="LOGIN",font=('arial',17,'bold'),fg="grey")
log.place(x=675,y=270)
 
mdp=Label(text="MOT DE PASSE",font=('arial',17,'bold'),fg="grey")
mdp.place(x=640,y=350)

logEntry=Entry(width=30,relief=FLAT,font=('arial',20),fg="grey")
logEntry.place(x=490,y=305)

mdpEntry=Entry(width=30,show="*",relief=FLAT,font=('arial',20),fg="grey")
mdpEntry.place(x=490,y=390)

def cmdSeconnecter():
    if logEntry.get()!="" and mdpEntry.get()!="" :
        messagebox.showinfo("Welcomme","You are registered succesfilly!!")
        acceuil()
    else:
        messagebox.showinfo("Error","PLEASE ENTER LOGIN AND PASSWORD!!")


submit=Button(text="Se connecter",command=cmdSeconnecter,bg="grey",fg="#fff",relief=FLAT,font=('arial',12),width=20)
submit.place(x=640,y=480)




interface.mainloop()
