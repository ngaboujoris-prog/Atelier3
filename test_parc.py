from voiture import Voiture
from parc_voitures import ParcVoitures


def test_voiture():
    print("Test voiture")
    v = Voiture("AB123", "Toyota", "Camry", "Jean")
    print(v)


def test_parc():
    print("Test parc")
    parc = ParcVoitures("Mon parc")
    v1 = Voiture("AB123", "Toyota", "Camry", "Jean")
    v2 = Voiture("CD456", "Honda", "Civic", "Marie")

    parc.ajouter(v1)
    parc.ajouter(v2)
    parc.afficher()

    print("Recherche de AB123")
    trouve = parc.chercher("AB123")
    if trouve:
        print(trouve)

    parc.retirer("AB123")
    parc.afficher()


if __name__ == "__main__":
    test_voiture()
    test_parc()
