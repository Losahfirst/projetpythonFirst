import csv

# Définition des matières et de leurs coefficients
matieres = {
    "Français": 3,
    "Anglais": 2,
    "Physique": 4,
    "Mathématiques": 5,
    "Sport": 1
}

# Création du fichier CSV avec l'en-tête si le fichier n'existe pas
try:
    with open("bulletins_etudiants.csv", mode="x", newline="", encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        entete = ["Nom", "Prénom"] + list(matieres.keys()) + ["Moyenne", "Mention"]
        writer.writerow(entete)
except FileExistsError:
    pass  # Le fichier existe déjà, on ne le recrée pas

# Boucle principale : gestion de plusieurs étudiants

while True:
    print("\nSaisie d’un nouveau bulletin")
    nom = input("Nom de l'étudiant : ").strip().capitalize()
    prenom = input("Prénom de l'étudiant : ").strip().capitalize()

    notes = {}
    total_points = 0
    total_coeffs = 0

    # Saisie et validation des notes pour chaque matière
    for matiere, coef in matieres.items():
        while True:
            try:
                note = float(input(f"Note de {matiere} (/20) : "))
                if 0 <= note <= 20:
                    notes[matiere] = note
                    total_points += note * coef
                    total_coeffs += coef
                    break
                else:
                    print("La note doit être comprise entre 0 et 20.")
            except ValueError:
                print("Entrée invalide. Veuillez saisir un nombre.")

    # Calcul de la moyenne pondérée
    moyenne = total_points / total_coeffs

    # Détermination de la mention
    if moyenne >= 16:
        mention = "Très bien"
    elif moyenne >= 14:
        mention = "Bien"
    elif moyenne >= 12:
        mention = "Assez bien"
    elif moyenne >= 10:
        mention = "Passable"
    else:
        mention = "Insuffisant"

    # Affichage du bulletin
    print("\nBulletin de", prenom, nom)
    print("-" * 40)
    for matiere, note in notes.items():
        print(f"{matiere:<15} : {note}/20")
    print("-" * 40)
    print(f"Moyenne générale : {moyenne:.2f}/20")
    print(f"Mention          : {mention}")
    print("-" * 40)

    # Enregistrement des résultats dans le fichier CSV
    # Vérification de l'existence du fichier avant d'écrire
    with open("bulletins_etudiants.csv", mode="a", newline="", encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        ligne = [nom, prenom] + [notes[m] for m in matieres] + [round(moyenne, 2), mention]
        writer.writerow(ligne)

    # Demander si on souhaite ajouter un autre étudiant
    continuer = input("Voulez-vous ajouter un autre étudiant ? (o/n) : ").lower()
    if continuer != 'o':
        print("\nLes résultats ont été enregistrés dans 'bulletins_etudiants.csv'.")
        print("Fin du programme.")
        break