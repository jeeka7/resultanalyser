import streamlit as st
import pandas as pd

marksList =[]

batch_size = st.slider("How many students are ther in your class?",1,10)

for i in range(batch_size):
  st.write("enter marks of",i)
  marksList.append(int(input("Enter marks")))

st.write(type(marksList))
