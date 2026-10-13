
import pandas as pd  # Pour construire et manipuler des tableaux
import numpy as np   # Pour générer des valeurs numériques aléatoires

# Fixer la graine aléatoire pour garantir la reproductibilité
np.random.seed(42)

n = 500  # Nombre de clients fictifs à générer

# Création du DataFrame avec les caractéristiques des clients (features)
data = pd.DataFrame({
    "age": np.random.randint(18, 70, n),
    "salaire": np.random.randint(1200, 8000, n),
    "abonnement": np.random.choice(
        ["Basique", "Standard", "Premium"], n
    ),
    "anciennete": np.random.randint(0, 15, n),
    "consommation": np.random.randint(0, 100, n)
})

# Création de la variable cible (target) : churn
# Un client est considéré à risque si :
# - sa consommation est inférieure à 30
# - son ancienneté est inférieure à 2 ans

data["churn"] = (
    (data["consommation"] < 30) &
    (data["anciennete"] < 2)
).astype(int)

# Sauvegarde des données dans un fichier CSV
data.to_csv("churn_data.csv", index=False)

# Affichage des 5 premières lignes
print(data.head())

# Affichage du taux de churn
print(f"Taux de churn : {data['churn'].mean():.1%}")
