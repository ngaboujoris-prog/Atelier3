from voiture import Voiture


class Parc:
    def __init__(self, capacite):
        self.capacite = capacite
        self.voitures = []

    def entrerVoiture(self, voiture):
        if self.calculerNbrPlacesLibres() == 0:
            print("Le parc est plein.")
            return False

        for v in self.voitures:
            if v.plaque == voiture.plaque:
                print("Cette voiture est deja dans le parc.")
                return False

        self.voitures.append(voiture)
        print("Voiture entree dans le parc.")
        print("Places libres:", self.calculerNbrPlacesLibres())
        return True

    def sortirVoiture(self, plaque):
        for voiture in self.voitures:
            if voiture.plaque == plaque:
                self.voitures.remove(voiture)
                print("Voiture retiree du parc.")
                print("Places libres:", self.calculerNbrPlacesLibres())
                return True

        print("La voiture n'est pas dans le parc.")
        return False

    def calculerNbrPlacesLibres(self):
        return self.capacite - len(self.voitures)

    def afficherVoitures(self):
        if not self.voitures:
            print("Aucune voiture dans le parc.")
            return

        print("Voitures dans le parc:")
        for voiture in self.voitures:
            print("-", voiture)
