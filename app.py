"""
Retrosynthesis AI - Explore App
Author: @Margaret Linan 
Created: 12.24.21 
Contributors: None
"""
import streamlit as st
from multiapp import MultiApp
from apps import home, chdis, inutero, drugres, negtrop, mol3d, zoo # import your app modules here
from PIL import Image
from pathlib import Path
import base64

st.set_page_config(
     page_title='Explore',
     layout="wide",
    initial_sidebar_state="expanded",
)


app = MultiApp()


st.image("media/logo.png")

st.title('Global Disease Research')
st.write('The aim of the Explore app is to enable scientists to explore molecular 3D visualizations as well as global and population specific disease trends.')
# Add all your application here
app.add_app("Home", home.app)
app.add_app("Molecular 3D", mol3d.app)
app.add_app("Pediatric Diseases", chdis.app)
app.add_app("Drug Resistant Diseases", drugres.app)
app.add_app("In Utero Diseases", inutero.app)
app.add_app("Neglected Tropical Diseases", negtrop.app)
app.add_app("Zoonotic Diseases", zoo.app)
app.run()
 

 
 
