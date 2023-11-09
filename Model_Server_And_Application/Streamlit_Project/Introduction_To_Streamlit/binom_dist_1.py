import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#st.set_option('deprecation.showPyplotGlobalUse', False)
binom_dist = np.random.binomial(1, 0.5, 1000)
list_of_means = []
for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())
fig1, ax1 = plt.subplots()
ax1 = plt.hist(list_of_means)
st.pyplot(fig1)
fig2, ax2 = plt.subplots()
ax2 = plt.hist([1, 1, 1, 1])
st.pyplot(fig2)