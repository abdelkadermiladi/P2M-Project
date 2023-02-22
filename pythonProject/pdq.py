
import warnings
warnings.filterwarnings("ignore")
import pandas as pd

# Chargement des données à partir du fichier CSV
data = pd.read_csv("premier_mois.csv")

# Sélectionner la colonne de données à utiliser pour le modèle
train_data = data.iloc[:int(0.8*len(data))]
train_data = train_data["debit"]

import statsmodels.api as sm
import itertools

def evaluate_arima_model(train_data, p_values, d_values, q_values):
    best_aic = float("inf")
    best_p = None
    best_d = None
    best_q = None

    for p, d, q in itertools.product(p_values, d_values, q_values):
        try:
            model = sm.tsa.ARIMA(train_data, order=(p, d, q))
            model_fit = model.fit()
            aic = model_fit.aic
            if aic < best_aic:
                best_aic = aic
                best_p = p
                best_d = d
                best_q = q
        except:
            continue

    print(f"Best ARIMA Model: p = {best_p}, d = {best_d}, q = {best_q} with AIC = {best_aic}")

p_values = [0, 1, 2, 4]
d_values = [0, 1, 2]
q_values = [0, 1, 2, 4]
evaluate_arima_model(train_data, p_values, d_values, q_values)
