"""
Module pour la gestion du parc de voitures.
"""

from voiture import Voiture


class ParcVoitures:
    """
    Classe représentant un parc de voitures.
    Gère l'ajout, la suppression et l'affichage des voitures.
    """

    def __init__(self, nom_parc, capacite_max=100):
        """
        Initialise le parc de voitures.

        Args:
            nom_parc (str): Nom du parc
            capacite_max (int): Capacité maximale du parc (default: 100)
        """
        self.nom_parc = nom_parc
        self.capacite_max = capacite_max
        self.voitures = []

    def ajouter_voiture(self, voiture):
        """
        Ajoute une voiture au parc.

        Args:
            voiture (Voiture): L'objet voiture à ajouter

        Returns:
            bool: True si l'ajout réussit, False sinon
        """
        if len(self.voitures) >= self.capacite_max:
            print(f"Erreur: Le parc {self.nom_parc} est plein!")
            return False

        # Vérifier que la plaque n'existe pas déjà
        for v in self.voitures:
            if v.plaque_immatriculation == voiture.plaque_immatriculation:
                print(f"Erreur: La plaque {voiture.plaque_immatriculation} existe déjà!")
                return False

        self.voitures.append(voiture)
        print(f"Voiture {voiture.plaque_immatriculation} ajoutée au parc {self.nom_parc}.")
        return True

    def retirer_voiture(self, plaque_immatriculation):
        """
        Retire une voiture du parc.

        Args:
            plaque_immatriculation (str): Plaque d'immatriculation de la voiture à retirer

        Returns:
            bool: True si le retrait réussit, False sinon
        """
        for voiture in self.voitures:
            if voiture.plaque_immatriculation == plaque_immatriculation:
                self.voitures.remove(voiture)
                print(f"Voiture {plaque_immatriculation} retirée du parc.")
                return True

        print(f"Erreur: Voiture avec plaque {plaque_immatriculation} non trouvée!")
        return False

    def chercher_voiture(self, plaque_immatriculation):
        """
        Cherche une voiture par sa plaque d'immatriculation.

        Args:
            plaque_immatriculation (str): Plaque à chercher

        Returns:
            Voiture: L'objet voiture trouvé, ou None
        """
        for voiture in self.voitures:
            if voiture.plaque_immatriculation == plaque_immatriculation:
                return voiture
        return None

    def afficher_toutes_voitures(self):
        """Affiche toutes les voitures du parc."""
        if not self.voitures:
            print(f"Le parc {self.nom_parc} est vide.")
            return

        print(f"\n--- Parc: {self.nom_parc} ---")
        for i, voiture in enumerate(self.voitures, 1):
            print(f"{i}. {voiture}")
        print()

    def get_nombre_voitures(self):
        """Retourne le nombre de voitures dans le parc."""
        return len(self.voitures)

    def get_places_disponibles(self):
        """Retourne le nombre de places disponibles."""
        return self.capacite_max - len(self.voitures)

    def __str__(self):
        """Affiche les informations du parc."""
        return (f"Parc: {self.nom_parc} | "
                f"Voitures: {self.get_nombre_voitures()}/{self.capacite_max} | "
                f"Places libres: {self.get_places_disponibles()}")
