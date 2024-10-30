import streamlit as st
import requests

paginas = {
  'Inicio' : 'p1',
  'Albumes' : 'p2',
  'Análisis' : 'p3'
}

elegir = st.sidebar.selectbox('Ir a:',list(paginas.keys()))

if elegir == 'Inicio':
    import secciones.pagina1
    secciones.pagina1.inicio()
elif elegir == 'Albumes':
    import secciones.pagina2
    secciones.pagina2.albumes()
elif elegir == 'Análisis':
    import secciones.pagina3
    secciones.pagina3.analisis()
