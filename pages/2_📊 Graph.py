import streamlit as st
import pandas as pd
import plotly.express as px
import pygwalker as pyg

st.set_page_config(
    page_title="Graph",
    page_icon="📈",
    layout="wide",
)

st.title("Data Analysis with PyGWalker.")

if 'df' in st.session_state:
    df = st.session_state['df']
    pyg.walk(df, env='Streamlit')