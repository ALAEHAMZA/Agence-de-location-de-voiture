from ClasseClient import Client
class ListeClient:

    def __init__(self,lc=[]):
        self.__ListClient=lc
        
    def ajouter(self,c,n,p,np,t):
        C=Client(c,n,p,np,t)
        for i in self.__ListClient:
            if i==C :
                print("DEJA EXIST")
            else:
                self.__ListClient.append(C)

    def supprimer(self,c):
        exist=False
        for i in self.__ListClient:
            if i.Cin == c:
                exist=True
                C=i
                break
        if exist:
            self.__ListClient.remove(C)
        else:
            print("N'EXISTE PAS")

    def modifier(self,client,c,n,p,np,t):
        exist=False
        for i in self.__ListClient:
            if i == client:
                exist=True
                break
        if exist :
            client=(c,n,p,np,t)
        else:
            print("CE CLASS N'EXISTE PAS")


        
                
