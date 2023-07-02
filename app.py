import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Main",
    page_icon="📈",
)

st.title("Dash Boad Main Page")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    **👈 Select a demo from the sidebar** to see some examples.
    """
)

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing earthquake data', type='csv')

# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file, encoding = "shift-jis")
    st.session_state['df'] = df