#!/usr/bin/env python
# coding: utf-8

# In[141]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
import seaborn as sns
from scipy.stats import zscore


# BENIN DATA ANALYSIS

# In[168]:


benin_data = pd.read_csv('../data/sierraleone-bumbuna.csv')  
benin_data.shape


# In[170]:


#Summary Statistics
summary_stats = benin_data.describe()

print("Summary Statistics:\n", summary_stats)


# In[144]:


# Check for missing values
missing_values = benin_data.isnull().sum()
print("Missing Values:\n", missing_values)

for column in ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']:
    benin_data[column].fillna(benin_data[column].median())

# Optionally, drop columns with too many missing values or rows with missing values in critical columns
benin_data.dropna(subset=['GHI', 'DNI', 'DHI',],)


# In[145]:


# Check for outliers (e.g., in GHI, DNI, DHI)
outliers = benin_data[(benin_data['GHI'] < 0) | (benin_data['DNI'] < 0) | (benin_data['DHI'] < 0)]
print("Outliers:\n", outliers)


# In[146]:


# Convert Timestamp to datetime
benin_data['Timestamp'] = pd.to_datetime(benin_data['Timestamp'])


# In[171]:


# Plot time series for GHI, DNI, DHI, Tamb
plt.figure(figsize=(12, 6))
plt.plot(benin_data['Timestamp'], benin_data['GHI'], label='GHI')
plt.plot(benin_data['Timestamp'], benin_data['DNI'], label='DNI')
plt.plot(benin_data['Timestamp'], benin_data['DHI'], label='DHI')
plt.plot(benin_data['Timestamp'], benin_data['Tamb'], label='Tamb')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Time Series of GHI, DNI, DHI, Tamb')
plt.legend()
plt.show()


# In[148]:


# Compare ModA and ModB readings before and after cleaning
cleaned_data = benin_data[benin_data['Cleaning'] == 1]
uncleaned_data = benin_data[benin_data['Cleaning'] == 0]

plt.figure(figsize=(12, 6))
plt.plot(cleaned_data['Timestamp'], cleaned_data['ModA'], label='ModA (Cleaned)', color='green')
plt.plot(uncleaned_data['Timestamp'], uncleaned_data['ModA'], label='ModA (Uncleaned)', color='red')
plt.xlabel('Time')
plt.ylabel('ModA Value')
plt.title('Impact of Cleaning on ModA Readings')
plt.legend()
plt.show()


# In[149]:


# Correlation heatmap
plt.figure(figsize=(10, 8))
corr = benin_data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# In[150]:


# Polar plot for wind speed and direction

plt.figure(figsize=(8, 8))
plt.subplot(projection='polar')
plt.scatter(benin_data['WD'] * np.pi / 180, benin_data['WS'], c=benin_data['WSgust'], cmap=cm.viridis, alpha=0.75)
plt.colorbar(label='Wind Gust Speed (m/s)')
plt.title('Wind Speed and Direction')
plt.show()


# In[151]:


# Scatter plot to explore the influence of RH on temperature
plt.figure(figsize=(12, 6))
plt.scatter(benin_data['RH'], benin_data['Tamb'], alpha=0.5)
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Temperature (°C)')
plt.title('Impact of Relative Humidity on Temperature')
plt.show()


# In[152]:


# Create histograms for GHI, DNI, DHI, WS, and temperatures
benin_data[['GHI', 'DNI', 'DHI', 'WS', 'Tamb']].hist(figsize=(15, 10), bins=50)
plt.suptitle('Histograms of GHI, DNI, DHI, WS, and Temperature')
plt.show()


# In[153]:


# Z-Score Analysis

benin_data['GHI_zscore'] = zscore(benin_data['GHI'])
zscore_outliers = benin_data[benin_data['GHI_zscore'].abs() > 3]
print("Z-Score Outliers:\n", zscore_outliers)


# In[154]:


# Bubble chart for GHI vs. Tamb vs. WS, with RH as bubble size
plt.figure(figsize=(12, 6))
plt.scatter(benin_data['GHI'], benin_data['Tamb'], s=benin_data['RH']*10, alpha=0.5, c=benin_data['WS'], cmap='viridis')
plt.colorbar(label='Wind Speed (m/s)')
plt.xlabel('GHI (W/m²)')
plt.ylabel('Ambient Temperature (°C)')
plt.title('Bubble Chart: GHI vs. Tamb vs. WS (Bubble Size: RH)')
plt.show()


# In[155]:


# Handle missing values 


# In[162]:


# 1) Drop rows with missing data
benin_data_cleaned = benin_data.dropna(axis=1, how='all')  
# print("Cleaned Data:\n", benin_data_cleaned.head())


# In[163]:


# 2) Filling with median 


# In[166]:


benin_data_cleaned = benin_data_cleaned.copy()

benin_data_cleaned = fill_missing_values(benin_data_cleaned)

print("Cleaned Data:\n", benin_data_cleaned.head())
