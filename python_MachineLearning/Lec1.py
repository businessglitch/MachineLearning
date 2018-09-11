# Y = mx +b
# Regresision is used to find m and b
# Mostly used for stock prices

import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
# Create a column with % change of Daily fluctuation
df['HL_PCT'] = ((df['Adj. High'] - df['Adj. Low'])/df['Adj. Low']) * 100
# Create a column with % change of new price
df['PCT_Change'] = ((df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open']) * 100

df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

forecast_col = 'Adj. Close'

df.fillna(-99999, inplace=True)

#figure out 10% of the dataframe
forecast_out = int(math.ceil(len(df) * 0.01))

# Create Label for future forecasting
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())

#Features is usually capital X
X = np.array(df.drop(['label'],1))
#Labels is small y
y = np.array(df['label'])

# Scale X before feeding it through classifier
X = preprocessing.scale(X)
