

#1 La récupération de données :  cotation Airbus et carrefour depuis 2010
#2 Le traitement et l’analyse : 
#2.1 Éliminer les NaN et les données non pertinentes
#2.2 traiter
#3 La représentation / application : Établir des graphique

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Created on 01 12 2020
########

#@author: Luisa,Ismail,Mamy, Olivier

#https://github.com/Benny-/Yahoo-ticker-symbol-downloader

#1 La récupération de données : cotation Airbus depuis 2010

#!/usr/bin/env python
# coding: utf-8
# TP ml Data scientist

# importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.preprocessing import MinMaxScaler
print("hello this for sharing group code")
import yfinance as yf

airbus ='AIR.PA'
carrefour ='CA.PA'

data = yf.Ticker(airbus)
datac = yf.Ticker(carrefour)

dataDFA = data.history(period='1d',start = '2000-12-01',end='2020-11-30')
dataDFC = datac.history(period='1d',start = '2000-12-01',end='2020-11-30')


dataDFA.to_csv(r'C:\Users\Luisa.HERNANDEZ-ZABA\PycharmProjects\tp-machine-learnig\data_airbus.csv', index = False)
dataDFC.to_csv(r'C:\Users\Luisa.HERNANDEZ-ZABA\PycharmProjects\tp-machine-learnig\data_carrefour.csv', index = False)

#partie ajouter pour classer les valeurs nulles des colonnes de differents tables avec leurs pourcentage
def missing_data(data):
    total = data.isnull().sum().sort_values(ascending = False)
    percent = (data.isnull().sum()/data.isnull().count()*100).sort_values(ascending = False)
    return pd.concat([total, percent], axis=1, keys=['Total NaN Values', 'Percentage of NaN Values'])

missing_data(dataDFA)
missing_data(dataDFC)

dataDFC.dtypes
dataDFC.head()
# suppression des colonnes qui n'ont pas d'interet
DataDFC = dataDFC.drop(['Open', 'High', 'Low', 'Volume', 'Dividends', 'Stock Splits'], axis = 1)
DataDFC.head()
DataDFC.plot(kind='bar', subplots=False)

dataDFA.dtypes
dataDFA.head()
# suppression des colonnes qui n'ont pas d'interet
DataDFA = dataDFA.drop(['Open', 'High', 'Low', 'Volume', 'Dividends', 'Stock Splits'], axis = 1)
DataDFA.head()
DataDFA.plot(kind='bar', subplots=False)

#mise en echelle de données AIRBUS
train_values = DataDFA.values
min_max_scaler = MinMaxScaler()
# définir le scaler à partir de l'ensemble des données
scaler = min_max_scaler.fit(train_values.reshape(-1, 1))
# mise à l'échelle des données d'apprentissage et de test
train_values = scaler.transform(DataDFA.values[:2000].reshape(-1, 1))
test_values = scaler.transform(DataDFA.values[2000:].reshape(-1, 1))

from sklearn.preprocessing import MinMaxScaler
#mise en echelle de données AIRBUS
data_airbus_serie = DataDFA.values
min_max = MinMaxScaler()
# définir le scaler à partir de l'ensemble des données # mise à l'échelle des données entre -1 et 1
data_airbus_serie = min_max.fit_transform(data_airbus_serie.reshape(-1, 1))

data_airbus_serie

def create_window(dataset, start_index, end_index, history_size, prediction_size):
    data = []
    labels = []

    start_index = start_index + history_size
    if end_index is None:
        end_index = len(dataset) - prediction_size

    for i in range(start_index, end_index):
        indices = range(i - history_size, i)
        data.append(np.reshape(dataset[indices], (history_size, 1)))
        
        if dataset[i+prediction_size] == 0:
            if dataset[i] == 0:
                labels.append(0)
            else:
                labels.append(-1)
        else:
            delta = ((dataset[i+prediction_size] - dataset[i]) / dataset[i+prediction_size]) * 100
            if delta > 2:
                labels.append(1)
            elif delta >= -2:
                labels.append(0)
            else:
                labels.append(-1)
       
    return np.array(data), np.array(labels)

#lancement de la fonction avec une fenetre se 20 jours et une prediction à 4 jours
data_X, data_Y = create_window(data_airbus_serie, 0, None, 20,4)

plt.hist(data_Y)
plt.show()
#on observe bien une matrice de points égale à -1, 0 et 1

data_X.shape

data_y.shape


print("end of code")
