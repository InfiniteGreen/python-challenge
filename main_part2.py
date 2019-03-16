#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import os
import csv


# In[2]:


#filepath budget_data.csv
poll_path = os.path.join('PyPoll','Resources','election_data.csv')


# In[3]:


#define variables
candidate_list=[]
unique_candidate_list=[]


# In[4]:


#read file

with open (poll_path, newline='') as poll_csv:
    #split into columns
    poll_reader = csv.reader(poll_csv,delimiter=',')    
    header = next(poll_reader)
    #Loop through the data
    for row in poll_reader:            
        candidate_list.append(row[2])
        if row[2] not in unique_candidate_list:
            unique_candidate_list.append(row[2])
#unique_candidate_list


# In[5]:


# Get total votes
totalvotes = len(candidate_list)


# In[6]:


k=0
vote_count=[]
vote_percent=[]
while k<len(unique_candidate_list):
    vote_count.append(candidate_list.count(str(unique_candidate_list[k])))    
    vote_percent.append("{:.3%}".format(vote_count[k]/totalvotes))
    k+=1
#vote_count   
#vote_percent 
#winner    


# In[7]:


#Get the Poll winner
winner=unique_candidate_list[vote_count.index(max(vote_count))]
winner


# In[8]:


#Print results
print("Election Results")
print("---------------------------")
print('Total Votes: ' + str(totalvotes))
print("---------------------------")   

j=0
while j<len(unique_candidate_list):
    print(str(unique_candidate_list[j]) + ': ' + str(vote_percent[j]) + ' (' + str(vote_count[j]) + ')')    
    j+=1
    
print("---------------------------") 
print('Winner: ' + str(winner))
print("---------------------------") 


# In[9]:


# Specify the file to write to
output_path = os.path.join("poll_out.csv")


# In[10]:


# Open the file using "write" mode
with open(output_path, 'w', newline='') as pollfile:

    # Initialize csv.writer
    csvwriter = csv.writer(pollfile)

    # Write the rows
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["---------------------------"])
    csvwriter.writerow(['Total Votes: ' + str(totalvotes)])
    csvwriter.writerow(["---------------------------"])
    
    i=0
    while i<len(unique_candidate_list):
        csvwriter.writerow([str(unique_candidate_list[i]) + ': ' + str(vote_percent[i]) + ' (' + str(vote_count[i]) + ')'])
        i+=1
    
    csvwriter.writerow(["---------------------------"]) 
    csvwriter.writerow(['Winner: ' + str(winner)])
    csvwriter.writerow(["---------------------------"]) 

