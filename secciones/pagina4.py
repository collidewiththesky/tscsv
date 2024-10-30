import streamlit as st
import requests

def recs():
  df = pd.read_csv('taylor_swift_spotify.csv',sep=';')
