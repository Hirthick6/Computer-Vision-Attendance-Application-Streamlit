import streamlit as st
import os


def app():
    st.markdown(""" <style> .font {
    font-size:25px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Provide Your Full Name</p>', unsafe_allow_html=True)

    name = st.text_input('Student Name')

    st.markdown(""" <style> .font {
    font-size:25px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Upload your photo here</p>', unsafe_allow_html=True)

    # Add file uploader to allow users to upload photos
    image_file = st.file_uploader("", type=['jpg', 'png', 'jpeg'])
    if image_file is not None:

        x = image_file.name.split(".")
        x[0] = name
        image_file.name = x[0] + "." + x[1]

        with open(os.path.join("images", image_file.name), "wb") as f:
            f.write(image_file.getbuffer())
        st.success("Saved File")