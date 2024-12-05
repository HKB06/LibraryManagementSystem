# SQL Exercise - University Enrollment Management System

## Objectif
Ce projet implémente un système de gestion des inscriptions universitaires en utilisant un modèle relationnel.

## Structure de la base de données
- **Students** : Contient les détails des étudiants.
- **Courses** : Contient les informations sur les cours.
- **Enrollments** : Lie les étudiants aux cours.

## Fichiers
- `schema.sql` : Définitions des tables et des triggers pour gérer les contraintes.
- `data.sql` : Données d'exemple (5 étudiants, 4 cours, 8 inscriptions).
- `queries.sql` : Requêtes SQL pour répondre aux tâches du projet.
- `README.md` : Documentation du projet.
- `SQL_EXERCISE.session.sql` : Fichier généré automatiquement par SQL Tools pour conserver les sessions et le contexte des requêtes exécutées.

## Utilisation de SQL Tools
### Pourquoi SQL Tools ?
SQL Tools est une extension intégrée à Visual Studio Code qui permet :
- De se connecter facilement à une base de données MySQL/MariaDB.
- D'exécuter des requêtes SQL directement depuis l'éditeur.
- De visualiser les résultats dans un environnement convivial.

### Connexion à la base de données
1. **Configurer SQL Tools** :
   - Accédez au panneau **SQL Tools** dans VS Code.
   - Ajoutez une connexion avec les paramètres suivants :
     - **Database** : `SQL_EXERCISE`.
     - **Host** : `localhost`.
     - **Port** : `3306` 
     - **Username** : `root`.
     - **Password** :
   
2. **Exécuter des fichiers SQL** :
   - Ouvrez un fichier SQL dans l'éditeur (par exemple, `schema.sql`).
   - Faites un clic droit et sélectionnez **Run Query** pour exécuter tout le fichier ou une sélection spécifique.

3. **Résultats des requêtes** :
   - Les résultats des requêtes sont affichés directement dans un panneau sous VS Code.

### Fichiers supplémentaires générés
- **`SQL_EXERCISE.session.sql`** :
  Ce fichier est généré par SQL Tools et contient des métadonnées liées à la session. Il peut être ignoré ou utilisé pour conserver un historique des requêtes exécutées.

## Requêtes incluses
1. Liste des étudiants et des cours auxquels ils sont inscrits.
2. Étudiants sans inscription.
3. Nombre d’étudiants inscrits par cours.
4. Cours dépassant la moitié de leur capacité.
5. Étudiant inscrit dans le maximum de cours.
6. Total des crédits par étudiant.
7. Cours sans inscription.

## Instructions
1. **Créer la structure de la base de données** :
   - Exécutez `schema.sql` pour créer les tables et les triggers.

2. **Insérer des données** :
   - Exécutez `data.sql` pour remplir les tables avec des données d'exemple.

3. **Exécuter les requêtes** :
   - Lancez les requêtes dans `queries.sql` pour valider le système.


## Notes supplémentaires
- **Validation des triggers** : Testez les triggers en tentant d'inscrire des étudiants dans des cours pleins ou au-delà de la limite de 5 cours.
- **Dépannage** : Si les triggers ne fonctionnent pas, activez cette commande dans votre environnement SQL :
  ```sql
  
```bash 
SET GLOBAL log_bin_trust_function_creators = 1;
```