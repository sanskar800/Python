import requests  
import pandas as pd  
import seaborn as sns  
import matplotlib.pyplot as plt 
import random  

# Get data from API
response = requests.get('https://api.covid19api.com/total/country/nepal')
data = pd.read_json(response.text)

# Format data
data['Date'] = pd.to_datetime(data['Date']).dt.date  # Convert date to datetime format
data = data.groupby(['Date']).agg({'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum'}).reset_index()  # Group by date and sum the Confirmed, Deaths, and Recovered cases

# Add new column for active cases
data['Active'] = data['Confirmed'] - data['Deaths'] - data['Recovered']  # Calculate active cases as the difference between Confirmed, Deaths, and Recovered cases

# Plot data
sns.set_style('darkgrid')

# Plot confirmed cases
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Confirmed'], color='red')
plt.title('Confirmed Cases in Nepal')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.show()

# Plot active cases
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Active'], color='orange')
plt.title('Active Cases in Nepal')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.show()

# Plot recovered cases
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Recovered'], color='green')
plt.title('Recovered Cases in Nepal')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.show()

# Plot deaths
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Deaths'], color='black')
plt.title('Deaths in Nepal')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.show()
