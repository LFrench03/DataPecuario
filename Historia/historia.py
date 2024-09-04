import streamlit as st
from streamlit_timeline import timeline
st.logo(image="brand/PNG/Identificador principal.png")
st.set_page_config(page_title="Timeline Ganaderia", layout="wide")

with open("events.json", "r") as f:
    data = f.read()

timeline(data, height=800)