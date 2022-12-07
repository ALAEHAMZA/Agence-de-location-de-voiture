from ClasseVoiture import Voiture
class VoitureVip(Voiture):
    
    def __init__(self,i=0,ma="Par defaut",c="Par defaut",mo="Par defaut",p=0,t="SUV"):
        super().__init__(i,ma,c,mo,p)
        self.__Type=t

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self,t):
        if t=="4*4" or t=="SUV" or t=="minibus" or t=="limousine":
            self.__Type=t

    def __str__(self):
        return f"{super().__str__} , TYPE : {self.__Type}"

    






    
