import matplotlib.pyplot as plt
import pandas as pd

def analisis():
  df = pd.read_csv('taylor_swift_spotify.csv')
  st.title('Número de Canciones por Álbum')
  cpa = df['album'].value_counts()
  colores = ['yellow','red','green','pink','hotpink','khaki','blue','lightblue','orange','fuchsia']
  fig, ax = plt.subplots()
  ax.pie(cpa, labels=cpa.index, autopct='%1.1f%%', startangle=45,colors=colores)
  st.pyplot(fig)
