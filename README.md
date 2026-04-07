# POO-Atelier 3 : Gestion d’un parc de voitures

## Description de l’atelier
Cet atelier porte sur la programmation orientée objet en Python. L'objectif est de développer un système complet de gestion d'un parc de voitures, en utilisant les classes pour représenter les voitures et le parc, ainsi que leurs interactions.

## Structure du projet

### Fichiers principaux
- **voiture.py** : Classe `Voiture` représentant une voiture avec ses attributs
- **parc_voitures.py** : Classe `ParcVoitures` gérant un ensemble de voitures
- **main.py** : Programme principal avec menu interactif
- **test_parc.py** : Tests unitaires du système
- **.gitignore** : Configuration Git pour ignorer les fichiers temporaires
- **README.md** : Documentation du projet

### Classes principales

#### Classe Voiture
Représente une voiture avec les attributs:
- `plaque_immatriculation` : Identifiant unique
- `marque` : Marque du véhicule
- `modele` : Modèle du véhicule
- `proprietaire` : Propriétaire du véhicule

Méthodes:
- `__str__()` : Affichage lisible
- `__repr__()` : Représentation pour le débogage

#### Classe ParcVoitures
Gère un parc de voitures avec:
- `nom_parc` : Nom du parc
- `capacite_max` : Capacité maximale (défaut: 100)
- `voitures` : Liste des voitures

Méthodes principales:
- `ajouter_voiture(voiture)` : Ajouter une voiture
- `retirer_voiture(plaque)` : Retirer une voiture
- `chercher_voiture(plaque)` : Chercher une voiture par plaque
- `afficher_toutes_voitures()` : Afficher toutes les voitures
- `get_nombre_voitures()` : Retourner le nombre de voitures
- `get_places_disponibles()` : Retourner les places libres

## Utilisation

### Lancer le programme principal
```bash
python main.py
```

Le menu propose:
1. Ajouter une voiture
2. Retirer une voiture
3. Afficher toutes les voitures
4. Chercher une voiture
5. Afficher les informations du parc
6. Quitter

### Exécuter les tests
```bash
python test_parc.py
```

## Conventions respectées
- Classes en CamelCase : `Voiture`, `ParcVoitures`
- Fonctions/méthodes en snake_case : `ajouter_voiture`, `chercher_voiture`
- Variables en snake_case : `plaque_immatriculation`, `proprietaire`
- Docstrings pour toutes les classes et méthodes publiques
- Commentaires explicatifs pour le code complexe

## Informations de l'auteur
- Nom: Ngabou Joris
- Prénom: Joris
- Date: Avril 2026

## Historique des commits
1. Premier commit : README.md
2. Étape 1 : Classe Voiture avec attributs et méthodes
3. Étape 2 : Classe ParcVoitures avec gestion des voitures
4. Étape 3 : Programme principal avec menu interactif
5. Étape 4 : Tests de fonctionnalité
6. Étape 5 : Fichier .gitignore
7. Étape 6 : Documentation complète du README

## Fonctionnalités implémentées

### Gestion des voitures
- ✅ Création de voitures avec attributs
- ✅ Ajout de voitures au parc
- ✅ Suppression de voitures du parc
- ✅ Recherche de voitures par plaque

### Gestion du parc
- ✅ Vérification de la capacité maximale
- ✅ Détection des doublons (plaques identiques)
- ✅ Affichage de l'état du parc
- ✅ Statistiques (nombre de voitures, places libres)

### Interface utilisateur
- ✅ Menu interactif
- ✅ Messages d'erreur clairs
- ✅ Confirmations d'actions

### Tests
- ✅ Tests de la classe Voiture
- ✅ Tests de la classe ParcVoitures
- ✅ Tests de gestion de capacité
- ✅ Tests de détection de doublons