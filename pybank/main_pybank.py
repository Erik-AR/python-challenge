import numpy as np
import pandas as pd
import csv
import os
#load data file
data_file = pd.read_csv('budget_data_1.csv')

#Definer headers
date = data_file ['Date']
revenue = data_file ['Revenue']

total_months = len(date)

total_revenue = sum(revenue)




#Figure out change and get avg
#create overview of change

Revenue = data_file ["Revenue"]
change_list = [0]
for index in range (len(Revenue)-1):
   
    current_value = Revenue[index]
    next_value = Revenue[index + 1]
   
    difference = next_value - current_value
  
    change_list.append(difference)

sum_change = sum(change_list) 

avg_change = sum_change/total_months


                
#get max and min change      

imax = np.argmax(change_list)
date[imax]
imin = np.argmin(change_list)
date[imin]

# print output

print("Financial Analysis")
print("--------------------")
print("Number of Months: " + str (total_months))
print("Total Revenue: " + str (total_revenue))
print("Average Change: " + str(avg_change))
print ("Max change: " + date[imax] + ": " + str(np.max(change_list)))
print("Min change in revenue: " + date[imin] + str(np.min(change_list)))
# print(np.argmin(change_list))
# print(sum_change)  