import pandas as pd
import numpy as np

# 1. Chargement des données (Simulation)
# Dans un projet réel, on utiliserait : df = pd.read_csv('ventes.csv')
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', None],
    'Produit': ['Alimentaire', 'Technique', 'Technique', 'Logistique', 'Alimentaire'],
    'CA_FCFA': ['150 000', '200 000', '200 000', '50 000', '100 000'],
    'Cout_FCFA': [100000, 120000, 120000, 40000, 70000]
}
df = pd.DataFrame(data)

print("--- Données Brutes ---")
print(df.head())

# 2. Nettoyage des données
# Suppression des doublons
df = df.drop_duplicates()

# Gestion des valeurs manquantes (Suppression des lignes sans date)
df = df.dropna(subset=['Date'])

# Nettoyage des formats numériques (Enlever les espaces dans les chaînes et convertir en float)
df['CA_FCFA'] = df['CA_FCFA'].str.replace(' ', '').astype(float)

# Conversion de la colonne Date en format datetime
df['Date'] = pd.to_datetime(df['Date'])

# 3. Création de nouvelles colonnes (Feature Engineering)
# Calcul de la Marge
df['Marge_FCFA'] = df['CA_FCFA'] - df['Cout_FCFA']

# Extraction du mois pour l'analyse temporelle
df['Mois'] = df['Date'].dt.month_name()

# 4. Agrégation des résultats (KPIs)
resultats_categorie = df.groupby('Produit').agg({
    'CA_FCFA': 'sum',
    'Marge_FCFA': 'sum'
}).reset_index()

print("\n--- Données Nettoyées & KPIs ---")
print(resultats_categorie)

# 5. Exportation pour Power BI
# df.to_csv('ventes_clean.csv', index=False)
