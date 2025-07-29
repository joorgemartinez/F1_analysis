import pandas as pd
import matplotlib.pyplot as plt


# Función para formatear segundos a mm:ss.SSS
def format_time(seconds):
    if pd.isna(seconds):
        return ""
    minutes = int(seconds // 60)
    sec = seconds % 60
    return f"{minutes}:{sec:06.3f}"  # ejemplo: 1:20.567

# Cargar el archivo ya con nombres
df = pd.read_csv("laps_spain_2024_named.csv")

# Excluir vueltas justo después de salir de boxes
df_clean = df[~df["is_pit_out_lap"]]

# Agrupar por piloto y calcular media
media_por_piloto = (
    df_clean.groupby("broadcast_name")["lap_duration"]
    .mean()
    .sort_values()
)
# Aplicar formato a texto legible
media_formateada = media_por_piloto.apply(format_time)

print("⏱️ Tiempos medios por vuelta:")
print(media_formateada)

# Opcional: gráfico usando segundos
media_por_piloto.plot(kind="barh", figsize=(10, 8), title="Tiempo medio por vuelta")
plt.xlabel("Duración (segundos)")
plt.tight_layout()
plt.show()