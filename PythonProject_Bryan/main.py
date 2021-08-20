import pandas as pd

BestAsiaCountry = pd.read_excel('Project_File.xlsx')

#print(AsiaCountry["Brunei Darussalam"])
#print(AsiaCountry.head(3))
#print(AsiaCountry.tail(3))

#class AsiaCountry:

    #def __init__(self, name_of_country, year_duration):
       #self.name_of_country = name_of_country
       #self.year_duration = year_duration




xls = pd.ExcelFile("Project_File.xlsx")

dataFrame = xls.parse(0, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12]),
names=["Year", "Brunei Darussalam", "Indonesia" , "Malaysia", "Philippines", "Thailand", "Viet Nam", "Myanmar","Japan","Hong Kong", "China", "Taiwan", "Korea, Republic Of" ],


print(dataFrame)





xls = pd.read_excel("Project_File.xlsx", nrows=120, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12]),
name=["Year", "Brunei Darussalam", "Indonesia" , "Malaysia", "Philippines", "Thailand", "Viet Nam", "Myanmar","Japan","Hong Kong", "China", "Taiwan", "Korea, Republic Of" ]

print(xls)



print("The top 3 most Countries with the most Visitor")
print("Japan:" + str (pd.read_excel("Project_File.xlsx")[0:120]["Japan"].sum()))
print("Hong Kong:" + str (pd.read_excel("Project_File.xlsx")[0:120]["Hong Kong"].sum()))
print("Taiwan:" + str (pd.read_excel("Project_File.xlsx")[0:120]["Taiwan"].sum()))

print("The mean visitor numbers from Top3 Countries ")
print("Japan:" + str (pd.read_excel("Project_File.xlsx")[0:120]["Japan"].mean()))
print("Hong Kong:" + str (pd.read_excel("Project_File.xlsx")[0:120]["Hong Kong"].mean()))
print("Taiwan:" + str (pd.read_excel("Project_File.xlsx")[0:120]["Taiwan"].mean()))
print("The Median visitor numbers from Top3 Countries")
print("Japan:" + str (pd.read_excel("Project_File.xlsx")[0:120]["Japan"].median()))
print("Hong Kong:" + str (pd.read_excel("Project_File.xlsx")[0:120]["Hong Kong"].median()))
print("Taiwan:" + str (pd.read_excel("Project_File.xlsx")[0:120]["Taiwan"].median()))

import matplotlib.pyplot as plt


plt.scatter("Japan:" + str(pd.read_excel("Project_File.xlsx")[0:120]["Japan"].sum()), "1978", color ='gold')
plt.scatter("Hong Kong:" + str(pd.read_excel("Project_File.xlsx")[0:120]["Hong Kong"].sum()), "1980")
plt.scatter("Taiwan:" + str(pd.read_excel("Project_File.xlsx")[0:120]["Taiwan"].sum()), "1982")
plt.scatter("China:" + str(pd.read_excel("Project_File.xlsx")[0:120]["China"].sum()), "1984 ")
plt.scatter("Korea:" + str(pd.read_excel("Project_File.xlsx")[0:120]["Korea, Republic Of"].sum()), "1986")
plt.ylabel("Years")
plt.xlabel("Total Visitor")

plt.legend(["Japan","Hong Kong", "Taiwan", "China", "Korea"])
plt.title("Total visitors per Country each year (10 years)")

plt.show()

#data = [("Japan:" + str(pd.read_excel("Project_File.xlsx")[0:120]["Japan"].sum())),("Hong Kong:" + str(pd.read_excel("Project_File.xlsx")[0:120]["Hong Kong"].sum())), ("Taiwan:" + str(pd.read_excel("Project_File.xlsx")[0:120]["Taiwan"].sum())), ("China:" + str(pd.read_excel("Project_File.xlsx")[0:120]["China"].sum())), ("Korea:" + str(pd.read_excel("Project_File.xlsx")[0:120]["Korea, Republic Of"].sum()))]
#data2 = [3543798, 894780, 738616, 48882, 261759]

#plt.title("Total visitors per Country each year")

#plt.ylabel("Years")
#plt.xlabel("Total Visitor")
#plt.bar(data, height=7.8, color = 'gold' )
#plt.show()
























