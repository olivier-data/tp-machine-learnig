# Created by Luisa Hernandez Z.

print("hello this for sharing group code")
import yfinance as yf

airbus ='AIR.PA'
data = yf.Ticker(airbus)

dataDF = data.history(period='1d',satart = '2000-12-01',end='2020-11-30')

