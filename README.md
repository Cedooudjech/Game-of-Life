# Conway's Game-of-Life

### Illustration : Gosper's glider gun

![Gosper's glider gun (animation du Jeu de la Vie)](https://upload.wikimedia.org/wikipedia/commons/7/7a/Gospers_glider_gun.gif)

## Objectif

Réaliser une simulation du Jeu de la Vie (Conway) en Python.  

## Introduction

Le Jeu de la Vie est un automate cellulaire où une grille 2D évolue selon des règles simples basées sur les voisins de chaque cellule. Ce projet consiste à implémenter la logique, la mise à jour des générations et une boucle d'affichage.

## Règles du jeu
- Grille 2D (ici on commence par une grille 7x7).
- Chaque cellule vaut 0 (morte) ou 1 (vivante).
- Une cellule a 8 voisins (horizontaux, verticaux, diagonaux).
- À chaque itération :
    - Une cellule morte avec exactement 3 voisins vivants devient vivante (naissance).
    - Une cellule vivante avec 2 ou 3 voisins vivants reste vivante ; sinon elle meurt.

## Fonctionnalités attendues
- Utiliser numpy pour représenter la grille (par ex. frame = numpy.array(...), taille 7x7).
- Implémenter le zero-padding (numpy.pad) pour gérer les bords.
- Fonction compute_number_neighbors(paded_frame, i, j) → nombre de voisins vivants.
- Fonction compute_next_frame(frame) → calcule et renvoie la frame suivante selon les règles.
- Boucle principale qui affiche les frames successives (mode pas-à-pas et/ou automatique).
- Arrêt propre (Ctrl+C) et messages clairs pour début/fin de simulation.
- Validation des dimensions et des valeurs de la grille.

## Installation
Prérequis :
- Python 3.8+
- numpy

Installation rapide :
- Cloner le dépôt
- (Optionnel) créer un environnement virtuel :
    - python -m venv venv
    - venv\Scripts\activate (Windows) ou source venv/bin/activate (Unix)
- Installer les dépendances :
    - pip install -r requirements.txt

## Exécution
- Lancer la version terminal :
    - python main.py 

Exemple d'utilisation minimale (fichier main.py) :
- Définir frame (7x7) avec numpy.
- Appeler compute_next_frame dans une boucle et afficher la frame.

## Licence & Auteurs
- Projet pédagogique de programmation Python.  
- Contributeur principal : https://github.com/Cedooudjech

Bon développement et amusez-vous bien en implémentant le Jeu de la Vie !
