from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import pandas
import os
import matplotlib
import matplotlib.pyplot as plt
import time

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

def macdStrat(stocks):
    data, meta_data = ti.get_macd(symbol=stocks, interval='15min')
    df = data['MACD_Hist']
    secondmacd = df[0]
    firstmacd = df[1]

    if secondmacd > firstmacd:
        return 'MACD: BUY ' + stocks
    else:
        return 'MACD: SELL ' + stocks


