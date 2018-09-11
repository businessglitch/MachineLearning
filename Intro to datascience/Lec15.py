import pandas as pd

dictonary = {'name':      pd.Series(['Braund','Cummings','Heikkinen','Allen'],index=['a','b','c','d']),
             'age':       pd.Series([22,38,26,35], index=['a','b','c','d']),
             'fare':      pd.Series([7.25,17.83,8.05,],index=['a','b','d']),
             'survived?': pd.Series([False, True, True, False], index=['a','b','c','d'])}
df = pd.DataFrame(dictonary)
print(df)
