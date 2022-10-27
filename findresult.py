import streamlit as st

batch_size = st.slider('How many students are there?', 0, 10)

st.write(batch_size)
