
from data import produits
import numpy as np




def supprimer_produit(nom):
    global produits
    for i in range(len(produits)):
        if produits[i][0].upper() == nom.upper():
            produits = np.delete(produits, i, axis=0)
            print("le produit est supprimer")
            break
        else:
            print("le nom de produit n'exist pas")


def mettre_a_jour(nom):
    global produits
    for i in range(len(produits)):
        if produits[i][0].upper() == nom.upper():
            x = int(input("entre nouvel quantité: "))
            produits[i][1]=x
            print(f"mettre a jour la quantité de {produits[i][0]}")
            break
        else:
            print("le nom qui vous entrez n'est pas exist")








