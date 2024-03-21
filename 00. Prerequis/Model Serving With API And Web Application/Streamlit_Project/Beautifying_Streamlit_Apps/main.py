import streamlit as st
import pandas as pd

st.title("SF Trees")
st.write(
    'This app analyses trees in San Francisco using a dataset kindly provided by SF DPW'
)

trees_df = pd.read_csv("trees.csv")

col1, col2, col3 = st.columns((1, 1, 1))

first_width = st.number_input('First Width', min_value=1, value=1)
second_width = st.number_input('Second Width', min_value=1, value=1)
third_width = st.number_input('Third Width', min_value=1, value=1)

with col1:
    st.write('First column')
with col2:
    st.write('Second column')
with col3:
    st.write('Third column')
