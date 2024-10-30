import streamlit as st
import requests
from pags import homepage, pag2, pag3, pag4

elegir = st.sidebar.selectbox('Ir a:',['Inicio','Álbumes','Análisis','Recomendaciones'])

if elegir == 'Inicio':
  homepage.pginicio()
elif elegir == 'Albumes':
  pag2.albumes()
elif elegir == 'Análisis':
  pag3.analisis()
elif elegir == 'Recomendaciones':
  pag4.recs()
