import streamlit as st
import pandas as pd

def albumes():
  df = pd.read_csv('taylor_swift_spotify.csv')

  st.title('Álbumes')
  alb = st.selectbox('Elige un álbum para ver sus canciones y videos musicales disponibles',['Taylor Swift','Fearless','Speak Now','Red','1989','Reputation','Lover','Folklore','Evermore','Midnights','The Tortured Poets Department'])
                                                                                     
  if alb == 'Taylor Swift':
    st.image('logos/debut.png')
  else:
    st.write('si')
  
