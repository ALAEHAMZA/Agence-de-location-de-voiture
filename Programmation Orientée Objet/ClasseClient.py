from ClassePersonne import Personne
class Client(Personne):
    def __init__(self,c=0,n="defaut",p="defaut",np=0,t=0):
        super().__init__(c,n,p)
        self.__NumPermis=np
        self.__tele=t

    @property
    def NumPermis(self):
        return self.__NumPermis
    @NumPermis.setter
    def NumPermis(self,np):
        self.__NumPermis=np
    @property
    def tele(self):
        return self.__tele
    @tele.setter
    def tele(self,t):
        self.__tele=t

    def __str__(self):
        return f"{super().__str__} , NUMERO DE PERMIS : {self.__NumPermis} , Telephone : {self.__tele}"
