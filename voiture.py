"""
Module pour la gestion des voitures.
"""


class Voiture:
    """
    Classe représentant une voiture dans le parc.
    """

    def __init__(self, plaque_immatriculation, marque, modele, proprietaire):
        """
        Initialise une voiture avec ses attributs.

        Args:
            plaque_immatriculation (str): Plaque d'immatriculation unique
            marque (str): Marque de la voiture
            modele (str): Modèle de la voiture
            proprietaire (str): Nom du propriétaire
        """
        self.plaque_immatriculation = plaque_immatriculation
        self.marque = marque
        self.modele = modele
        self.proprietaire = proprietaire

    def __str__(self):
        """Retourne une représentation textuelle de la voiture."""
        return (f"Voiture: {self.marque} {self.modele} "
                f"({self.plaque_immatriculation}) - Propriétaire: {self.proprietaire}")

    def __repr__(self):
        """Retourne une représentation pour le débogage."""
        return f"Voiture('{self.plaque_immatriculation}', '{self.marque}', '{self.modele}', '{self.proprietaire}')"
