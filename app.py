import pandas as pd 
import streamlit as st 
df = pd.read_csv('users.csv')

st.title('Sidentifier')
username = st.text_input('Entre ton identifiant')
password = st.text_input('Entre un mot de passe', type="password")
boutton = st.button('Login')

if boutton: # si on clique sur le boutton
  if username in df['name'].values:
    stockage_password = df[df['name'] == username]['password'].values[0]
    if password == stockage_password:
      st.session_state['username'] = username
      st.switch_page("pages/accueil.py") # on passe à la page suivante
    else:
      st.warning('Mot de passe incorrect')

else:
  st.warning('Identifiant incorrect')
