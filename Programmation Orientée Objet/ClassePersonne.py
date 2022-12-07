class Personne:
    
    def __init__(self,c=0,n="defaut",p="defaut"):
        self._Cin=c
        self._Nom=n
        self._Prenom=p

    @property
    def Cin(self):
        return self._Cin
    @Cin.setter
    def Cin(self,c):
        self._Cin=c
    @property
    def Nom(self):
        return self._Nom
    @Nom.setter
    def Nom(self,n):
        self._Nom=n  
    @property
    def Prenom(self):
        return self._Prenom
    @Prenom.setter
    def Prenom(self,p):
        self._Prenom=p

    def __str__(self):
        return f"CIN : {self._Cin} , NOM : {self._Nom} , PRENOM : {self._Prenom}"

    
