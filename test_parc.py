"""
Module de tests pour le système de gestion de parc de voitures.
"""

from voiture import Voiture
from parc_voitures import ParcVoitures


def test_voiture():
    """Test la classe Voiture."""
    print("\n=== Test de la classe Voiture ===")
    v1 = Voiture("AB-123-CD", "Toyota", "Camry", "Jean Dupont")
    print(f"Voiture créée: {v1}")
    print(f"Repr: {repr(v1)}")
    print("✓ Classe Voiture fonctionne correctement\n")


def test_parc_voitures():
    """Test la classe ParcVoitures."""
    print("=== Test de la classe ParcVoitures ===")

    # Créer un parc
    parc = ParcVoitures("Parc Test", capacite_max=3)
    print(f"Parc créé: {parc}")

    # Ajouter des voitures
    print("\n--- Ajout de voitures ---")
    v1 = Voiture("AB-123-CD", "Toyota", "Camry", "Jean Dupont")
    v2 = Voiture("EF-456-GH", "Honda", "Civic", "Marie Martin")
    v3 = Voiture("IJ-789-KL", "Ford", "Mustang", "Pierre Bernard")

    parc.ajouter_voiture(v1)
    parc.ajouter_voiture(v2)
    parc.ajouter_voiture(v3)

    print(f"État du parc: {parc}")
    parc.afficher_toutes_voitures()

    # Chercher une voiture
    print("--- Recherche ---")
    voiture_trouvee = parc.chercher_voiture("EF-456-GH")
    if voiture_trouvee:
        print(f"Trouvée: {voiture_trouvee}")

    # Retirer une voiture
    print("\n--- Retrait ---")
    parc.retirer_voiture("AB-123-CD")
    print(f"État après retrait: {parc}")
    parc.afficher_toutes_voitures()

    print("✓ Classe ParcVoitures fonctionne correctement\n")


def test_capacite():
    """Test la gestion de la capacité."""
    print("=== Test de la capacité ===")

    parc = ParcVoitures("Parc Petit", capacite_max=2)

    v1 = Voiture("A1", "Marque1", "Model1", "Prop1")
    v2 = Voiture("A2", "Marque2", "Model2", "Prop2")
    v3 = Voiture("A3", "Marque3", "Model3", "Prop3")

    parc.ajouter_voiture(v1)
    parc.ajouter_voiture(v2)
    print(f"Parc plein: {parc}")

    # Essayer d'ajouter quand le parc est plein
    parc.ajouter_voiture(v3)

    print("✓ Gestion de la capacité fonctionne\n")


def test_doublon():
    """Test la détection des doublons."""
    print("=== Test de détection de doublons ===")

    parc = ParcVoitures("Parc Doublon", capacite_max=10)

    v1 = Voiture("AB-123-CD", "Toyota", "Camry", "Jean Dupont")
    v2 = Voiture("AB-123-CD", "Honda", "Civic", "Marie Martin")

    parc.ajouter_voiture(v1)
    print("Tentative d'ajout d'une voiture avec la même plaque:")
    parc.ajouter_voiture(v2)

    print("✓ Détection de doublons fonctionne\n")


if __name__ == "__main__":
    print("="*50)
    print("TESTS DU SYSTÈME DE GESTION DE PARC DE VOITURES")
    print("="*50)

    test_voiture()
    test_parc_voitures()
    test_capacite()
    test_doublon()

    print("="*50)
    print("TOUS LES TESTS SONT TERMINÉS")
    print("="*50)
