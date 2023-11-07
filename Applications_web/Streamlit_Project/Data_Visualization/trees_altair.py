import streamlit as st
import pandas as pd
import altair as alt

st.title('SF Trees')
st.write('This app analyses trees is San Francisco using '
         'a dataset kindly provided by SF DPW'
         )
st.subheader('Bokeh Chart')
trees_df = pd.read_csv('trees.csv')
fig = alt.Chart(trees_df).mark_bar().encode(x = 'caretaker', y = 'count(*):Q')
st.altair_chart(fig)