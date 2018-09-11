
import pandas

from ggplot import *


def lineplot_compare(hr_by_team_year_sf_la_csv):
    # Write a function, lineplot_compare, that will read a csv file
    # called hr_by_team_year_sf_la.csv and plot it using pandas and ggplot.
    #
    # This csv file has three columns: yearID, HR, and teamID. The data in the
    # file gives the total number of home runs hit each year by the SF Giants 
    # (teamID == 'SFN') and the LA Dodgers (teamID == "LAN"). Produce a 
    # visualization comparing the total home runs by year of the two teams. 
    # 
    # You can see the data in hr_by_team_year_sf_la_csv
    # at the link below:
    # https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/hr_by_team_year_sf_la.csv
    #
    # Note that to differentiate between multiple categories on the 
    # same plot in ggplot, we can pass color in with the other arguments
    # to aes, rather than in our geometry functions. For example, 
    # ggplot(data, aes(xvar, yvar, color=category_var)). This might help you 
    # in this exercise.
    df = pandas.read_csv(hr_by_team_year_sf_la_csv)
    df_SFN = df[(df['teamID'] == 'SFN')]
    df_LAN = df[(df['teamID'] == 'LAN')]

    #Second way and correct way
     #gg = ggplot(df,aes(x='yearID',y='HR', color='teamID')) + geom_point() +geom_line()  + ggtitle('HR by year') +xlab('Year') +ylab('HR')
    
    gg = ggplot(df,aes(x='yearID',y='HR')) + geom_point() +geom_line(data=df_SFN, color='red')  +geom_line(data=df_LAN,color='green') + ggtitle('HR by year') +xlab('Year') +ylab('HR')
    return gg
