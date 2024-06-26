# # Simulez ensuite la vente des articles

from modele.article import Article
from modele.achat import Achat
from modele.facture import Facture

# • Instanciez deux nouveaux articles
art_1 = Article("CODE001", "Gourde", 2500, "Accessoire", 15)
art_2 = Article("CODE002", "Stylo Schneider", 150, "Academique", 20)

# • Affichez les informations de l’article
print(art_1.afficher())

# • Créez aussi deux achats correspondants aux deux articles instanciés
achat_1 = Achat(art_1, 3)
achat_2 = Achat(art_2, 10)

# • Modifiez la quantité d’articles achetés pour le premier achat
achat_1.quantite_achetee = 4

# • Créez ensuite une nouvelle facture correspondant à une nouvelle vente
facture_1 = Facture()

# • Ajoutez ensuite les deux achats précédents à la facture
facture_1.ajouter_achat(achat_1)
facture_1.ajouter_achat(achat_2)

# • Affichez le montant total de la facture
print(facture_1.montant_total_facture())

# • Affichez tous les détails de la facture
facture_1.detail_facture()


