# Arsat-2
Este proyecto busca conocer la cobertura y capacidad de transmisión del satélite argentino ARSAT-2 ofreciendo en dicha región utilizando frecuencias en el rango de la Banda Ku.

Objetivo
•	Procesar un archivo CSV con datos de cobertura satelital (coordenadas de polígonos y atributos como colores e IDs).
•	Convertir los datos en un GeoDataFrame y exportarlos a GeoJSON.
•	Crear un mapa interactivo con folium para visualizar las zonas de cobertura.
________________________________________
Dependencias

Librería - Uso:

pandas -	Lectura y manipulación de datos en CSV.
geopandas	- Manejo de datos geoespaciales (GeoDataFrame).
shapely -	Creación de geometrías (Polygon).
folium -	Generación del mapa interactivo.
branca.colormap	- Manejo de escalas de colores para visualización.

