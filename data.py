

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

print("hello this for sharing group code")
import yfinance as yf

airbus ='AIR.PA'
carrefour ='CA.PA'

data = yf.Ticker(airbus)
datac = yf.Ticker(carrefour)

dataDF = data.history(period='1d',start = '2000-12-01',end='2020-11-30')

dataDF.to_csv(r'C:\Users\Luisa.HERNANDEZ-ZABA\PycharmProjects\tp-machine-learnig\data_airbus.csv', index = False)


print("end of code")
