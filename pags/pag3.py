import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def analisis():
  df = pd.read_csv('taylor_swift_spotify.csv')
  st.title('Número de Canciones por Álbum')
  albs = ["Taylor Swift (Deluxe Edition)","Fearless (Taylor's Version)","Speak Now (Taylor's Version)", "Red (Taylor's Version","1989 (Taylor's Version) [Deluxe]","reputation","Lover","folklore (deluxe version)","evermore (deluxe version)","Midnights (The Til Dawn Edition)","THE TORTURED POETS DEPARTMENT: THE ANTHOLOGY"]
  ab = df[df['album'].isin(albs)]
  cpa = ab.value_counts()
  colores = ['yellow','red','green','pink','hotpink','khaki','blue','lightblue','orange','fuchsia']
  fig, ax = plt.subplots()
  ax.pie(ab, labels=ab.index, autopct='%1.1f%%', startangle=45,colors=colores)
  st.pyplot(fig)
