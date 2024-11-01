import streamlit as st
import pandas as pd
import logos

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
    embed_code = """
    <iframe src="https://open.spotify.com/embed/album/5eyZZoQEFQWRHkV2xgAeBw?utm_source=generator" width="900" height="380" frameBorder="0" allowTransparency="true" allow="encrypted-media"></iframe>
    """
    st.subheader('Escucha el álbum aquí:')
    st.components.v1.html(embed_code, height=400)
  elif alb == 'Fearless':
    st.image('logos/fearless.png')
    albumts = "Fearless (Taylor's Version)"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
    embed_code = """
    <iframe src="https://open.spotify.com/embed/album/4hDok0OAJd57SGIT8xuWJH?utm_source=generator" width="900" height="380" frameBorder="0" allowTransparency="true" allow="encrypted-media"></iframe>
    """
    st.subheader('Escucha el álbum aquí:')
    st.components.v1.html(embed_code, height=400)
  elif alb == 'Speak Now':
    st.image('logos/sntv.png')
    albumts = "Speak Now (Taylor's Version)"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
    embed_code = """
    <iframe src="https://open.spotify.com/embed/album/5AEDGbliTTfjOB8TSm1sxt?utm_source=generator" width="900" height="380" frameBorder="0" allowTransparency="true" allow="encrypted-media"></iframe>
    """
    st.subheader('Escucha el álbum aquí:')
    st.components.v1.html(embed_code, height=400)
  elif alb == 'Red':
    st.image('logos/red tv.png', width=200)
    albumts = "Red (Taylor's Version)"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
    embed_code = """
    <iframe src="https://open.spotify.com/embed/album/6kZ42qRrzov54LcAk4onW9?utm_source=generator" width="900" height="380" frameBorder="0" allowTransparency="true" allow="encrypted-media"></iframe>
    """
    st.subheader('Escucha el álbum aquí:')
    st.components.v1.html(embed_code, height=400)
  elif alb == '1989':
    st.image('logos/1989tv.png')
    albumts = "1989 (Taylor's Version)"
    canciones = df.loc[df['album'] == albumts]
    st.write(f"Canciones del álbum: {albumts}\n")
    for index, row in canciones.iterrows():
      st.write(f"{row['track_number']}.- {row['name']}")
    embed_code = """
    <iframe src="https://open.spotify.com/embed/album/64LU4c1nfjz1t4VnGhagcg?utm_source=generator" width="900" height="380" frameBorder="0" allowTransparency="true" allow="encrypted-media"></iframe>
    """
    st.subheader('Escucha el álbum aquí:')
    st.components.v1.html(embed_code, height=400)
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
    
