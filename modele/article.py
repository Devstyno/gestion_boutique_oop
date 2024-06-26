class Article:
    """ Un article est caractérisé par un Code, une Désignation, un Prix, une Catégorie et une Quantité en stock"""

    __effectif = 0

    # constructeur
    def __init__(self, code : str, design : str, prix : float, cat : str, qtte : int):
        self.__code : str = code
        self.__designation : str = design
        self.__prix : float = prix
        self.__categorie : str = cat
        self.__quantite_en_stock : int = qtte
    
    # propriete code
    @property
    def code(self):
        return self.__code
    
    @code.setter
    def code(self, value : str):
        self.__code = value
    
    # propriete designation
    @property
    def designation(self):
        return self.__designation
    
    @designation.setter
    def designation(self, value : str):
        self.__designation = value
    
    # propriete prix
    @property
    def prix(self):
        return self.__prix
    
    @prix.setter
    def prix(self, value : float):
        self.__prix = value
    
    # propriete categorie
    @property
    def categorie(self):
        return self.__categorie
    
    @categorie.setter
    def categorie(self, value : str):
        self.__categorie = value
    
    # propriete quantite_en_stock
    @property
    def quantite_en_stock(self):
        return self.__quantite_en_stock
    
    @quantite_en_stock.setter
    def quantite_en_stock(self, value : int):
        self.__quantite_en_stock = value
    
    # effectif
    @classmethod
    def effectif(cls):
        return cls.__effectif
    
    # methodes complementaires
    ## afficher
    def afficher(self):
        return f"Code : {self.code}\nDesignation : {self.designation}\nPrix : {self.prix}\nCategorie : {self.categorie}\nQuantite en stock : {self.quantite_en_stock}"

    # comparer    
    def comparer(self, autre_article):
        if isinstance(autre_article, Article):
            if self.code == autre_article.code and self.designation == autre_article.designation and self.prix == autre_article.prix and self.categorie == autre_article.categorie and self.quantite_en_stock == autre_article.quantite_en_stock :
                return "Ces deux articles sont identiques."
            return "Ces deux articles sont differents."
        raise ValueError("L'objet passé en argument n'est pas un article !")
