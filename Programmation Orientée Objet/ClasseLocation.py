from datetime import *
from ClasseVoiture import Voiture
from ClasseClient import Client

class Location:
    
    auto=1
    def __init__(self,da=date(111,11,1),du=timedelta(),p=0,c=Client(),v=Voiture()):
        self.__idLocation=Location.auto
        Location.auto+=1
        self.__dateLocation=da
        self.__dureeLocation=du
        self.__prixLocation=p
        self.__client=c
        self.__voiture=v
        
    @property
    def idLocation(self):
        return self.__idLocation
    @property
    def dateLocation(self):
        return self.__dateLocation
    @dateLocation.setter
    def dateLocation(self,da):
        self.__dateLocation=da
    @property
    def dureeLocation(self):
        return self.__dureeLocation
    @dureeLocation.setter
    def dureeLocation(self,da):
        self.__dateLocation=da
    @property
    def prixLocation(self):
        return self.__prixLocation
    @prixLocation.setter
    def prixLocation(self,p):
        self.__prixLocation=p  
    @property
    def client(self):
        return self.__client
    @client.setter
    def client(self,c):
        self.__client=c
    @property
    def voiture(self):
        return self.__voiture
    @voiture.setter
    def voiture(self,v):
        self.__voiture=v
    
    def __str__(self):
        return f"ID DE LOCATION : {Location.auto} , DATE DE LOCATION : {self.__dateLocation} , DUREE DE LOCATION : {self.__dureeLocation} , PRIX DE LOCATION : {self.__prixLocation} , CLIENT : {self__client} , VOITURE : {self.__voiture}"

    

        
        
