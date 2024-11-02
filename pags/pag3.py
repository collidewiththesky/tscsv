import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
from pyecharts import options as opts
from pyecharts.charts import Bar

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
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F39C12"]  # Añade más colores si es necesario
    numalbs = len(fd3)
    
    # Configuración del gráfico
    option = {
    "title": {
        "text": "Popularidad Promedio de Álbumes Filtrados",
        "subtext": "Datos de Taylor Swift",
        "left": "center"
    },
    "tooltip": {},
    "xAxis": {
        "type": "value"
    },
    "yAxis": {
        "type": "category",
        "data": fd3["album"].tolist()
    },
    "series": [{
        "name": "popularity",
        "type": "bar",
        "data": fd3["popularity"].tolist(),
        "itemStyle": {
            "color": {
                "type": "linear",
                "x": 0,
                "y": 0,
                "x2": 1,
                "y2": 1,
                "colorStops": [{"offset": i / numalbs, "color": colors[i]} for i in range(numalbs)]
                }
            }
        }]
    }
    
    # Mostrar el gráfico en Streamlit
    st_echarts(options=option)
