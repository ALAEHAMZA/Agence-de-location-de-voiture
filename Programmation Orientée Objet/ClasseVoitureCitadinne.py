from ClasseVoiture import Voiture
class VoitureCitadinne(Voiture):
    
    def __init__(self,i=0,ma="Par defaut",c="Par defaut",mo="Par defaut",p=0,g="A"):
        super().__init__(i,ma,c,mo,p)
        self.__gamme=g

    @property
    def gamme(self):
        return self.__gamme
    @gamme.setter
    def gamme(self,g):
        if g=="A" or g=="B" or g=="C":
            self.__gamme=g

    def __str__(self):
        return f"{super().__str__} , GAMME : {self.__gamme}"

    
