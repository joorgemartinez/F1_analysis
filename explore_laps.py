import pandas as pd

# Cargar el CSV
df = pd.read_csv("laps_spain_2024.csv")

# Mostrar las primeras filas
print("📄 Primeras filas:")
print(df.head())

# Ver columnas disponibles
print("\n🧾 Columnas:")
print(df.columns.tolist())

# Ver resumen general del DataFrame
print("\n📊 Info:")
print(df.info())

# Ver número de vueltas por piloto
print("\n🏁 Vueltas por piloto:")
if "driver_number" in df.columns:
    print(df['driver_number'].value_counts())
else:
    print("⚠️ No se encontró la columna 'driver_number'")
