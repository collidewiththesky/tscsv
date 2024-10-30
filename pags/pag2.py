import streamlit as st
import pandas as pd
import logos

def albums():
  st.header('Álbumes')
  alb = st.selectbox(
    'Elige un álbum:',
    ('Taylor Swift','Fearless','Speak Now','Red','1989','Reputation','Lover','Folklore','Evermore','Midnights','The Tortured Poets Department'),
  )
                                                                                     
  if alb == 'Taylor Swift':
    st.write('Elegiste:')
    st.image('logos/debut.png')
  elif alb == 'Fearless':
    st.image('logos/fearless.png')
  else:
    st.write('si)
    
  
