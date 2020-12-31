import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
import datetime
import yfinance as yf
pd.options.display.float_format = '{:,.0f}'.format
yf.pdr_override()
hoje = datetime.datetime.now().isoformat()[:10]
data = web.get_data_yahoo(sys.argv[1], start='2019-05-05',end=hoje)
from stockstats import StockDataFrame as Sdf
stock  = Sdf.retype(data)
signal = stock['macds']        
macd   = stock['macd']                                                    
listLongShort = ["No data"]

for i in range(1, len(signal)):
    #                          
    if macd[i] > signal[i] and macd[i - 1] <= signal[i - 1] and macd[i] < 0 and signal[i] < 0 :
        listLongShort.append("COMPRAR FORTE")
    #                         
    elif macd[i] < signal[i] and macd[i - 1] >= signal[i - 1]:
        listLongShort.append("VENDER")
    elif macd[i] > signal[i] and macd[i - 1] <= signal[i - 1]:
        listLongShort.append("COMPRAR")

    #                         
    else:
        listLongShort.append("SEGURAR")

stock['Recomendacao'] = listLongShort
stock['Ativo'] = sys.argv[1]
dado = stock.tail(4)
resul = dado[['Recomendacao','Ativo']]
print (resul)

del stock
