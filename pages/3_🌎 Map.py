import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Mapping",
    page_icon="📈",
)

st.title("Mapping Demo")
st.header('Statistics of Dataframe')

if 'df' in st.session_state:
    df = st.session_state['df']
    st.write(df.describe())
    st.map(df, use_container_width=True)
