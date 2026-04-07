class Voiture:
    def __init__(self, plaque, marque, modele, proprietaire):
        self.plaque = plaque
        self.marque = marque
        self.modele = modele
        self.proprietaire = proprietaire

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.plaque}) - {self.proprietaire}"
