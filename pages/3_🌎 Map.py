import streamlit as st
import pandas as pd
import folium
from folium.plugins import SemiCircle, Draw
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Mapping",
    page_icon="📈",
)

st.title("Mapping Demo")
st.header('Statistics of Dataframe')

if 'df' in st.session_state:
    df = st.session_state['df']

    # Check columns
    required_columns = {"col0", "lon", "lat", "radius", "start_angle", "stop_angle", "color", "fill_color"}
    if not required_columns <= set(df.columns):
        # if not, show default map
        st.map(df, use_container_width=True)
    else:
        # if exist, show folium map in folium map
        m = folium.Map([35.72935639, 139.8327619], zoom_start=9)

        # For loop : each df line
        for row in df.itertuples(index=False):

            # Add Marker
            folium.Marker(
                (row.lat, row.lon),
                popup = row.col0
            ).add_to(m)

            # Add semicircle
            text_start_angle = row.start_angle
            text_stop_angle  = row.stop_angle
            SemiCircle(
                (row.lat, row.lon),
                radius      = row.radius,
                start_angle = row.start_angle,
                stop_angle  = row.stop_angle,
                color       = row.color,
                fill_color  = row.fill_color,
                opacity     = 0,
                popup= f"start angle - {text_start_angle} degrees, stop angle - {text_stop_angle} degrees",
            ).add_to(m)

        # Add draw plugin
        Draw(export=True).add_to(m)

        # Show folium map
        st_data = st_folium(m, width=1200, height=800)

    # Show df
    st.write(df)

