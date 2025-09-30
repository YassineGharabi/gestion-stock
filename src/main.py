
from stock import ajouter_produit , afficher


def menu():

    choix = 0


    while choix != 4 :

        print("choisir operation")
        print("1 - ajouter : ")
        print("2 - afficher : ")
        print("3 - quit : ")

        choix = int(input("entrer choix :"))

        if choix == 1 :
            ajouter_produit()
        elif choix == 2 :
            afficher()


menu()

