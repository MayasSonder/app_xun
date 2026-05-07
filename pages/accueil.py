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
st.image('https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MThjZ3E3ZWZjcHdubXlyZjkxN3h2MWFqM3FhanUxNWJ1anR1aHVydyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/6uOKby3tWy4yXwTa5H/giphy.gif')
