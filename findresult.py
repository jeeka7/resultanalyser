import streamlit as st
import pandas as pd

marksList =[]

batch_size = st.slider("How many students are ther in your class?",1,10)

for i in range(batch_size):
  number = st.number_input('Insert a number')
  marksList.append(number)
  st.write(i)
st.write('The current number is ', number)
st.write(type(marksList))
