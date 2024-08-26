#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
import seaborn as sns
from scipy.stats import zscore


# In[2]:


sierraleone_data = pd.read_csv('../data/sierraleone-bumbuna.csv')  


# In[3]:


#Summary Statistics
summary_stats = sierraleone_data.describe()

print("Summary Statistics:\n", summary_stats)


# In[4]:


# Check for missing values
missing_values = sierraleone_data.isnull().sum()
# print("Missing Values:\n", missing_values)

for column in ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']:
    sierraleone_data[column].fillna(sierraleone_data[column].median())

# Optionally, drop columns with too many missing values or rows with missing values in critical columns
# sierraleone_data.dropna(subset=['GHI', 'DNI', 'DHI',],)


# In[5]:


# Check for outliers (e.g., in GHI, DNI, DHI)
outliers = sierraleone_data[(sierraleone_data['GHI'] < 0) | (sierraleone_data['DNI'] < 0) | (sierraleone_data['DHI'] < 0)]
# print("Outliers:\n", outliers)


# In[6]:


# Convert Timestamp to datetime
sierraleone_data['Timestamp'] = pd.to_datetime(sierraleone_data['Timestamp'])


# In[7]:


# Plot time series for GHI, DNI, DHI, Tamb
plt.figure(figsize=(12, 6))
plt.plot(sierraleone_data['Timestamp'], sierraleone_data['GHI'], label='GHI')
plt.plot(sierraleone_data['Timestamp'], sierraleone_data['DNI'], label='DNI')
plt.plot(sierraleone_data['Timestamp'], sierraleone_data['DHI'], label='DHI')
plt.plot(sierraleone_data['Timestamp'], sierraleone_data['Tamb'], label='Tamb')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Time Series of GHI, DNI, DHI, Tamb')
plt.legend()
plt.show()


# In[8]:


# Compare ModA and ModB readings before and after cleaning
cleaned_data = sierraleone_data[sierraleone_data['Cleaning'] == 1]
uncleaned_data = sierraleone_data[sierraleone_data['Cleaning'] == 0]

plt.figure(figsize=(12, 6))
plt.plot(cleaned_data['Timestamp'], cleaned_data['ModA'], label='ModA (Cleaned)', color='green')
plt.plot(uncleaned_data['Timestamp'], uncleaned_data['ModA'], label='ModA (Uncleaned)', color='red')
plt.xlabel('Time')
plt.ylabel('ModA Value')
plt.title('Impact of Cleaning on ModA Readings')
plt.legend()
plt.show()


# In[9]:


# Correlation heatmap
# plt.figure(figsize=(10, 8))
corr = sierraleone_data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# In[10]:


# Polar plot for wind speed and direction

plt.figure(figsize=(8, 8))
plt.subplot(projection='polar')
plt.scatter(sierraleone_data['WD'] * np.pi / 180, sierraleone_data['WS'], c=sierraleone_data['WSgust'], cmap=cm.viridis, alpha=0.75)
plt.colorbar(label='Wind Gust Speed (m/s)')
plt.title('Wind Speed and Direction')
plt.show()


# In[11]:


# Scatter plot to explore the influence of RH on temperature
plt.figure(figsize=(12, 6))
plt.scatter(sierraleone_data['RH'], sierraleone_data['Tamb'], alpha=0.5)
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Temperature (°C)')
plt.title('Impact of Relative Humidity on Temperature')
plt.show()


# In[12]:


# Create histograms for GHI, DNI, DHI, WS, and temperatures
sierraleone_data[['GHI', 'DNI', 'DHI', 'WS', 'Tamb']].hist(figsize=(15, 10), bins=50)
plt.suptitle('Histograms of GHI, DNI, DHI, WS, and Temperature')
plt.show()


# In[13]:


# Z-Score Analysis

sierraleone_data['GHI_zscore'] = zscore(sierraleone_data['GHI'])
zscore_outliers = sierraleone_data[sierraleone_data['GHI_zscore'].abs() > 3]
# print("Z-Score Outliers:\n", zscore_outliers)


# In[14]:


# Bubble chart for GHI vs. Tamb vs. WS, with RH as bubble size
plt.figure(figsize=(12, 6))
plt.scatter(sierraleone_data['GHI'], sierraleone_data['Tamb'], s=sierraleone_data['RH']*10, alpha=0.5, c=sierraleone_data['WS'], cmap='viridis')
plt.colorbar(label='Wind Speed (m/s)')
plt.xlabel('GHI (W/m²)')
plt.ylabel('Ambient Temperature (°C)')
plt.title('Bubble Chart: GHI vs. Tamb vs. WS (Bubble Size: RH)')
plt.show()


# In[15]:


# Handle missing values 


# In[16]:


# 1) Drop rows with missing data
sierraleone_data_cleaned = sierraleone_data.dropna(axis=1, how='all')  
print("Cleaned Data:\n", sierraleone_data_cleaned.head())


# In[17]:


# 2) Filling with median 
sierraleone_data_cleaned = sierraleone_data_cleaned.copy()
sierraleone_data_cleaned = fill_missing_values(sierraleone_data_cleaned)
print("Cleaned Data:\n", sierraleone_data_cleaned.head())


# In[ ]:





# In[ ]:





# In[ ]:




