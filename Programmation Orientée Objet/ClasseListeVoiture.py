from ClasseVoiture import Voiture
class ListeVoiture:

    def __init__(self,lv):
        self.__ListVoiture=lv

    def ajouter(self,i,ma,c,mo,p):
        V=Voiture(i,ma,c,mo,p)
        for i in self.__ListVoiture:
            if i==V :
                print("DEJA EXIST")
            else:
                self.__ListVoiture.append(V)

    def supprimer(self,i):
        exist=False
        for i in self.__ListVoiture:
            if i.immatriculation == i:
                exist=True
                V=i
                break
        if exist:
            self.__ListVoiture.remove(V)
        else:
            print("N'EXISTE PAS")

    def modifier(self,voiture,i,ma,c,mo,p):
        exist=False
        for i in self.__ListVoiture:
            if i == voiture:
                exist=True
                break
        if exist :
            voiture=(i,ma,c,mo,p)
        else:
            print("CE CLASS N'EXISTE PAS")
