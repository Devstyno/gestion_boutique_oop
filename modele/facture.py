from datetime import datetime
from modele.achat import Achat

class Facture():
    """ Une facture est identifiée par : le numéro de la facture, la date de la facture et une collection d'achats"""

    __effectif = 0

    # constructeur
    def __init__(self):
        self.__date : datetime = datetime.now()
        self.__collection_achats : list = []

        Facture.__effectif += 1
        self.__numero : int = Facture.__effectif
    
    # propriete numero
    @property
    def numero(self):
        return self.__numero
    
    # propriete date
    @property
    def date(self):
        return self.__date
    
    # propriete collection_achats
    @property
    def collection_achats(self):
        return self.__collection_achats
    
    @collection_achats.setter
    def collection_achats(self, value : list):
        self.__collection_achats = value

    # effectif
    @classmethod
    def effectif(cls):
        return cls.__effectif
    
    # methodes complementaires
    ## ajout d'un nouvel achat
    def ajouter_achat(self, achat : Achat):
        self.__collection_achats.append(achat)
    
    ## montant total de la facture
    def montant_total_facture(self):
        total = 0
        for achat in self.collection_achats:
            total += achat.prix_total()
        return total
    
    ## details de la facture
    def detail_facture(self):
        print(f"Numero: {self.numero}\t\t\t\t\t\t\t\tDate: {self.date.strftime('%Y-%m-%d %H:%M:%S')}")
        print("\t\t\t\t\tListe des achats")
        print("Designation\t\tPrix unitaire (XOF)\t\tQuantite\tPrix total (XOF)")
        for achat in self.collection_achats:
            # Utilisation de ljust pour aligner les colonnes
            designation = str(achat.article.designation).ljust(24)
            prix_unitaire = str(achat.article.prix).ljust(32)
            quantite = str(achat.quantite_achetee).ljust(16)
            prix_total = str(achat.prix_total()).ljust(20)
            print(f"{designation}{prix_unitaire}{quantite}{prix_total}")
        print(f"\nMontant total: {self.montant_total_facture()}")