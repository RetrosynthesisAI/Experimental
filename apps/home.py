import streamlit as st
from PIL import Image
import plotly.express as px
from sklearn.datasets import load_iris

def app():
    st.subheader('Regional Focus')
    st.image("media/mideast.jpeg")
    st.write(' ')
    iris = load_iris()
    df = iris.data
    fig = scatter_3d(df, x=df['0'], y=df['1'], z=df['2'], color=df['3'])
    fig.show()