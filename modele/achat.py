from modele.article import Article

class Achat:
    """ Les attributs de la classe Achat sont : le numéro de l'achat, l'article concerné par l'achat et la quantité d'articles achetés"""

    __effectif = 0

    # constructeur
    def __init__(self, article : Article, qtte : int):
        self.__article : Article = article
        self.__quantite_achetee : int = qtte

        Achat.__effectif += 1
        self.__numero = Achat.__effectif
    
    # propriete numero
    @property
    def numero(self):
        return self.__numero
    
    # propriete article
    @property
    def article(self):
        return self.__article
    
    @article.setter
    def article(self, value : Article):
        self.__article = value
    
    # propriete quantite_achetee
    @property
    def quantite_achetee(self):
        return self.__quantite_achetee
    
    @quantite_achetee.setter
    def quantite_achetee(self, value : int): # modifier_quantite()
        self.__quantite_achetee = value
    
    # effectif
    @classmethod
    def effectif(cls):
        return cls.__effectif

    # methodes complementaires
    ## prix total
    def prix_total(self):
        return self.article.prix * self.quantite_achetee