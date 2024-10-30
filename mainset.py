import streamlit as st
import requests
from secciones import hmpage, pagina2, pagina3, pagina4

elegir = st.sidebar.selectbox('Ir a:',['Inicio','Álbumes','Análisis','Recomendaciones'])

if elegir == 'Inicio':
  hmpage.home()
elif elegir == 'Albumes':
  pagina2.albumes()
elif elegir == 'Análisis':
  pagina3.analisis()
elif elegir == 'Recomendaciones':
  pagina4.recs()
