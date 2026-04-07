from voiture import Voiture
from parc import Parc


def test_parc():
    parc = Parc(3)

    voiture1 = Voiture("AB123", "Toyota", "Camry", "Jean")
    voiture2 = Voiture("CD456", "Honda", "Civic", "Marie")

    parc.entrerVoiture(voiture1)
    parc.entrerVoiture(voiture2)

    print("Places libres apres entree:", parc.calculerNbrPlacesLibres())

    parc.sortirVoiture("AB123")
    print("Places libres apres sortie:", parc.calculerNbrPlacesLibres())

    parc.sortirVoiture("ZZ999")


if __name__ == "__main__":
    test_parc()
