import requests
import pandas as pd

url = "https://api.openf1.org/v1/sessions"
response = requests.get(url)

if response.status_code == 200:
    df = pd.DataFrame(response.json())

    # Mostramos las columnas disponibles
    print("🧾 Columnas disponibles:")
    print(df.columns)

    # Filtrar por carreras en España (Spain)
    spain_races = df[(df['country_name'] == 'Spain') & (df['session_type'] == 'Race')]

    print("\n📊 Carreras en España:")
    print(spain_races[['session_key', 'year', 'location', 'meeting_key']])
else:
    print(f"❌ Error al hacer la petición: {response.status_code}")
