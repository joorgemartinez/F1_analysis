import pandas as pd
import matplotlib.pyplot as plt


# Función para formatear segundos a mm:ss.SSS
def format_time(seconds):
    if pd.isna(seconds):
        return ""
    minutes = int(seconds // 60)
    sec = seconds % 60
    return f"{minutes}:{sec:06.3f}"  # ejemplo: 1:20.567

# Diccionario de colores por equipo
team_colors = {
    "Red Bull Racing": "#1E41FF",
    "Ferrari": "#DC0000",
    "Mercedes": "#00D2BE",
    "McLaren": "#FF8700",
    "Aston Martin": "#006F62",
    "Alpine": "#0090FF",
    "Williams": "#005AFF",
    "Kick Sauber": "#52E252",
    "RB": "#6692FF",
    "Haas F1 Team": "#B6BABD"
}

# Cargar el archivo ya con nombres
df = pd.read_csv("laps_spain_2024_named.csv")

# Excluir vueltas justo después de salir de boxes (Son outliers)
df_clean = df[~df["is_pit_out_lap"]]

# Agrupar por piloto y calcular media
media_por_piloto = (
    df_clean.groupby(["broadcast_name", "team_name"])["lap_duration"]
    .mean()
    .sort_values()
)

# Convertir a DataFrame y aplicar color y formato de tiempo
df_final = media_por_piloto.reset_index()
df_final["color"] = df_final["team_name"].map(team_colors)
df_final["formatted_time"] = df_final["lap_duration"].apply(format_time)

# Crear gráfico de barras horizontal con colores por equipo
plt.figure(figsize=(10, 8))
bars = plt.barh(df_final["broadcast_name"], df_final["lap_duration"], color=df_final["color"])

# Añadir etiquetas con el tiempo formateado a la derecha de cada barra
for bar, label in zip(bars, df_final["formatted_time"]):
    plt.text(
        bar.get_width() + 0.2,  # un poco a la derecha del final de la barra
        bar.get_y() + bar.get_height() / 2,
        label,
        va="center"
    )

plt.xlabel("Duración media (segundos)")
plt.title("Tiempo medio por vuelta - GP España 2024")
plt.tight_layout()
plt.savefig("tiempos_medios.png", dpi=300, bbox_inches="tight")
plt.show()

