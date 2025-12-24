import requests
from datetime import datetime, timedelta
import pandas as pd  
import matplotlib.pyplot as plt            



#Calculate Dates
today = datetime.now()
next_days = today + timedelta(days=7)

#Format Dates for API
start_date = today.strftime("%Y-%m-%d")
end_date = next_days.strftime("%Y-%m-%d")

#API Call
url = f"https://api.open-meteo.com/v1/forecast?latitude=24.9048&longitude=91.8600&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data = response.json()
print(data)



#--------------------------------
#Load With pandas

daily_data = data["daily"]

df = pd.DataFrame({
    'date': daily_data['time'],
    'Max_temp': daily_data['temperature_2m_max'],
    'Min_temp': daily_data['temperature_2m_min']
})
df['date'] = pd.to_datetime(df['date'])

print(df)



#---------------------------------
#Visualize the data

plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['Max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['Min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Sylhet Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

