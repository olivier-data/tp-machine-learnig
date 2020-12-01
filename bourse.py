#!/usr/bin/env python
# coding: utf-8

# In[147]:


import yfinance as yf
from github import Github
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt


# In[9]:


#Définir ticker pour Airbus
airbus='AIR.PA'
data=yf.Ticker(airbus)


# In[18]:


#Récupérer data
dataAirbusDF = data.history(period='1d',start='2000-12-01',end='2020-11-30')


# In[20]:


dataAirbusDF


# In[21]:


#Définir ticker pour Carrefour
carrefour='CA.PA'
data_c=yf.Ticker(carrefour)


# In[23]:


#Récupérer data
dataCarrefourDF = data_c.history(period='1d',start='2000-12-01',end='2020-11-30')


# In[24]:


dataCarrefourDF


# In[81]:


#créer fichiers csv
dataAirbusDF.to_csv('C:\\Users\\mamy.rasolomona\\Downloads\\airbus.txt',sep=';')


# In[82]:


dataCarrefourDF.to_csv('C:\\Users\\mamy.rasolomona\\Downloads\\carrefour.txt',sep=';')


# In[101]:


#lire fichier csv Airbus
data_airbus = pd.read_csv('C:\\Users\\mamy.rasolomona\\Downloads\\airbus.txt',sep=';',index_col="Date",parse_dates=True)
data_airbus=data_airbus['Close']


# In[102]:


data_airbus_serie = data_airbus.values


# In[103]:


#normalisation
min_max = MinMaxScaler()
data_airbus_serie = min_max.fit_transform(data_airbus_serie.reshape(-1, 1))


# In[107]:


data_airbus_serie


# In[157]:


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


# In[158]:


data_X, data_Y = create_window(data_airbus_serie, 0, None, 20,4)


# In[159]:


plt.hist(data_Y)
plt.show()


# In[161]:


data_X.shape


# In[162]:


data_Y.shape


# In[ ]:




