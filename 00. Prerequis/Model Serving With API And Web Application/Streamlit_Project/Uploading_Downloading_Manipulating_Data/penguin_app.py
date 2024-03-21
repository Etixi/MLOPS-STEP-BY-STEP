import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

st.title("Palmer's Penguins")
st.markdown("Use this Streamlit app to make you own scatterplot about penguins")
selected_x_vars = st.selectbox(
    'what do you want the x variable to be?',
    ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g']
)
selected_y_vars = st.selectbox(
    'what about the y ?',
    ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g']
)
markers = {"Adelie" : 'X', "Gentoo" : 's', "Chinstrap" : 'o'}
# Import our data
penguins_df = pd.read_csv("penguins.csv")
st.write(penguins_df.head())

fig, ax = plt.subplots()
ax = sns.scatterplot(
    data = penguins_df,
    x = selected_x_vars,
    y = selected_y_vars,
    hue = 'species',
    markers = markers,
    style = 'species'
)

plt.xlabel(selected_x_vars)
plt.ylabel(selected_y_vars)
plt.title("Scatterplot of Palmer's Penguins")
st.pyplot(fig)