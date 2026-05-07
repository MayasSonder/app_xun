import pandas as pd 
import streamlit as st 
if 'username' not in st.session_state:
    st.switch_page("app.py")
df = pd.read_csv('users.csv')

bouttond = st.sidebar.button('Déconnexion')
username = st.session_state['username']
st.sidebar.write(f'Bienvenue {username}')

if bouttond:
    del st.session_state['username']
    st.switch_page("app.py")

st.sidebar.page_link("pages/accueil.py", label="Accueil")
st.sidebar.page_link("pages/photos.py", label="Les photos de mon chat")

st.title('Bienvenue sur ma page')
st.image('https://i.pinimg.com/originals/1c/69/43/1c6943c372187ed186416b895f4eb06c.gif')
