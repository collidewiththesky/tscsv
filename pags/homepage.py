import streamlit as st
import requests

def pginicio():
  try:
    st.title('Taylor Swift')
    st.subheader('Álbumes, análisis de Spotify y recomendaciones de canciones')
    st.markdown('![Taylor Swift en el Eras Tour](https://64.media.tumblr.com/816f0834b6114424000d9b0ea5d1e541/36575a8dabee0ec2-cc/s540x810/0cad0d55b358f3c3069e5cf8626829dd38c73074.gifv'))
    st.link_button('Página oficial de Taylor Swift','https://www.taylorswift.com/')
  except ImportError as e:
    st.error(f"Error al importar: {e}")
  except AttributeError as e:
    st.error(f"Error al llamar a la función: {e}")
