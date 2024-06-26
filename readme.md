# Gestion d’une boutique de vente d’articles

On vous confie la mise en place d’un système de gestion de ventes des articles d’un magasin.
Pour cela, il faudra :

## Gérer les articles en créant une classe Article

- Un article est caractérisé par un Code, une Désignation, un Prix, une Catégorie et une Quantité en stock
- Ajoutez le constructeur de la classe en initialisant tous les attributs de la classe avec des valeurs reçues en paramètres
- Implémenter le principe de l’encapsulation pour tous les attributs d’instance de la classe
- Implémentez les méthodes suivantes :

    * afficher() permettant d’afficher toutes les informations d’un article
    * comparer() permettant de comparer deux (2) articles. Deux articles sont identiques quand ils ont les mêmes propriétés

## Gérer un achat

- Les attributs de la classe Achat sont : le numéro de l’achat, l’article concerné
par l’achat et la quantité d’articles achetés
- Ajoutez le constructeur de la classe en initialisant tous les attributs de la classe
avec des valeurs reçues en paramètres
- Implémenter le principe de l’encapsulation pour tous les attributs d’instance de
la classe
- Ajoutez aussi une méthode modifierQuantite() permettant de modifier la
quantité d’articles achetés après sa création en prenant la nouvelle quantité en
paramètre

## Ensuite, il va falloir gérer les ventes des articles en générant la facture à chaque vente

### Implémentation de la classe Facture

- Une facture est identifiée par : le numéro de la facture, la date de la facture et
une collection d’achats
- Ajoutez le constructeur de la classe en initialisant tous les attributs de la classe
avec des valeurs reçues en paramètres
- Implémenter le principe de l’encapsulation pour tous les attributs d’instance de
la classe
- Implémentez les méthodes suivantes :

    * ajouterAchat() : permet d’ajouter un achat à la collection d’achats d’une facture, vérifier la non existence du même achat dans la collection dans le cas contraire la méthode doit afficher un message d’erreur
    * montantTotalFacture() : retourne le montant total de la facture
    * detailsFacture() : affiche le numéro de la facture, la date de la facture, la liste des articles achetés, le montant total de la facture sous le format suivant :

        `

            Numero ...                                               Date ...

                                    Liste des achats
            
            Designation      Prix unitaire (XOF)     Quantite        Prix total
            ...              ...                     ...             ...


            Montant total : ...

        `

## Simulez ensuite la vente des articles

- Instanciez deux nouveaux articles
- Affichez les informations de l’article
- Créez aussi deux achats correspondants aux deux articles instanciés
- Modifiez la quantité d’articles achetés pour le premier achat
- Créez ensuite une nouvelle facture correspondant à une nouvelle vente
- Ajoutez ensuite les deux achats précédents à la facture
- Affichez le montant total de la facture
- Affichez tous les détails de la facture

## Note

_Vous pourrez utiliser la version ipynb du fichier tests pour proceder a une execution par bloc et avoir un meilleur apercu. Pour ce faire, installez l'extension de jupyter notebook dans votre IDE, notamment VSCode. Sinon, installez Anaconda._
_Pour le fichier main.py, libre a vous de l'ecrire comme vous voulez. Laissez parler votre inspiration !_
