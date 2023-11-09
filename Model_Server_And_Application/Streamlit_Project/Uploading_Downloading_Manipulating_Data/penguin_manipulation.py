import time

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

st.title("Palmer's Penguins")
st.markdown("Use this Streamlit app to make you own scatterplot about penguins")

# Import our data
penguin_file = st.file_uploader('Select Your Local Penguins CSV default provided')

@st.cache_data()
def load_file(penguin_file):
    time.sleep(3)
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv('penguins.csv')
    return(df)

penguins_df = load_file(penguin_file)

selected_x_vars = st.selectbox(
    'what do you want the x variable to be?',
    ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g']
)
selected_y_vars = st.selectbox(
    'what about the y ?',
    ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g']
)

selected_gender = st.selectbox(
    'what gender do you want to filter for?',
    ['all penguins', 'male penguins', 'female penguins']
)

if selected_gender == 'male penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else :
    pass


fig, ax = plt.subplots()
ax = sns.scatterplot(
    x = penguins_df[selected_x_vars],
    y = penguins_df[selected_y_vars],
    hue = penguins_df['species']
)

plt.xlabel(selected_x_vars)
plt.ylabel(selected_y_vars)
plt.title("Scatterplot of Palmer's Penguins : {}". format(selected_gender))
st.pyplot(fig)