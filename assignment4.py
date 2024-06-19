import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset
csv_file_path = 'CO2_Temperature_Anomalies.csv'
merged_data = pd.read_csv(csv_file_path)

# Plotting the data
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot CO2 emissions
ax1.set_xlabel('Year')
ax1.set_ylabel('CO2 Emissions (MtCO2)', color='tab:blue')
ax1.plot(merged_data['Year'], merged_data['CO2 Emissions (MtCO2)'], color='tab:blue', label='CO2 Emissions')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis for temperature anomalies
ax2 = ax1.twinx()
ax2.set_ylabel('Temperature Anomalies (°C)', color='tab:red')
ax2.plot(merged_data['Year'], merged_data['Temperature Anomalies (°C)'], color='tab:red', label='Temperature Anomalies')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Adding title and legend
plt.title('Global CO2 Emissions and Temperature Anomalies Over Time')
fig.tight_layout()

# Show plot
plt.show()
