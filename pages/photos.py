import pandas as pd 
import streamlit as st 
df = pd.read_csv('users.csv')

bouttond = st.sidebar.button('Déconnexion')
username = st.session_state['username']
st.sidebar.write(f'Bienvenue {username}')

if bouttond:
    del st.session_state['username']
    st.switch_page("app.py")

st.sidebar.page_link("pages/accueil.py", label="Accueil")
st.sidebar.page_link("pages/photos.py", label="Les photos de mon chat")

col1, col2, col3 = st.columns(3)
st.title("Bienvenue dans l'album de xun")
col1.image("xun1.jpg")
col2.image("xun2.jpg")
col3.image("xun3.jpg")

col4, col5 = st.columns(2)
col4.image("xun4.jpg")
col5.image("xun5.jpg")


