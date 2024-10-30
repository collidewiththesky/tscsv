import streamlit as st
import requests
from pags import homepage, pag2, pag3, pag4

elegir = st.sidebar.selectbox('Ir a:',['Inicio','Álbumes','Análisis','Recomendaciones'])
st.sidebar.markdown('![Alt Text](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdW92a242d3AxdHZyOHpwejR1Y21mb29xMWVxdThscjNmYW42d2E5OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/KBbeJb7fvMnlJsfYWY/giphy.gif)')

if elegir == 'Inicio':
  homepage.pginicio()
elif elegir == 'Albumes':
  pag2.albumes()
elif elegir == 'Análisis':
  pag3.analisis()
elif elegir == 'Recomendaciones':
  pag4.recs()
