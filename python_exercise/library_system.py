print("Bienvenue dans le système de gestion de bibliothèque.")

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def __str__(self):
        return f"{self.titre} par {self.auteur} - {'Disponible' if self.disponible else 'Emprunté'}"

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, titre, auteur):
        livre = Livre(titre, auteur)
        self.livres.append(livre)
        print(f"Le livre '{titre}' par {auteur} a été ajouté à la bibliothèque.")

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            print("Liste des livres dans la bibliothèque :")
            for livre in self.livres:
                print(f" - {livre}")

    def rechercher_livre(self, recherche):
        resultats = [livre for livre in self.livres if recherche.lower() in livre.titre.lower() or recherche.lower() in livre.auteur.lower()]
        if resultats:
            print("Livres trouvés :")
            for livre in resultats:
                print(f" - {livre}")
        else:
            print("Aucun livre trouvé pour cette recherche.")

    def charger_livres(self, chemin_fichier):
        try:
            with open(chemin_fichier, "r", encoding="utf-8") as fichier:
                for ligne in fichier:
                    titre, auteur, disponible = ligne.strip().split(",")
                    livre = Livre(titre, auteur)
                    livre.disponible = disponible == "True"
                    self.livres.append(livre)
            print(f"Les livres ont été chargés depuis {chemin_fichier}.")
        except FileNotFoundError:
            print(f"Le fichier {chemin_fichier} n'existe pas encore. Aucun livre chargé.")

    def sauvegarder_livres(self, chemin_fichier):
        with open(chemin_fichier, "w", encoding="utf-8") as fichier:
            for livre in self.livres:
                ligne = f"{livre.titre},{livre.auteur},{livre.disponible}\n"
                fichier.write(ligne)
        print(f"Les livres ont été sauvegardés dans {chemin_fichier}.")


class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []

    def emprunter_livre(self, titre, bibliotheque):
        if len(self.livres_empruntes) >= 3:
            print(f"{self.nom} ne peut pas emprunter plus de 3 livres.")
            return

        for livre in bibliotheque.livres:
            if livre.titre == titre:
                if livre.disponible:
                    livre.disponible = False
                    self.livres_empruntes.append(livre)
                    print(f"{self.nom} a emprunté le livre '{titre}'.")
                    return
                else:
                    print(f"Le livre '{titre}' est déjà emprunté.")
                    return
        print(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")

    def rendre_livre(self, titre, bibliotheque):
        for livre in self.livres_empruntes:
            if livre.titre == titre:
                livre.disponible = True
                self.livres_empruntes.remove(livre)
                print(f"{self.nom} a rendu le livre '{titre}'.")
                return
        print(f"{self.nom} n'a pas emprunté le livre '{titre}'.")



if __name__ == "__main__":
    
    biblio = Bibliotheque()
    biblio.ajouter_livre("1984", "George Orwell")
    biblio.ajouter_livre("Le Petit Prince", "Antoine de Saint-Exupéry")

    
    biblio.afficher_livres()

    print("\nRecherche des livres contenant '1984' :")
    biblio.rechercher_livre("1984")

    
    etudiant = Etudiant("Alice")
    etudiant.emprunter_livre("1984", biblio)

    
    print("\nLivres après emprunt :")
    biblio.afficher_livres()

    etudiant.rendre_livre("1984", biblio)

    
    print("\nLivres après retour :")
    biblio.afficher_livres()

def run_library_system():
    
    biblio = Bibliotheque()
    biblio.charger_livres("library_data.txt")

    
    while True:
        print("\n===== MENU DE LA BIBLIOTHÈQUE =====")
        print("1. Voir tous les livres")
        print("2. Ajouter un nouveau livre")
        print("3. Rechercher un livre")
        print("4. Emprunter un livre")
        print("5. Rendre un livre")
        print("6. Sauvegarder et quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == "1":  
            biblio.afficher_livres()
        
        elif choix == "2":  
            titre = input("Titre du livre : ")
            auteur = input("Auteur du livre : ")
            biblio.ajouter_livre(titre, auteur)
        
        elif choix == "3":  
            recherche = input("Entrez un titre ou un auteur à rechercher : ")
            biblio.rechercher_livre(recherche)
        
        elif choix == "4":  
            etudiant_nom = input("Nom de l'étudiant : ")
            titre = input("Titre du livre à emprunter : ")
            etudiant = Etudiant(etudiant_nom)
            etudiant.emprunter_livre(titre, biblio)
        
        elif choix == "5":  
            etudiant_nom = input("Nom de l'étudiant : ")
            titre = input("Titre du livre à rendre : ")
            etudiant = Etudiant(etudiant_nom)
            etudiant.rendre_livre(titre, biblio)
        
        elif choix == "6":  
            biblio.sauvegarder_livres("library_data.txt")
            print("Les données de la bibliothèque ont été sauvegardées. Au revoir !")
            break
        
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    run_library_system()