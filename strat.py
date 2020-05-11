from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import pandas
import os
import matplotlib
import matplotlib.pyplot as plt

ts = TimeSeries(key = 'API_KEY', output_format='pandas')

ti = TechIndicators(key= 'API_KEY', output_format='pandas')

def strat(stocks):
    data, meta_data = ti.get_ema(symbol= stocks, interval='1min', time_period=9, series_type='close')
    datat, meta_datat = ti.get_ema(symbol= stocks, interval='1min', time_period=20, series_type='close')
    df = data.iloc[-1]
    dfa = datat.iloc[-1]
    if float(df) / float(dfa) >= 1 and float(df)/float(dfa) <= 1.25 :
        return print('BUY ' + stocks)  
    else:
        return print('SELL ' + stocks)

stocks = ["MMM", "AXP", "AAPL", "BA", "CAT", "CVX", "CSCO", "KO", "DOW", "XOM", "GS", "HD", "IBM", "INTC", "JNJ", "JPM", "MCD", "MRK", "MSFT", "NKE", "PFE", "PG", "TRV", "UNH", "UTX", "VZ", "V", "WMT", "WBA", "DIS"]

for i in stocks:
    x = strat(i)
    print(x)


