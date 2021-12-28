import streamlit as st
from PIL import Image
import plotly.express as px

def app():
    st.subheader('Regional Focus')
    st.image("media/mideast.jpeg")
    st.write(' ')
    df = px.data.iris()
    fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
    fig.show()