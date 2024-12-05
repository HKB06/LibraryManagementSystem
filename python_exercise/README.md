Library Management System (Python)
Bienvenue dans mon projet de gestion de bibliothèque ! Cette application est développée en Python et permet une gestion simplifiée des livres et des emprunts.

Configuration initiale
Assurez-vous d'avoir Python installé sur votre machine.

Installation des dépendances
Aucune dépendance externe requise.

Lancement du projet
```bash 
python library_system.py
```

Structure du projet
library_system.py : Le fichier principal contenant tout le code.
library_data.txt : Le fichier où les livres sont sauvegardés et chargés.
README.md : Ce fichier expliquant comment utiliser le projet.

Exemple de fichier library_data.txt
```bash 
1984,George Orwell,True
Le Petit Prince,Antoine de Saint-Exupéry,False
Harry Potter,J.K. Rowling,True
```

Utilisation de l'application
Menu principal :

```bash 
===== MENU DE LA BIBLIOTHÈQUE =====
1. Voir tous les livres
2. Ajouter un nouveau livre
3. Rechercher un livre
4. Emprunter un livre
5. Rendre un livre
6. Sauvegarder et quitter
```
Fonctionnalités principales :
Ajouter des livres à la bibliothèque.
Rechercher un livre par titre ou auteur.
Emprunter et retourner des livres (limite de 3 livres par étudiant).
Sauvegarder automatiquement les livres dans un fichier.