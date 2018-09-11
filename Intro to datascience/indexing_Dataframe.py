import pandas as pd

'''
You can think of a DataFrame as a group of Series that share an index.
This makes it easy to select specific columns that you want from the 
DataFrame. 

Also a couple pointers:
1) Selecting a single column from the DataFrame will return a Series
2) Selecting multiple columns from the DataFrame will return a DataFrame

*This playground is inspired by Greg Reda's post on Intro to Pandas Data Structures:
http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
'''
# Change False to True to see Series indexing in action
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print football['year']
    print ''
    print football.year  # shorthand for football['year']
    print ''
    print football[['year', 'wins', 'losses']]
    
# 0    2010
# 1    2011
# 2    2012
# 3    2011
# 4    2012
# 5    2010
# 6    2011
# 7    2012
# Name: year, dtype: int64

# 0    2010
# 1    2011
# 2    2012
# 3    2011
# 4    2012
# 5    2010
# 6    2011
# 7    2012
# Name: year, dtype: int64

#   year  wins  losses
# 0  2010    11       5
# 1  2011     8       8
# 2  2012    10       6
# 3  2011    15       1
# 4  2012    11       5
# 5  2010     6      10
# 6  2011    10       6
# 7  2012     4      12


'''
Row selection can be done through multiple ways.

Some of the basic and common methods are:
   1) Slicing
   2) An individual index (through the functions iloc or loc)
   3) Boolean indexing

You can also combine multiple selection requirements through boolean
operators like & (and) or | (or)
'''
# Change False to True to see boolean indexing in action
if True:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print football.iloc[[0]]
    print ""
    print football.loc[[0]]
    print ""
    print football[3:5]
    print ""
    print football[football.wins > 10]
    print ""
    print football[(football.wins > 10) & (football.team == "Packers")]

# losses   team  wins  year
# 0       5  Bears    11  2010

#   losses   team  wins  year
# 0       5  Bears    11  2010

#   losses     team  wins  year
# 3       1  Packers    15  2011
# 4       5  Packers    11  2012

#   losses     team  wins  year
# 0       5    Bears    11  2010
# 3       1  Packers    15  2011
# 4       5  Packers    11  2012

#   losses     team  wins  year
# 3       1  Packers    15  2011
# 4       5  Packers    11  2012

