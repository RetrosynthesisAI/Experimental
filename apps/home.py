import streamlit as st
from PIL import Image
import plotly.graph_objects as go

def app():
    st.subheader('Regional Focus')
    st.image("media/mideast.jpeg")
    st.write(' ')
    df = data.iris()
    fig = scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
    st.plotly_chart(fig)