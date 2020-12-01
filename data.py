# Created by Luisa Hernandez Z.
#https://github.com/Benny-/Yahoo-ticker-symbol-downloader
print("hello this for sharing group code")
import yfinance as yf

airbus ='AIR.PA'
data = yf.Ticker(airbus)

dataDF = data.history(period='1d',start = '2000-12-01',end='2020-11-30')


dataDF.to_csv(r'C:\Users\Luisa.HERNANDEZ-ZABA\PycharmProjects\tp-machine-learnig\data_airbus.csv', index = False)


print("end of code")