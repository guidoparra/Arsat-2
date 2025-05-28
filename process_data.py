import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
import ast
import numpy as np

# Lectura de archivo CSV
file_path = 'datos-cobertura-banda-ku-arsat2-sudamerica-v2.csv'
df = pd.read_csv(file_path, header=None)

# Se analiza la estructura del archivo
print("Estructura del archivo:")
print(df.head())
print("\nInformación del DataFrame:")
print(df.info())

# Procesamiento de columnas en cuanto a coordenadas
def parse_coordinates(coord_str):
    try:
        # Eliminar comillas si existen y dividir los puntos
        coord_str = coord_str.replace('"', '')
        points = coord_str.split(' ')
        # Convertir cada punto a una tupla de coordenadas
        coords = [tuple(map(float, point.split(','))) for point in points if point]
        return coords
    except Exception as e:
        print(f"Error al procesar coordenadas: {e}")
        return None

# Se crea un GeoDataFrame para almacenar los polígonos
polygons = []
colors = []
ids = []

for index, row in df.iterrows():
    if pd.notna(row[2]):  # La columna 2 contiene las coordenadas
        coords = parse_coordinates(row[2])
        if coords and len(coords) > 2:  # Se necesita al menos 3 puntos para un polígono
            polygon = Polygon(coords)
            polygons.append(polygon)
            colors.append(row[7])  # Columna 7 contiene el color
            ids.append(row[5])     # Columna 5 contiene el ID

# Se crea GeoDataFrame
gdf = gpd.GeoDataFrame({
    'id': ids,
    'color': colors,
    'geometry': polygons
}, crs="EPSG:4326")  # Sistema de coordenadas WGS84

# Verificación de los datos procesados
print("\nGeoDataFrame creado:")
print(gdf.head())
print("\nInformación del GeoDataFrame:")
print(gdf.info())

# Se guardan los datos procesados en un archivo GeoJSON
gdf.to_file("arsat2_cobertura.geojson", driver='GeoJSON')