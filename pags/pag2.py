import streamlit as st
import pandas as pd
import logos
import spotifyAPI

def albums():
  st.header('Albumes')
  alb = st.selectbox(
    'Elige un álbum:',
    ('Taylor Swift','Fearless','Speak Now','Red','1989','Reputation','Lover','Folklore','Evermore','Midnights','The Tortured Poets Department'),
  )

  df = pd.read_csv('taylor_swift_spotify.csv')
                                                                                     
  if alb == 'Taylor Swift':
    st.image('logos/debut.png')
    albumts = "Taylor Swift (Deluxe Edition)"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
    iframe_code = f"""
      <iframe src="https://open.spotify.com/intl-es/album/5eyZZoQEFQWRHkV2xgAeBw" 
              width="300" 
              height="380" 
              frameBorder="0" 
              allowTransparency="true" 
              allow="encrypted-media">
      </iframe>
      """
        st.markdown(iframe_code, unsafe_allow_html=True)
  elif alb == 'Fearless':
    st.image('logos/fearless.png')
    albumts = "Fearless (Taylor's Version)"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
  elif alb == 'Speak Now':
    st.image('logos/sntv.png',width=500)
    albumts = "Speak Now (Taylor's Version)"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
  elif alb == 'Red':
    st.image('logos/red tv.png', width=200)
    albumts = "Red (Taylor's Version)"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
  elif alb == '1989':
    st.image('logos/1989tv.png',width=500)
    albumts = "1989 (Taylor's Version)"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
  elif alb == 'Reputation':
    st.image('logos/rep.png')
    albumts = "reputation"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
  elif alb == 'Lover':
    st.image('logos/lover.png')
    albumts = "Lover"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
  elif alb == 'Folklore':
    st.image('logos/folklore.png')
    albumts = "folklore (deluxe version)"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
  elif alb == 'Evermore':
    st.image('logos/evermore.png')
    albumts = "evermore (deluxe version)"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
  elif alb == 'Midnights':
    st.image('logos/midnights.png')
    albumts = "Midnights (The Til Dawn Edition)"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
  elif alb == 'The Tortured Poets Department':
    st.image('logos/ttpd.png')
    albumts = "THE TORTURED POETS DEPARTMENT: THE ANTHOLOGY"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
    
  
