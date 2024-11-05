import pandas as pd
import streamlit as st

def recs():
  st.title('Recomendaciones')
  st.write('Este es un sistema de recomendaciones de canciones. Puedes seleccionar entre varias opciones para encontrar alguna canción que se ajuste a tí, por ejemplo, canciones bailables, versiones en vivo, acústicas, etc. ¡Elige lo que más se acomode a lo que deseas!')
  recom = st.radio('Quiero una canción...',['similar a una que ya conozco','de un estilo específico'])

  df = pd.read_csv('taylor_swift_spotify.csv')
  
  if recom == 'similar a una que ya conozco':
    st.write('¡Genial! Selecciona la canción que deseas')
  elif recom == 'de un estilo específico':
    st.write('¿Qué estilo buscas?')
    
