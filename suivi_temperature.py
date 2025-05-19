# Suivi de la température quotidienne
import csv
import matplotlib.pyplot as plt



def lire_fichier_csv(nom_fichier):

    # Fonction pour lire un fichier CSV contenant des données de température
   
    jours = []
    temperatures = []
    
    # Vérifier si le fichier existe et est accessible
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            lecteur = csv.reader(fichier)
            # Ignorer l'en-tête
            next(lecteur)
            # Lire les données
            for ligne in lecteur:
                jours.append(ligne[0])
                temperatures.append(float(ligne[1]))
        return jours, temperatures
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
        return [], []


def calculer_statistiques(temperatures):
   

    if not temperatures:
        return {"moyenne": 0, "min": 0, "max": 0}
    
    moyenne = sum(temperatures) / len(temperatures)
    minimum = min(temperatures)
    maximum = max(temperatures)
    
    return {
        "moyenne": round(moyenne, 2),
        "min": minimum,
        "max": maximum
    }

def detecter_temperatures_critiques(jours, temperatures, seuil=30):
    
    jours_critiques = []
    
    for i in range(len(jours)):
        if temperatures[i] > seuil:
            jours_critiques.append((jours[i], temperatures[i]))
    
    return jours_critiques

def generer_graphique(jours, temperatures, seuil=30):
    
    plt.figure(figsize=(10, 6))
    
    # Tracer les données de température
    plt.plot(jours, temperatures, marker='o', linestyle='-', color='blue', linewidth=2)
    
    # Ajouter une ligne pour le seuil critique
    plt.axhline(y=seuil, color='red', linestyle='--', label=f'Seuil critique ({seuil}°C)')
    
    # Personnaliser le graphique
    plt.title('Évolution des températures', fontsize=16)
    plt.xlabel('Jour', fontsize=12)
    plt.ylabel('Température (°C)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Ajuster la rotation des étiquettes si nécessaire
    plt.xticks(rotation=45 if len(jours) > 7 else 0)
    
    plt.tight_layout()
    plt.savefig('graphique_temperatures.png')
    plt.show()

def main():
    # Nom du fichier CSV contenant les données de température
    # Assurez-vous que le fichier CSV est dans le même répertoire que ce script
    nom_fichier = "temperatures.csv"
    
    # Lire les données du fichier CSV
    jours, temperatures = lire_fichier_csv(nom_fichier)
    
    if not jours or not temperatures:
        print("Aucune donnée disponible. Vérifiez le fichier CSV.")
        return
    
    # Afficher les données lues
    print("\n--- DONNÉES DE TEMPÉRATURE ---")
    for i in range(len(jours)):
        print(f"{jours[i]}: {temperatures[i]}°C")
    
    # Calculer et afficher les statistiques
    stats = calculer_statistiques(temperatures)
    print("\n--- STATISTIQUES ---")
    print(f"Température moyenne: {stats['moyenne']}°C")
    print(f"Température minimale: {stats['min']}°C")
    print(f"Température maximale: {stats['max']}°C")
    
    # Détecter et afficher les températures critiques
    jours_critiques = detecter_temperatures_critiques(jours, temperatures)
    print("\n--- ALERTES TEMPÉRATURE CRITIQUE ---")
    if jours_critiques:
        print(f"Températures dépassant 30°C détectées les jours suivants:")
        for jour, temp in jours_critiques:
            print(f"- {jour}: {temp}°C")
    else:
        print("Aucune température critique détectée.")
    
    # Générer le graphique
    print("\nGénération du graphique...")
    generer_graphique(jours, temperatures)
    print("Graphique généré et sauvegardé comme 'graphique_temperatures.png'")

if __name__ == "__main__":
    main()