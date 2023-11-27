import streamlit as st
import pandas as pd


def app():
    st.markdown(""" <style> .font {
        font-size:25px ; font-family: 'Cooper Black'; color: #FF9633;}
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Attendance Sheet</p>', unsafe_allow_html=True)
    df = pd.read_csv('./Attendance.csv', index_col=False)
    st.write(df)
