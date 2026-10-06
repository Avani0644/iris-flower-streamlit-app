import streamlit as st

st.title("General Information")

st.header("Iris Flower Classification")

st.write("""
The Iris Flower Classification project uses machine learning
to predict the species of an iris flower based on its measurements.
""")

st.subheader("Input Features")

st.write("• Sepal Length")
st.write("• Sepal Width")
st.write("• Petal Length")
st.write("• Petal Width")

st.subheader("Flower Species")

st.write("• Setosa")
st.write("• Versicolor")
st.write("• Virginica")