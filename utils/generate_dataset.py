# Script Python pour générer un fichier CSV réaliste des étudiants Akieni
import pandas as pd
import random
from datetime import datetime, timedelta

# Liste simulée d'étudiants avec leur discipline et module
etudiants = [
    ("Alice", "Data Science", "Python & DS"),
    ("Benoît", "Fullstack", "React Fullstack"),
    ("Chloé", "Data Science", "Python & DS"),
    ("David", "UX/UI", "UX Design"),
    ("Emmanuel", "Fullstack", "React Fullstack"),
    ("Farida", "Data Science", "Python & DS"),
    ("Grace", "UX/UI", "UX Design"),
    ("Hakim", "Fullstack", "React Fullstack")
]

# Création de données aléatoires pour chaque étudiant
data = []
for i, (nom, discipline, module) in enumerate(etudiants, start=1):
    total_cours = 12
    presences = random.randint(6, 12)         # Présences entre 6 et 12
    score = random.randint(60, 100)           # Score entre 60 et 100
    date = datetime.today() - timedelta(days=random.randint(0, 30))  # Date récente
    
    data.append({
        "ID": f"{i:03d}",
        "Nom": nom,
        "Module": module,
        "Discipline": discipline,
        "Présences": presences,
        "Total_Cours": total_cours,
        "Score": score,
        "Date": date.strftime("%Y-%m-%d")
    })

# Création d’un DataFrame pandas
df = pd.DataFrame(data)

# Sauvegarde en CSV dans le dossier /data
df.to_csv("data/students_data.csv", index=False)
print("✅ Fichier CSV généré avec succès dans /data/students_data.csv")