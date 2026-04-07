from voiture import Voiture
from parc_voitures import ParcVoitures


def afficher_menu():
    print("\n1. Ajouter une voiture")
    print("2. Retirer une voiture")
    print("3. Afficher toutes les voitures")
    print("4. Chercher une voiture")
    print("5. Voir le nombre de voitures")
    print("6. Quitter")


def ajouter_voiture(parc):
    plaque = input("Plaque: ").strip()
    marque = input("Marque: ").strip()
    modele = input("Modele: ").strip()
    proprietaire = input("Proprietaire: ").strip()
    voiture = Voiture(plaque, marque, modele, proprietaire)
    parc.ajouter(voiture)


def retirer_voiture(parc):
    plaque = input("Plaque a retirer: ").strip()
    parc.retirer(plaque)


def chercher_voiture(parc):
    plaque = input("Plaque a chercher: ").strip()
    voiture = parc.chercher(plaque)
    if voiture:
        print("Voiture trouvee:", voiture)
    else:
        print("Aucune voiture trouvee.")


def main():
    parc = ParcVoitures("Mon parc")

    while True:
        afficher_menu()
        choix = input("Choix: ").strip()

        if choix == "1":
            ajouter_voiture(parc)
        elif choix == "2":
            retirer_voiture(parc)
        elif choix == "3":
            parc.afficher()
        elif choix == "4":
            chercher_voiture(parc)
        elif choix == "5":
            print("Nombre de voitures:", parc.nombre())
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
