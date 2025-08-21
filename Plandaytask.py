#!/usr/bin/env python
# coding: utf-8

# # Task 1

# Given the missing functionality in Tableau to perform data cleaning task, I will start off by cleaning the dataset using Python, and then import a cleaned CSV file to Tableau for the data visualization tasks. 

# In[19]:


import pandas as pd
import numpy as np


# In[20]:


#Importing the dataset and gaining a quick overview of the Columns and Data types associated with it. 
df = pd.read_csv("/Users/emillokken/Desktop/DA task.csv")

df.head()
df.info()


# In[21]:


#From the overview seen above, we have a strong dataset, but most columns is displayed in an incorrect datatype. 
#We can fix this in Python by converting each column to its prefferred DT. I have followed the table scheme in the 
#task document for the correct data types.

#Convert string columns to datetime
date_cols = ["TIMESTAMP", "CONVERTED_AT", "TRIAL_START", "TRIAL_END"]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")

#Double-check datatypes again to see if the conversion was succesfull
df.info()


# In[24]:


#Check for missing values in the dataset
df.isna().sum()

#As all missing values are related to the "Converted at" column, we do not treat these as problematic nulls. 
#If we had found missing values in other important columns (e.g.TIMESTAMP or TRIAL_START),
#there are typically two main approaches:
#1. Drop the rows (if only a small % of the dataset is affected).
#2. Impute or fill the missing values (if dropping would remove too much valuable data).


# In[29]:


#For the next step I want to remove any duplicate rows. It's common to check for and remove rows that are 
#entirely duplicated across all columns. These are not meaningful for analysis and can skew metrics if left in.

#Count exact duplicates
duplicate_count = df.duplicated().sum()
print(f"Exact duplicate rows: {duplicate_count}")

#Only drop rows that are fully identical across all columns
df = df.drop_duplicates()

#Confirm new shape of dataset is equal to total amount of rows before dropping duplicates - total count of duplicates
print(f"Remaining rows after dropping exact duplicates: {len(df)}")


# In[33]:


#In this step, I want to perform some sanity checks and make sure that the events are occuring in the expected data range

#First of all we can check if all events occurred within the trial window:
invalid_time_mask = (df["TIMESTAMP"] < df["TRIAL_START"]) | (df["TIMESTAMP"] > df["TRIAL_END"])
invalid_time_rows = df[invalid_time_mask]
print(f"Events outside trial period: {len(invalid_time_rows)}")

#We can also check if CONVERTED == True always has a CONVERTED_AT timestamp. This should always be the case, 
#so it is crucial that we verify this
converted_without_timestamp = df[(df["CONVERTED"] == True) & (df["CONVERTED_AT"].isna())]
print(f"Converted rows missing CONVERTED_AT: {len(converted_without_timestamp)}")


# In[34]:


#The last step is to add some derived fields that might be included in later analysis in Tableau:

#1. Days from trial start to each event
df["DAYS_FROM_START"] = (df["TIMESTAMP"] - df["TRIAL_START"]).dt.days

#2. Days from trial start to conversion (only if converted)
df["DAYS_TO_CONVERSION"] = (df["CONVERTED_AT"] - df["TRIAL_START"]).dt.days

#3. Flag: Did this event happen before conversion?
df["EVENT_BEFORE_CONVERSION"] = df["TIMESTAMP"] <= df["CONVERTED_AT"]

#4. Week of trial (helps with aggregation later in Tableau)
df["WEEK_FROM_START"] = ((df["TIMESTAMP"] - df["TRIAL_START"]).dt.days // 7) + 1


# In[35]:


# Step 8: Export cleaned dataset for Tableau
output_file = "cleaned_trial_data.csv"
df.to_csv(output_file, index=False)
print(f"Cleaned dataset exported to: {output_file}")


# In[ ]:




