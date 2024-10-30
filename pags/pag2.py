import streamlit as st
import pandas as pd

def albums():
  st.title('Álbumes')
  alb = st.selectbox('Elige un álbum:',['Taylor Swift','Fearless','Speak Now','Red','1989','Reputation','Lover','Folklore','Evermore','Midnights','The Tortured Poets Department'])
                                                                                     
  if alb == 'Taylor Swift':
    st.image('logos/debut.png')
  else:
    st.write('si')
  
