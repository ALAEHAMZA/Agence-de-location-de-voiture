from ClassePersonne import Personne
class Utilisateur(Personne):
    
    def __init__(self,c,n,p,l,m,e):
        super().__init__(c,n,p)
        self.__Login=l
        self.__MotDdePasse=m
        self.__Email=e

    @property
    def Login(self):
        return self.__Login
    @Login.setter
    def Login(self,l):
        self.__Login=l
    @property
    def MotDdePasse(self):
        return  self.__MotDdePasse
    @MotDdePasse.setter
    def MotDdePasse(self,m):
        self.__MotDdePasse=m
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self,e):
        self.__Email=e

    def __str__(self):
        return f"{super().__str__} , LOGIN : {self.__Login} , MOT DE PASSE : {self.__MotDePasse} , EMAIL : {self.__Email}"
