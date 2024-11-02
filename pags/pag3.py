import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

def analisis():
    st.title('Análisis gráfico')
    df = pd.read_csv('taylor_swift_spotify.csv')
    albs = ["Taylor Swift (Deluxe Edition)","Fearless (Taylor's Version)","Speak Now (Taylor's Version)", "Red (Taylor's Version","1989 (Taylor's Version) [Deluxe]","reputation","Lover","folklore (deluxe version)","evermore (deluxe version)","Midnights (The Til Dawn Edition)","THE TORTURED POETS DEPARTMENT: THE ANTHOLOGY"]
    fd = df[df['album'].isin(albs)]
    cpa = fd.groupby('album').size().reset_index(name='canciones')
    labels = cpa['album'].tolist()
    values = cpa['canciones'].tolist()
    gpie = {
        "title": {"text": " ", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "horizontal", "left": "left",},
        "series": [
            {
                "name": "Álbum",
                "type": "pie",
                "radius": "50%",
                "data": [{"value": v, "name": l} for v, l in zip(values, labels)],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
        "color": ["lightskyblue", "gold", "hotpink","steelblue","purple","beige","limegreen","sienna","silver","dimgray"]
    }
    st.subheader('Porcentaje de Canciones por Álbumes')
    st_echarts(
        options=gpie, height="600px",
    )
    #Grafico 2
    fd2 = df[df['album'].isin(albs)]
    pivot_df = fd2.pivot(index='track_number', columns='album', values='popularity').fillna(0)
    
    # Prepare the data for ECharts
    glinea = {
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
                'type': 'line'
            }
        },
        'legend': {
            'data': pivot_df.columns.tolist()
        },
        'xAxis': {
            'type': 'category',
            'data': pivot_df.index.tolist()
        },
        'yAxis': {
            'type': 'value'
        },
        'series': []
    }
    kolors = ["lightskyblue", "gold", "hotpink","steelblue","purple","beige","limegreen","sienna","silver","dimgray"]
    for i, album in enumerate(pivot_df.columns):
        glinea['series'].append({
            'name': album,
            'type': 'line',
            'stack': 'total',
            'data': pivot_df[album].tolist(),
            'smooth': True,
            'itemStyle': {
                'color': kolors[i % len(kolors)]
            }
        })
    st.subheader('Popularidad de Canciones por Álbum')
    st_echarts(options=glinea,height='600px')
    #Grafico 3
    
    fd3 = df[df['album'].isin(albs)]
    popularity_by_album = fd3.groupby('album')['popularity'].mean().reset_index()
    # Configurar el gráfico de barras
    option = {
        'dataset': {
        'source': [
            ['popularity', 'album'],
        ] + fd3[['popularity', 'album']].values.tolist()  # Añadir datos
        },
        'grid': {'containLabel': True},
        'xAxis': {'name': 'Popularity'},
        'yAxis': {'type': 'category'},
        'visualMap': {
            'orient': 'horizontal',
            'left': 'center',
            'min': 0,
            'max': 100,
            'text': ['High Popularity', 'Low Popularity'],
            'dimension': 0,  # Usar la columna de popularidad para el mapeo
            'inRange': {
                'color': ['#65B581', '#FFCE34', '#FD665F']  # Colores para el rango de popularidad
            }
        },
        'series': [
            {
                'type': 'bar',
                'encode': {
                    'x': 'popularity',  # Mapear popularidad al eje X
                    'y': 'album'  # Mapear álbum al eje Y
                    }
                }
            ]
        }
    
    # Mostrar en Streamlit
    st_pyecharts(option)
