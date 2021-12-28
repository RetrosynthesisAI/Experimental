import streamlit as st
from PIL import Image
import plotly.graph_objects as go
from sklearn.datasets import load_iris

def app():
    st.subheader('Regional Focus')
    st.image("media/mideast.jpeg")
    st.write(' ')
    iris = load_iris()
    df = iris.data
    fig = st.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
    st.plotly_chart(fig)