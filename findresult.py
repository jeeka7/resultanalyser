import streamlit as st
import pandas as pd

marksList =[]

batch_size = st.slider("How many students are ther in your class?",1,10)
total = st.slider("What is the maximum marks for this paper ?",5,100,100,0.5)

for i in range(batch_size):
  marksList[i] = st.slider("What is the marks obtained ?",5,100,10,0.5)

st.write(type(marksList))
st.write(marksList)
