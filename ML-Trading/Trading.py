import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#usecols = ['Date', 'Adj Close'], na_values=['nan]

#Close
##Actual price reported at the exchange reported that day

#Adj Close
## Adjusted price for Stock splits, Dividend payments


def get_max_close(df):
    return df['Close'].max()

def get_mean_volume(df):
    return df['Volume'].mean()

def get_values_date_range(start,end,df):
    return ''

def symbol_to_path(symbol, base_dir="./"):
    ''' Return CSV file path given ticker symbol'''
    return os.path.join(base_dir,"{}.csv".format(str(symbol)))

def get_data(symbols, df_final):
    '''Read stock data for all the symbols'''
    for symbol in symbols:
        df_temp = pd.read_csv('{}.csv'.format(symbol), index_col="Date", parse_dates=True,na_values=['nan'], usecols=['Date','Adj Close'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df_final = df_final.join(df_temp, how='inner')

    return df_final
#df['Adj Close'].plot()
#plt.show()

df1 = pd.read_csv('HCP.csv', index_col="Date", parse_dates=True, usecols=['Date','Adj Close'])
symbols = ['IBM','SPY', 'GOOGL','GLD']

df1 = get_data(symbols, df1)

print (df1)
#252 Trading days in NYSE
