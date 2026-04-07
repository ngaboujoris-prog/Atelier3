from voiture import Voiture


class ParcVoitures:
    def __init__(self, nom):
        self.nom = nom
        self.voitures = []

    def ajouter(self, voiture):
        for v in self.voitures:
            if v.plaque == voiture.plaque:
                print("Cette plaque existe déjà.")
                return False

        self.voitures.append(voiture)
        print("Voiture ajoutée.")
        return True

    def retirer(self, plaque):
        for voiture in self.voitures:
            if voiture.plaque == plaque:
                self.voitures.remove(voiture)
                print("Voiture retirée.")
                return True

        print("Voiture non trouvée.")
        return False

    def chercher(self, plaque):
        for voiture in self.voitures:
            if voiture.plaque == plaque:
                return voiture
        return None

    def afficher(self):
        if not self.voitures:
            print("Le parc est vide.")
            return

        print(f"Parc {self.nom}:")
        for voiture in self.voitures:
            print("-", voiture)

    def nombre(self):
        return len(self.voitures)
