import pandas as pd

# charger le fichier extracted_data_04_until_08.csv en utilisant pandas
extracted_rows = pd.read_csv("to_be_insert_inmarch.csv")

# convertir la colonne date en type datetime pour pouvoir utiliser les fonctions de manipulation de date
extracted_rows['date'] = pd.to_datetime(extracted_rows['date'])

extracted_rows['date'] = extracted_rows['date'] + pd.Timedelta(days=4)

extracted_rows['cumul'] = 0

# enregistrer le fichier february_data.csv avec les nouvelles lignes
extracted_rows.to_csv("to_be_insert_inmarch_final.csv", index=False)

print(extracted_rows)