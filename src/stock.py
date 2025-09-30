from data import produits
import numpy as np

def ajouter_produit():
    global produits
    nom_produit = input("Enter le nom de produit : ")
    quantite = int(input("Enter la quantité de produit : "))
    prix_unitaire = int(input("Enter le prix unitaire de produit : "))

    produits= np.append(produits,[[ nom_produit , quantite , prix_unitaire ]],axis=0)


def afficher():
    global produits
    for produit in produits :
        print(f"{produit[0]} | {produit[1]} Qte | {produit[2]} DH")


def mettre_a_jour_quantite():
    global produits

    nom_produit = input("Enter the name of product you want to update : ")
    exists = False
    index = 0
    for i in range(len(produits)):
        if produits[i][0].lower() == nom_produit.lower():
            index = i
            exists = True

    if(exists):
        new_qte = int(input("Enter the new qte : "))
        produits[index][1] = new_qte
        print("Updated")
    else:
        print("Product not exist")


def supprimer_produit():
    global produits

    nom_produit = input("Enter the name of produit you want to delete : ")

    exists = False
    index = 0

    for i in range(len(produits)):
        if produits[i][0].lower() == nom_produit.lower():
            exists = True
            index = i
        else:
            exists = False

    if(exists):
        produits = np.delete(produits,index,axis=0)
        print("deleted")
    else:
        print("Not exists")




