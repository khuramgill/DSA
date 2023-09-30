import matplotlib.pyplot as plt
import pandas as pd 

# Given Code
# df = pd.read_csv('D:\\3rd Sem\\DSA\\Lab\\Lab 4\\population_by_country_2020.csv' )  
# print(df.dtypes) 
# list1 = df['Country (or dependency)'].values.tolist()  
# list2 = df['Population (2020)'].values.tolist()  
# plt.bar(list1, list2,width = 1, color = ['red', 'green']) 
# plt.show()

# Daily Steps / Line
# df = pd.read_csv('D:\\3rd Sem\\DSA\\Lab\\Lab 4\\Data Set\\dailySteps_merged.csv' )  
# print(df.dtypes) 
# list1 = df['Id'].values.tolist()  
# list2 = df['StepTotal'].values.tolist()  
# plt.plot( list1, list2) 
# plt.show()

# Total Time In Bed \ Scatter
# df = pd.read_csv('D:\\3rd Sem\\DSA\\Lab\\Lab 4\\Data Set\\sleepDay_merged.csv' )  
# print(df.dtypes) 
# list1 = df['Id'].values.tolist()  
# list2 = df['TotalTimeInBed'].values.tolist()  
# plt.scatter( list1, list2) 
# plt.show()

#  Daily Distan \ Bar
# df = pd.read_csv('D:\\3rd Sem\\DSA\\Lab\\Lab 4\\Data Set\\dailySteps_merged.csv' )  
# print(df.dtypes) 
# list1 = df['ActivityDay'].values.tolist()  
# list2 = df['StepTotal'].values.tolist()  
# plt.bar( list1, list2,width = 1, color = ['red', 'green']) 
# plt.show()

# Pie Chart
df = pd.read_csv('D:\\3rd Sem\\DSA\\Lab\\Lab 4\\Data Set\\hourlySteps_merged.csv' )  
print(df.dtypes)  
date = df['ActivityHour'].values[2:25].tolist()
date=pd.to_datetime(date,format='%m/%d/%Y %I:%M:%S %p')
hourlySteps=df['StepTotal'].values[2:25].tolist()
plt.pie(hourlySteps, labels=date.strftime('%I:%M %p'), startangle=140)
plt.title('Hourly Steps on 12th April 2016')
plt.show()
