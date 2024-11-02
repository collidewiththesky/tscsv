import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

def analisis():
    df = pd.read_csv('taylor_swift_spotify.csv')
    albs = ["Taylor Swift (Deluxe Edition)","Fearless (Taylor's Version)","Speak Now (Taylor's Version)", "Red (Taylor's Version","1989 (Taylor's Version) [Deluxe]","reputation","Lover","folklore (deluxe version)","evermore (deluxe version)","Midnights (The Til Dawn Edition)","THE TORTURED POETS DEPARTMENT: THE ANTHOLOGY"]
    fd = df[df['album'].isin(albs)]
    cpa = fd.groupby('album').size().reset_index(name='canciones')
    labels = cpa['album'].tolist()
    values = cpa['canciones'].tolist()
    options = {
        "title": {"text": "Porcentaje de Canciones por Álbum", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical", "left": "left",},
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
    st_echarts(
        options=options, height="600px",
    )
    # Agrupar por álbum y calcular la media de popularidad
    fd2 = df[df['album'].isin(albs)]
    
    # Pivot the DataFrame for a stacked line graph
    pivot_df = fd2.pivot(index='track_number', columns='album', values='popularity').fillna(0)
    
    # Prepare the data for ECharts
    chart_data = {
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
    
    # Add series for each selected album
    for album in pivot_df.columns:
        chart_data['series'].append({
            'name': album,
            'type': 'line',
            'stack': 'total',
            'data': pivot_df[album].tolist(),
            'smooth': True
        })
    st_echarts(options=chart_data)
