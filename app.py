import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Streamlit Demo")
st.subheader("by M.M")

df = px.data.iris()

st.write(df)

st.write(px.scatter(df,x="sepal_length",y="sepal_width"))
