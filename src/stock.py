import numpy as np

def ajouter_produit():
    global produits
    nom_produit = input("Enter le nom de produit : ")
    quantite = int(input("Enter la quantité de produit : "))
    prix_unitaire = int(input("Enter le prix unitaire de produit : "))

    produits= np.append(produits,[[ nom_produit , quantite , prix_unitaire ]],axis=0)


def afficher():
    global produits
    for item in produits :
        print(item)
    


