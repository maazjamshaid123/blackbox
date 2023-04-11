import streamlit as st
from blackhole import detect_hole
from intro import show_intro

st.set_page_config(page_title = 'Black Box | AstroAlgo',page_icon="page_icon.jpeg", layout="wide", menu_items={
        'Get Help': 'https://www.linkedin.com/in/maazjamshaid/',
        'Report a bug': "https://www.linkedin.com/in/maazjamshaid/",
        'About': '''$BlackBox$'''
    })

# st.sidebar.image("1.png", use_column_width=True)

st.sidebar.markdown("---")

PAGE_DICT = {
    "What is Black Box?": show_intro,
    "Black Holes in Globular Clusters":detect_hole
}
page = st.sidebar.selectbox("Get Started", PAGE_DICT)

st.sidebar.markdown("---")


#***********************************************************************************************

if page == "What is Black Box?": #FIRST PAGE
    show_intro()

#***********************************************************************************************

elif page == "Black Holes in Globular Clusters": #SECOND PAGE
    detect_hole()
