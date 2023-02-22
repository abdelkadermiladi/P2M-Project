import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

# charger les données
df = pd.read_csv("anciens csv/df_february_2.csv")

# prétraitement des données
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df = df.sort_index()
scaler = MinMaxScaler()
df['debit'] = scaler.fit_transform(df[['debit']])

# préparation des données pour l'entraînement et la validation
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)

# convertir les données en une structure utilisable pour le modèle
data = df.values
train_size = int(len(data) * 0.67)
test_size = len(data) - train_size
train, test = data[0:train_size,:], data[train_size:len(data),:]
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)

# reshape les données pour les passer au modèle LSTM
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

# définir et entraîner le modèle LSTM
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)

# faire les prévisions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

# dé-normaliser les prévisions pour les comparer à la valeur réelle
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse
