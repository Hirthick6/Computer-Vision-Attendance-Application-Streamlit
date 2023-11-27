import streamlit as st
from PIL import Image
import numpy as np


def app():
    display = Image.open('./Attendance-management.jpg')
    display = np.array(display)
    st.image(display)
    st.markdown(""" <style> .font {
        font-size:20px ; font-family: 'Cooper Black'; text-align: center; color: #000000;} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<h1 class="font">Made With ❤️ By Kathija afrose</h1>', unsafe_allow_html=True)
