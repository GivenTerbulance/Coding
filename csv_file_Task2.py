import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


#############################################################
print("WELCOME!!, WE SPEAK DATA")
#############################################################
"""This python script generate the dataset and manipulate the dataset in terms of calculating the summary statistics, filtering
dataset, generating the bargraph, and saving the manipulated data in a new file 
"""
print("Dataset table:")


  
data ={
    """This is the dataset used to store the services with respect to the salary and people providing the services on different contries
    """
    "Person":["Jack", "James", "Andrew", "Olivia", "Lucas" ],
    "salary(R)":["15000", "13000", "19000", "21000", "17000"],
    "Facilities":["2","5","1","4","3"],
    "Services":["Software Engineering", "Web-development", "Hardware development", "Networking services", "System Troubleshoot"],
    "Country":["USA", "South Africa","France","Germany","London"]

 }

"""
Saving new manipulated dataset to file person.csv
"""
df = pd.DataFrame(data)
df.to_csv("person.csv")

df = pd.read_csv('person.csv')
print(df.head())
#############################################################
print("Summary Statistics:")
#############################################################
"""
This part set the summary statistics variables to calculate them
"""
mean1 = df['salary(R)'].mean()
sum1 =df['salary(R)'].sum()
max1 = df['Facilities'].max()
min1 = df['Facilities'].min()
count1 = df['salary(R)'].count()
meadian1 =df['Facilities'].median()
standard_dev =df["Facilities"].std()
  
"""
This part we execute the summary statistics accordingly
"""
print('mean salary:' + str(mean1))
print('Sum of the salary:' + str(sum1))
print('max of facilities is:' + str(max1))
print('min of facilities is:' + str(min1))
print('count of salary is:' + str(count1))
print('meadian of facilities is:' + str(meadian1))
print('Standard_deviation of facilities is:' + str(standard_dev))


#Filtering data
df =df[["Facilities", "Services"]]
print(df)


##################Ploting bar-graph############################

  

Services = "Services"
salary = "salary(R)"
plt.bar(Services, salary, color ='blue',width=0.5)
plt.xlabel("Services")
plt.ylabel("salary(R)")
plt.title("Salary vs Services")
plt.show()
 
