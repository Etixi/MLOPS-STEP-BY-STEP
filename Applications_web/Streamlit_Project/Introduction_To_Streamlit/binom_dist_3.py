import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Illustration du théorème central limite avec Streamlit")

st.subheader("Une application de Etienne KOA")

st.title(
         "Cette application simule un millier de tirages au sort en utilisant,"
         "le hasard des têtes saisies ci-dessous, puis des échantillons avec remplacement, "
         "à partir de cette population et trace l'histogramme des moyennes des échantillons,"
         " afin d'illustrer le « théorème central limite»."
)

perc_heads = st.number_input(
    label = 'Chance of coins Landing on Heads',
    min_value = 0.0,
    max_value = 1.0,
    value = 0.5
)

binom_dist = np.random.binomial(1, perc_heads, 1000)

list_of_means = []

for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())

fig, ax = plt.subplots()
ax = plt.hist(list_of_means, range=[0, 1])
st.pyplot(fig)