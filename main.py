from voiture import Voiture
from parc import Parc


def main():
    parc = Parc(3)

    voiture1 = Voiture("AB123", "Toyota", "Camry", "Jean")
    voiture2 = Voiture("CD456", "Honda", "Civic", "Marie")
    voiture3 = Voiture("EF789", "Renault", "Clio", "Paul")
    voiture4 = Voiture("GH012", "Peugeot", "208", "Lucie")

    parc.entrerVoiture(voiture1)
    parc.entrerVoiture(voiture2)
    parc.entrerVoiture(voiture3)
    parc.entrerVoiture(voiture4)

    parc.afficherVoitures()

    parc.sortirVoiture("CD456")

    parc.afficherVoitures()
    print("Nombre de places libres:", parc.calculerNbrPlacesLibres())


if __name__ == "__main__":
    main()
