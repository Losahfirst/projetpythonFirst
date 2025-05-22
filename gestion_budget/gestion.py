def repartion_budget():
    
    salaire = float(input("Entrez votre salaire: "))
    budget = {
        "loyer/ Nouriture / Transport": 0.5 * salaire,
        "epargne": 0.2 * salaire,
        "invest": 0.2 * salaire,
        "loisir": 0.1 * salaire,
    }
    print("Voici la repartion de votre budget:")
    for key, value in budget.items():
        print(f"{key}: {value:.1f} FCFA")
   
    state = True

    return state


def analyse_budget():
    
    salaire = float(input("Quel est votre salaire ? "))
    loyer = float(input("Entrez le montant de votre loyer/ Nouriture / Transport: "))
    epargne = float(input("Entrez le montant de votre Epargne: "))
    invest = float(input("Entrez le montant de votre invest: "))
    loisirs = float(input("Entrez le montant de vos loisir/ action sociale: "))
    

    if (loyer + epargne + invest + loisirs) > salaire:
            print("Il est conseillé de ne pas depenser plus que votre budget total.")
            print("Vous risquez de ne pas realiser vos projets et d'etre super endetter\n")
    else:
            print("Votre budget est bien repartie.")
            print("Vous etes sur la bonne voie vers la reussite\n")
    
    
        
    return True


print("Bienvenue dans le programme de gestion de budget.\n")

while True:
    print("1. Repartition de budget")
    print("2. Analyse de budget")
    print("3. Quitter")
    
    choix = input("Choisissez une option (1-3): ")
    
    if choix == "1":
        repartion_budget()
    elif choix == "2":
        analyse_budget()
    elif choix == "3":
        print("Merci d'avoir utilisé le programme de gestion de budget.")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")