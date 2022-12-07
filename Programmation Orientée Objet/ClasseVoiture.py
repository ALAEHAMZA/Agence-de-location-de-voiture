class Voiture:
    
    def __init__(self,i=0,ma="defaut",c="defaut",mo="defaut",p="defaut"):
        self._immatriculation=i
        self._marque=ma
        self._carburant=c
        self._modele=mo
        self._puissanceFiscale=p

    @property
    def immatriculation(self):
        return  self._immatriculation
    @immatriculation.setter
    def immatriculation(self,i):
        self._immatriculation=i
    @property
    def marque(self):
        return self._marque
    @marque.setter
    def marque(self,ma):
        self._marque=ma
    @property
    def carburant(self):
        return self._carburant
    @carburant.setter
    def carburant(self,c):
        self._carburant=c
    @property
    def modele(self):
        return self._modele
    @modele.setter
    def modele(self,mo):
        self._modele=mo
    @property
    def puissanceFiscale(self):
        return self._puissanceFiscale
    @puissanceFiscale.setter
    def puissanceFiscale(self,p):
        self._puissanceFiscale=p

    def __str__(self):
        return f"Immatriculation : {immatriculation} , Marque : {marque} , Carburant : {carburant} , Modele : {modele} , Puissance fiscale : {puissanceFiscale}"

    


    




        



    

        
