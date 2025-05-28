import folium
from branca.colormap import linear
import geopandas as gpd

# Se cargan los datos del GeoJSON generado por process_data.py
gdf = gpd.read_file('arsat2_cobertura.geojson')

# Se crea un mapa centrado en Sudamérica
m = folium.Map(location=[-30, -60], zoom_start=4)

# Función para convertir color hexadecimal a RGB
def hex_to_rgb(hex_color):
    hex_color = str(hex_color).lstrip('#')
    # Se confirma que el valor de color tenga 6 caracteres
    if len(hex_color) == 3:
        hex_color = ''.join([c * 2 for c in hex_color])
    elif len(hex_color) != 6:
        # Valor por defecto (verde) si el color no es válido
        return (0, 128, 0)
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Se añaden los polígonos al mapa
for _, row in gdf.iterrows():
    # Convertir el color hexadecimal a RGB
    color_hex = f"{int(row['color']):06x}"  # Se asegura que tenga 6 dígitos
    color_rgb = hex_to_rgb(color_hex)
    
    # Se crea el polígono con estilo de colores 
    folium.GeoJson(
        row['geometry'],
        style_function=lambda x, color=color_rgb: {
            'fillColor': f'rgb{color}',
            'color': f'rgb{color}',
            'weight': 1,
            'fillOpacity': 0.5
        },
        tooltip=f"ARSAT-2 Cobertura (ID: {row['id']})"
    ).add_to(m)

# Se añade control de capas
folium.LayerControl().add_to(m)

# Se guarda el mapa como archivo HTML
m.save('arsat2_cobertura_map.html')

print("Mapa interactivo creado y guardado como 'arsat2_cobertura_map.html'")