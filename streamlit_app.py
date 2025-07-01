import folium
from streamlit_folium import st_folium
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Enchentes RS", layout="centered", page_icon = '🌩️')

# Título do aplicativo
st.subheader("Visualização da enchente no RS por imagem de Satélite")

geometry = {"type":"Polygon","coordinates":[[[-53.031349,-30.14869],[-53.031349,-29.973673],[-52.767677,-29.973673],[-52.767677,-30.14869],[-53.031349,-30.14869]]]}

coordinates = geometry["coordinates"][0]

min_lon = min(coord[0] for coord in coordinates)
max_lon = max(coord[0] for coord in coordinates)
min_lat = min(coord[1] for coord in coordinates)
max_lat = max(coord[1] for coord in coordinates)

bounds = [[min_lat, min_lon], [max_lat, max_lon]]

center_lat = (min_lat + max_lat) / 2
center_lon = (min_lon + max_lon) / 2

center_point = [center_lat, center_lon]

m = folium.Map(center_point, zoom_start=12, control = False)

# Adicionar a camada openstreetmap de tile
folium.TileLayer('openstreetmap', control = False).add_to(m)

# Adicionar a camada Stamen Terrain de tile


imagem_1 = folium.raster_layers.ImageOverlay(
    image="2025-06-30-00_00_2025-06-30-23_59_Sentinel-2_L2A_SWIR (1).jpg",
    name="30 de junho de 2025",
    bounds=bounds,
    opacity=0.8,
    interactive=False,
    cross_origin=False,
    zindex=1,
    alt="Mapa Cachoeira do Sul",
    overlay = False,
    show = False
)


imagem_1.add_to(m)

imagem_2 = folium.raster_layers.ImageOverlay(
    image="2025-06-25-00_00_2025-06-25-23_59_Sentinel-2_L2A_SWIR (2).jpg",
    name="25 de junho de 2025",
    bounds=bounds,
    opacity=0.8,
    interactive=False,
    cross_origin=False,
    zindex=1,
    alt="Mapa Cachoeira do Sul",
    overlay = False,
    show = False
)


imagem_2.add_to(m)

imagem = folium.raster_layers.ImageOverlay(
    image="2025-05-11-00_00_2025-05-11-23_59_Sentinel-2_L2A_SWIR.jpg",
    name="11 de maio de 2025",
    bounds=bounds,
    opacity=0.8,
    interactive=False,
    cross_origin=False,
    zindex=1,
    alt="Mapa Cachoeira do Sul",
    overlay = False,
    show = False
)


imagem.add_to(m)


imagem = folium.raster_layers.ImageOverlay(
    image="2024-05-06-00_00_2024-05-06-23_59_Sentinel-2_L2A_SWIR.jpg",
    name="06 de maio de 2024",
    bounds=bounds,
    opacity=0.8,
    interactive=False,
    cross_origin=False,
    zindex=1,
    alt="Mapa Cachoeira do Sul",
    overlay = False,
    show = False
)


imagem.add_to(m)

folium.LayerControl().add_to(m)


st_folium(m, width=300, height = 500, returned_objects=[])
