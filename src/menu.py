from stock import ajouter_produit , afficher , mettre_a_jour_quantite , supprimer_produit


def menu():

    choix = 0


    while choix != 5 :

        print("choisir operation")
        print("1 - ajouter : ")
        print("2 - afficher : ")
        print("3 - mettre a jour : ")
        print("4 - supprimer : ")
        print("5 - quit : ")

        choix = int(input("entrer choix :"))

        if choix == 1 :
            ajouter_produit()
        elif choix == 2 :
            afficher()
        elif choix == 3:
            mettre_a_jour_quantite()
        elif choix == 4:
            supprimer_produit()



