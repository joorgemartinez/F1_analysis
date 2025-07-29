import requests
import pandas as pd

import requests
import pandas as pd

# Endpoint de vueltas
url = "https://api.openf1.org/v1/laps"
params = {
    "session_key": 9539  # GP de España 2024
}

response = requests.get(url, params=params)

if response.status_code == 200:
    df = pd.DataFrame(response.json())
    df.to_csv("laps_spain_2024.csv", index=False)
    print("✅ Datos guardados en laps_spain_2024.csv")
    print(df.head())
else:
    print(f"❌ Error al hacer la petición: {response.status_code}")


