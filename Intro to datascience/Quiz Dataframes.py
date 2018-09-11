import numpy as np
import pandas as pd

'''
The following code is to help you play with the concept of Dataframe in Pandas.

You can think of a Dataframe as something with rows and columns. It is
similar to a spreadsheet, a database table, or R's data.frame object.

*This playground is inspired by Greg Reda's post on Intro to Pandas Data Structures:
http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
'''

'''
To create a dataframe, you can pass a dictionary of lists to the Dataframe
constructor:
1) The key of the dictionary will be the column name
2) The associating list will be the values within that column.
'''
# Change False to True to see Dataframes in action
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print football
    
    #     losses     team  wins  year
    # 0       5    Bears    11  2010
    # 1       8    Bears     8  2011
    # 2       6    Bears    10  2012
    # 3       1  Packers    15  2011
    # 4       5  Packers    11  2012
    # 5      10    Lions     6  2010
    # 6       6    Lions    10  2011
    # 7      12    Lions     4  2012


'''
Pandas also has various functions that will help you understand some basic
information about your data frame. Some of these functions are:
1) dtypes: to get the datatype for each column
2) describe: useful for seeing basic statistics of the dataframe's numerical
   columns
3) head: displays the first five rows of the dataset
4) tail: displays the last five rows of the dataset
'''
# Change False to True to see these functions in action
if True:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print football.dtypes
    # losses     int64
    # team      object
    # wins       int64
    # year       int64
    # dtype: object
    print ""
    print football.describe()
    #         losses       wins         year
    # count   8.000000   8.000000     8.000000
    # mean    6.625000   9.375000  2011.125000
    # std     3.377975   3.377975     0.834523
    # min     1.000000   4.000000  2010.000000
    # 25%     5.000000   7.500000  2010.750000
    # 50%     6.000000  10.000000  2011.000000
    # 75%     8.500000  11.000000  2012.000000
    # max    12.000000  15.000000  2012.000000
    print ""
    print football.head()
#     losses    team   wins  year
# 0       5    Bears    11  2010
# 1       8    Bears     8  2011
# 2       6    Bears    10  2012
# 3       1  Packers    15  2011
# 4       5  Packers    11  2012
    print ""
    print football.tail()
#       losses     team    wins year
# 3       1       Packers    15  2011
# 4       5       Packers    11  2012
# 5      10        Lions     6   2010
# 6       6        Lions    10   2011
# 7      12        Lions     4   2012
