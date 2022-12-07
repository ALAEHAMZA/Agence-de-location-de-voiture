from ClasseUtilisateur import Utilisateur
class ListeUtilisateur:

    def __init__(self,lu=[]):
        self.__ListUtilisateur=lu

    def authentifier(self,l,m):
        exist=False
        for i in self.__ListUtilisateur:
            if i.Login==l and i.MotDdePasse==m:
                exist=True
                break
        if exist:
            print("BIENVENUE")
        else:
            print("AUTHENTIFICATION INVALID")
        
    def ajouter(self,c,n,p,l,m,e):
        U=Utilisateur(c,n,p,l,m,e)
        for i in self.__ListUtilisateur:
            if i==U :
                print("DEJA EXIST")
            else:
                self.__ListUtilisateur.append(U)

    def supprimer(self,l):
        exist=False
        for i in self.__ListUtilisateur:
            if i.Login == l:
                exist=True
                U=i
                break
        if exist:
            self.__ListUtilisateur.remove(U)
        else:
            print("N'EXISTE PAS")

    def modifier(self,utilisateur,c,n,p,l,m,e):
        exist=False
        for i in self.__ListUtilisateur:
            if i == utilisateur:
                exist=True
                break
        if exist :
            utilisateur=(c,n,p,l,m,e)
        else:
            print("CE CLASS N'EXISTE PAS")
