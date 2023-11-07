# Import the BaseSettings from pydantic_settings
#from pydantic_settings import BaseSettings

# Your other imports remain unchanged
import pandas as pd
import matplotlib.pyplot as plt
import requests
import streamlit as st
from streamlit_lottie import st_lottie
#from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns

sns.set_style('darkgrid')
st.set_page_config(layout="wide")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


file_url = "https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json"
lottie_penguin = load_lottieurl(file_url)
st_lottie(lottie_penguin, speed=2, width=800, height=400)

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

# Import our data
penguin_file = st.file_uploader('Select Your Local Penguins CSV default provided')
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    penguins_df = pd.read_csv('penguins.csv')

markers = {"Adelie": 'X', "Gentoo": 's', "Chinstrap": 'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(
    data=penguins_df,
    x=selected_x_vars,
    y=selected_y_vars,
    hue='species',
    markers=markers,
    style='species'
)
plt.xlabel(selected_x_vars)
plt.ylabel(selected_y_vars)
plt.title("Scatterplot of Palmer's Penguins")
st.pyplot(fig)

st.title("Pandas Profiling of Penguin Dataset")
penguin_profile = ProfileReport(penguins_df, explorative=True)
st_profile_report(penguin_profile)
