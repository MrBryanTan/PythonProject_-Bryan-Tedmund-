import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

class AsiaCountryStatistics:
    def __init__(self):
        self.asiaCountries = pd.ExcelFile('Project_File.xlsx')
        self.df = self.asiaCountries.parse(0, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], names=['Date', 'Brunei Darussalam', 'Indonesia', 'Malaysia', 'Philippines','Thailand', 'Viet Nam', 'Myanmar', 'Japan', 'Hong Kong', 'China','Taiwan', 'Korea, Republic Of'])

    def Top10years(self):
       print(self.df[0:120])

    def SplitingMonthnYear(self):
       self.df['month'] = pd.DatetimeIndex(self.df['Date']).month
       self.df['year'] = pd.DatetimeIndex(self.df['Date']).year
       print(self.df.head(120))



    def AllCountry(self):
        print("Sum of Countries with Visitor")
        print("Japan: " + str(self.df[0:120]["Japan"].sum()))
        print("China: " + str(self.df[0:120]["China"].sum()))
        print("Hong Kong: " + str(self.df[0:120]["Hong Kong"].sum()))
        print("Taiwan: " + str(self.df[0:120]["Taiwan"].sum()))
        print("Korea, Republic Of: " + str(self.df[0:120]["Korea, Republic Of"].sum()))

    def Top3CountrySum(self):
        print("Top 3 Countries with the Most Visitor")
        print("Japan: " + str(self.df[0:120]["Japan"].sum()))
        print("Hong Kong: " + str(self.df[0:120]["Hong Kong"].sum()))
        print("Taiwan: " + str(self.df[0:120]["Taiwan"].sum()))

    def Top3CountryMean(self):
        print("Mean visitor numbers from TOP 3 Countries")
        print("Mean from Japan: " + str(self.df[0:120]["Japan"].mean()))
        print("Mean from Hong Kong: " + str(self.df[0:120]["Hong Kong"].mean()))
        print("Mean from Taiwan: " + str(self.df[0:120]["Taiwan"].mean()))

    def Top3CountryMedian(self):
        print("Median visitor number from TOP 3 Countries")
        print("Median from Japan: " + str(self.df[0:120]["Japan"].median()))
        print("Median from Hong Kong: " + str(self.df[0:120]["Hong Kong"].median()))
        print("Media from Taiwan: " + str(self.df[0:120]["Taiwan"].median()))

    def BarGraph(self):
        plt.bar(self.df['year'][0:120], self.df['Japan'][0:120], color=['red'])
        plt.xlabel("Year", fontweight='bold')
        plt.ylabel("No.of visitor", fontweight='bold')
        plt.title("No. of visitor visited over 10 years in Japan", fontweight='bold')
        ax = plt.axes()
        ax.set_facecolor("black")
        plt.show()






acs = AsiaCountryStatistics()
acs.Top10years()
acs.SplitingMonthnYear()
acs.AllCountry()
acs.Top3CountrySum()
acs.Top3CountryMean()
acs.Top3CountryMedian()
acs.BarGraph()



