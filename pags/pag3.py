import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

def analisis():
  df = pd.read_csv('taylor_swift_spotify.csv')
  albs = ["Taylor Swift (Deluxe Edition)","Fearless (Taylor's Version)","Speak Now (Taylor's Version)", "Red (Taylor's Version","1989 (Taylor's Version) [Deluxe]","reputation","Lover","folklore (deluxe version)","evermore (deluxe version)","Midnights (The Til Dawn Edition)","THE TORTURED POETS DEPARTMENT: THE ANTHOLOGY"]
  ab = df[df['album'].isin(albs)]
  cpa = ab['album'].value_counts().reset_index()
  colores = ['yellow','red','green','lightskyblue','mediumpurple','hotpink','peru','silver','dimgray','limegreen']
  st.title('Porcentaje de Canciones por Álbumes')

  grafikito = {
      "title": {"text": "某站点用户访问来源", "subtext": "纯属虚构", "left": "center"},
      "tooltip": {"trigger": "item"},
      "legend": {"orient": "vertical", "left": "left",},
      "series": [
          {
              "name": "Canciones",
              "type": "pie",
              "radius": "50%",
              "data": cpa.to_dict(orient='records'),
              "emphasis": {
                  "itemStyle": {
                      "shadowBlur": 10,
                      "shadowOffsetX": 0,
                      "shadowColor": "rgba(0, 0, 0, 0.5)"
                  }
              },
          }
      ],
  }
  st_echarts(grafikito=grafikito)
