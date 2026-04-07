"""
Programme principal pour la gestion du parc de voitures.
"""

from voiture import Voiture
from parc_voitures import ParcVoitures


def afficher_menu():
    """Affiche le menu principal."""
    print("\n" + "="*50)
    print("GESTION DU PARC DE VOITURES")
    print("="*50)
    print("1. Ajouter une voiture")
    print("2. Retirer une voiture")
    print("3. Afficher toutes les voitures")
    print("4. Chercher une voiture")
    print("5. Afficher les informations du parc")
    print("6. Quitter")
    print("="*50)


def ajouter_voiture(parc):
    """Fonction pour ajouter une voiture."""
    print("\n--- Ajout d'une voiture ---")
    plaque = input("Plaque d'immatriculation: ").strip().upper()
    marque = input("Marque: ").strip()
    modele = input("Modèle: ").strip()
    proprietaire = input("Propriétaire: ").strip()

    voiture = Voiture(plaque, marque, modele, proprietaire)
    parc.ajouter_voiture(voiture)


def retirer_voiture(parc):
    """Fonction pour retirer une voiture."""
    print("\n--- Retrait d'une voiture ---")
    plaque = input("Plaque d'immatriculation à retirer: ").strip().upper()
    parc.retirer_voiture(plaque)


def chercher_voiture(parc):
    """Fonction pour chercher une voiture."""
    print("\n--- Recherche d'une voiture ---")
    plaque = input("Plaque d'immatriculation: ").strip().upper()
    voiture = parc.chercher_voiture(plaque)

    if voiture:
        print(f"Voiture trouvée: {voiture}")
    else:
        print(f"Aucune voiture trouvée avec la plaque {plaque}.")


def main():
    """Fonction principale."""
    # Créer un parc de voitures
    parc = ParcVoitures("Parc Principal", capacite_max=20)

    # Ajouter quelques voitures de démonstration
    parc.ajouter_voiture(Voiture("AB-123-CD", "Toyota", "Camry", "Jean Dupont"))
    parc.ajouter_voiture(Voiture("EF-456-GH", "Honda", "Civic", "Marie Martin"))
    parc.ajouter_voiture(Voiture("IJ-789-KL", "Ford", "Mustang", "Pierre Bernard"))

    while True:
        afficher_menu()
        choix = input("Choisir une option (1-6): ").strip()

        if choix == "1":
            ajouter_voiture(parc)
        elif choix == "2":
            retirer_voiture(parc)
        elif choix == "3":
            parc.afficher_toutes_voitures()
        elif choix == "4":
            chercher_voiture(parc)
        elif choix == "5":
            print(f"\n{parc}")
            print(f"Détails: {parc.get_nombre_voitures()} voitures, "
                  f"{parc.get_places_disponibles()} places libres")
        elif choix == "6":
            print("\nAu revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
