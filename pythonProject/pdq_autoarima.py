import pandas as pd
from pmdarima.arima import auto_arima

# Chargement des données à partir du fichier CSV
data = pd.read_csv('february_data_with_insert1-et-2.csv')

# Sélectionner la colonne de données à utiliser pour le modèle
train_data = data.iloc[:int(0.8*len(data))]
train_data = train_data["debit"]

# Trouver les meilleures valeurs de p, d et q en utilisant la fonction auto_arima
stepwise_fit = auto_arima(train_data, start_p=0, d=1, start_q=0, max_p=5, max_d=5, max_q=5, seasonal=False, trace=True)

# Afficher les meilleures valeurs de p, d et q trouvées
print(stepwise_fit.order)
