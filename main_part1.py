#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import os
import csv


# In[2]:


#filepath budget_data.csv
budget_path = os.path.join('PyBank','Resources','budget_data.csv')


# In[3]:


#define variables
total=0
new_buget_list=[]
new_buget_date=[]
buget_change=[]
max_profit_date=''
max_profit_num=0
min_profit_date=''
min_profit_num=0


# In[4]:


#read file

with open (budget_path, newline='') as budget_csv:
    #split into columns
    budget_reader = csv.reader(budget_csv,delimiter=',')
    #print(budget_reader)
    header = next(budget_reader)
    #Loop through the data
    for row in budget_reader:              
        total += int(row[1])
        new_buget_list.append(int(row[1]))
        new_buget_date.append(row[0])

# Generate a list with budget changes
i=1
while i<len(new_buget_list):    
    buget_change.append((new_buget_list[i]-new_buget_list[i-1]))
    i+=1

    
#         if int(row[1])>=0:
#             if int(row[1])>max_profit_num:
#                 max_profit_num = int(row[1])
#                 max_profit_date = row[0]
#         else:
#             if int(row[1])<min_profit_num:
#                 min_profit_num = int(row[1])
#                 min_profit_date = row[0]


# In[5]:


# Calculate Max & Min budge change
max_profit_num=max(buget_change)
max_profit_date=new_buget_date[buget_change.index(max_profit_num)+1]
min_profit_num=min(buget_change)
min_profit_date=new_buget_date[buget_change.index(min_profit_num)+1]


# In[6]:


#Calculate total month
total_month = len(new_buget_list)
#Calculate Average  Change
ave_change = round(sum(buget_change)/len(buget_change),2)    


# In[7]:


#Print results
print("Financial Analysis")
print("==================")
print('Total Months: ' + str(total_month))
print('Total: $' + str(total))
print('Average  Change: $' + str(ave_change))
print('Greatest Increase in Profits: ' + max_profit_date + ' ($' + str(max_profit_num) + ')')
print('Greatest Decrease in Profits: ' + min_profit_date + ' ($' + str(min_profit_num) + ')')


# In[8]:


# Specify the file to write to
output_path = os.path.join("budget_out.csv")


# In[9]:


# Open the file using "write" mode
with open(output_path, 'w', newline='') as budgetfile:

    # Initialize csv.writer
    csvwriter = csv.writer(budgetfile)

    # Write the rows
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["=================="])
    csvwriter.writerow(["Total Months: " + str(total_month)])
    csvwriter.writerow(['Total: $' + str(total)])
    csvwriter.writerow(['Average  Change: $' + str(ave_change)])
    csvwriter.writerow(['Greatest Increase in Profits: ' + max_profit_date + ' ($' + str(max_profit_num) + ')'])
    csvwriter.writerow(['Greatest Decrease in Profits: ' + min_profit_date + ' ($' + str(min_profit_num) + ')'])

