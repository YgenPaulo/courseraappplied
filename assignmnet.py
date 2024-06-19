import pandas as pd


co2_url = 'https://github.com/owid/co2-data/raw/master/owid-co2-data.csv'
temp_url = 'https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv'

co2_data = pd.read_csv(co2_url)
temp_data = pd.read_csv(temp_url, skiprows=1)

# Filter the CO2 data for global emissions and relevant columns
co2_data_filtered = co2_data[['year', 'co2']].dropna()

# Rename columns for temperature data for clarity
temp_data.columns = ['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'J-D', 'D-N', 'DJF', 'MAM', 'JJA', 'SON']

# Filter the temperature data for the annual mean (J-D column)
temp_data_filtered = temp_data[['Year', 'J-D']].dropna()

# Merge the datasets on the year column
merged_data = pd.merge(co2_data_filtered, temp_data_filtered, left_on='year', right_on='Year').drop(columns=['Year'])

# Create the merged dataset to save as CSV
merged_data_csv = merged_data[['year', 'co2', 'J-D']]
merged_data_csv.columns = ['Year', 'CO2 Emissions (MtCO2)', 'Temperature Anomalies (°C)']

# Save the merged dataset to a CSV file
csv_file_path = 'CO2_Temperature_Anomalies.csv'
merged_data_csv.to_csv(csv_file_path, index=False)

print(f"The merged dataset has been saved to {csv_file_path}")
