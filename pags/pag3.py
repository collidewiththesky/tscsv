import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

def analisis():
  data = pd.read_csv('taylor_swift_spotify.csv')
  
  # Definir los álbumes que deseas incluir
  albumes_seleccionados = ["Taylor Swift (Deluxe Edition)","Fearless (Taylor's Version)","Speak Now (Taylor's Version)", "Red (Taylor's Version","1989 (Taylor's Version) [Deluxe]","reputation","Lover","folklore (deluxe version)","evermore (deluxe version)","Midnights (The Til Dawn Edition)","THE TORTURED POETS DEPARTMENT: THE ANTHOLOGY"]
  
  # Filtrar el DataFrame para incluir solo los álbumes seleccionados
  data_filtrada = data[data['album'].isin(albumes_seleccionados)]
  
  # Contar el número de canciones por álbum
  album_counts = data_filtrada['album'].value_counts().reset_index()
  album_counts.columns = ['album', 'canciones']
  
  # Configurar la página
  st.title('Número de Canciones por Álbumes Seleccionados de Taylor Swift')
  
  # Crear el gráfico de torta con st_echarts
  options = {
        "title": {"text": "某站点用户访问来源", "subtext": "纯属虚构", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical", "left": "left",},
        "series": [
            {
                "name": "访问来源",
                "type": "pie",
                "radius": "50%",
                "data": album_counts,
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }
    st_echarts(
        options=options, height="600px",
    )
