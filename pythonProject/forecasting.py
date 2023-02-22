from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

# Charger les données en utilisant pandas
data = pd.read_csv('anciens csv/df_february_2.csv')

# Séparer les données en données d'entraînement et de test
train_data = data.iloc[:int(0.8*len(data))]
test_data = data.iloc[int(0.8*len(data)):]

#removes the rows that contains NULL values
#data=data.dropna()
#tracer les données du premier mois
data['cumul'].plot(figsize=(100,10))
#data['cumul'].plot(figsize=(100,10))

# Créer et entraîner le modèle SARIMAX
model = SARIMAX(train_data["cumul"], order=(3, 2, 3))
model_fit = model.fit()




# Faire des prévisions sur les données de test
predictions = model_fit.predict(start=test_data.index[0], end=test_data.index[-1],typ='changes',dynamic=True)
print(predictions)

plt.figure(figsize=(100, 10))
# Tracer les données de test
plt.plot(test_data["cumul"], label="Données de test")

# Tracer les données prédites
plt.plot(predictions, label="Données prédites", linestyle='dashed')

# Ajouter une légende et un titre
plt.legend()
plt.title("Comparaison des données prédites et de test")


# Afficher le graphique
plt.show()

# Evaluer les prévisions en utilisant des métriques de performance appropriées (RMSE)

rmse = np.sqrt(mean_squared_error(test_data["cumul"], predictions))
print("RMSE: ", rmse)

# Calculer le coefficient de corrélation entre les valeurs prédites et les valeurs de test
correlation = r2_score(test_data["cumul"], predictions)
print("Coefficient de corrélation :", correlation)
