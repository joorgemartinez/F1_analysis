import requests
import pandas as pd

# Obtener los pilotos de la carrera de España 2024
url = "https://api.openf1.org/v1/drivers"
params = {
    "session_key": 9539 # Session Key de la carrera de España 2024
}

response = requests.get(url, params=params)

if response.status_code == 200:
    df_drivers = pd.DataFrame(response.json())
    df_drivers = df_drivers[['driver_number', 'broadcast_name']].drop_duplicates()
    print(df_drivers)
else:
    print(f"Error: {response.status_code}")

# Cargar vueltas
df_laps = pd.read_csv("laps_spain_2024.csv")

# Unir los nombres al DataFrame original
df_laps = df_laps.merge(df_drivers, on="driver_number", how="left")

# Guardamos una nueva versión
df_laps.to_csv("laps_spain_2024_named.csv", index=False)

print("✅ Archivo guardado con nombres: laps_spain_2024_named.csv")