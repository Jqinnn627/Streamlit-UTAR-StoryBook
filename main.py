import streamlit as st

#Set app title
st.title("My first streamlit app")

#streamlit run [filename].py

st.write('Welcome to my first streamlit app')

#Display a button
st.button("Reset", type="primary")
if st.button("Say Hello"):
  st.write("Why hello there")
else:
  st.write("Goodbye")
