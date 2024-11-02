import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

def analisis():
    data = pd.read_csv('taylor_swift_spotify.csv')
    albumes_seleccionados = ['Fearless (Platinum Edition)', '1989', 'Lover']

    # Filtrar el DataFrame para incluir solo los álbumes seleccionados
    data_filtrada = data[data['album'].isin(albumes_seleccionados)]

    # Contar el número de canciones por álbum
    album_counts = data_filtrada['album'].value_counts().reset_index()
    album_counts.columns = ['album', 'canciones']
    options = {
        "title": {"text": "Porcentaje de Canciones por Álbum", "left": "center"},
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

