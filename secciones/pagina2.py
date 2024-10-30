import streamlit as st
import requests

def albumes():
  df = pd.read_csv('taylor_swift_spotify.csv',sep=';')

