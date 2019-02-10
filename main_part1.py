#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import os
import csv


# In[2]:


#filepath budget_data.csv
budget_path = os.path.join('PyBank','Resources','budget_data.csv')


# In[18]:


#read file
total=0
totalfirstrow=0
ave_change=0
max_profit_date=''
max_profit_num=0
min_profit_date=''
min_profit_num=0

with open (budget_path, newline='') as budget_csv:
    #split into columns
    budget_reader = csv.reader(budget_csv,delimiter=',')
    #header = next(budget_reader)
    #Loop through the data
    for row in budget_reader:
        #print (row)
        totalfirstrow+=1
        if row[1].isnumeric():
            #total += int(row[1])
            if int(row[1])>=0:
                if int(row[1])>max_profit_num:
                    max_profit_num = int(row[1])
                    max_profit_date = row[0]
                    total+= int(row[1])
            else:
                if int(row[1])> min_profit_num:
                    min_profit_num = int(row[1])
                    min_profit_date = row[0]
                    total-= int(row[1])
                   
    totalfirstrow-=1
    print(str(total))
  


# In[8]:


#Print result
print("Financial Analysis")
print("==================")
print('Total Months: ' + str(totalfirstrow))
print('Total: ' + str(total))
print('Average  Change: $' + str(total/totalfirstrow))
print('Greatest Increase in Profits: ' + max_profit_date + ' ($' + str(max_profit_num) + ')')
print('Greatest Decrease in Profits: ' + min_profit_date + ' ($' + str(min_profit_num) + ')')


# In[ ]:




