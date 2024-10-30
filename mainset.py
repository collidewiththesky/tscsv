import streamlit as st
import requests

paginas = {
  'Inicio' : 'p1',
  'Albumes' : 'p2',
  'Análisis' : 'p3',
  'Recomendaciones' : 'p4'
}

elegir = st.sidebar.selectbox('Ir a:',list(paginas.keys()))

if elegir == 'Inicio':
  import secciones.hmpage
  secciones.hmpage.home()
elif elegir == 'Albumes':
  import secciones.pagina2
  secciones.pagina2.albumes()
elif elegir == 'Análisis':
  import secciones.pagina3
  secciones.pagina3.analisis()
elif elegir == 'Recomendaciones':
  import secciones.pagina4
  secciones.pagina4.recs()
