from ClasseLocation import Location

class ListeLocations:

    def _init_(self,ll=[]):
        self.__ListLocation=ll
    
    def AfficherListeLocation(self):
        return self.__ListLocation
    
    def AfficherListeLocationCitadine(self):
        l=[]
        for i in self.__ListLocation:
            if isinstance(i.voiture,VoitureCitadinne):
                l.append(i)
        return l
    
    def AfficherListeLocationVip(self):
        l=[]
        for i in self.__ListLocation:
            if isinstance(i.voiture,VoitureVip):
                l.append(i)
        return l
    
    def AfficherLocationMarque(self,m):
        l=[]
        for i in self.__ListLocation:
            if i.voiture.marque==m:
                l.append(i)
        return l
    
    def AfficherLocationImma(self,im):
        l=[]
        for i in self.__ListLocation:
            if i.Voiture.immatriculation==im:
                l.append(i)
        return l
    
    def AfficherLocationClient(self,cin):
        l=[]
        for i in self.__ListLocation:
            if i.Client.Cin==cin:
                l.append(i)
        return l
    
    def AjouterLocation(self,L):
        if L in self.__ListLocation:
            print("DEJA EXIST")
        else:
            self.__ListLocation.append(L)
            
    def SupprimerLocation(self,L):
        if Location in self.__ListLocation:
            self.__ListLocation.remove(L)
        else:
            print("N'EXISTE PAS")

    def FiltrerLocationDate(self,d):
         l=[]
         for i in self.__ListLocation:
             if i.DateLocation==date:
                 l.append(i)
         return l
        
