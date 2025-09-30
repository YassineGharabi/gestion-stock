
from data import produits
import numpy as np

def somme(mul):

    total = 0
    for x in mul:
        total = total + x
    return total

def multiplication(produits):
    mul = []
    for produit in produits:
        mul.append( float(produit[1]) * float(produit[2]))
    return mul

def total_stock():

    return somme(multiplication(produits))



def prix_moyen():
    n = len(produits)
    return np.sum(produits[:, 2].astype(float))/n



def prix_min():
    return np.min(produits[:, 2].astype(float))

def prix_max():
    return np.max(produits[:, 2].astype(float))


