import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Iris Data Analysis")

iris = sns.load_dataset("iris")

st.subheader("Dataset")
st.dataframe(iris)

st.subheader("Sepal Length Distribution")

fig, ax = plt.subplots()
ax.hist(iris["sepal_length"])
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Frequency")
st.pyplot(fig)

st.subheader("Sepal Length vs Petal Length")

fig, ax = plt.subplots()
ax.scatter(iris["sepal_length"], iris["petal_length"])
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Petal Length")
st.pyplot(fig)