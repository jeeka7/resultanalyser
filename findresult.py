import streamlit as st
import pandas as pd

marksList =[]

batch_size = st.slider("How many students are ther in your class?",1,10)
total = st.slider("What is the maximum marks for this paper ?",5,100,100,0.5)

for i in range(batch_size+1):
  st.write(i+1)
  marks = st.slider("What is the marks obtained ?",5,100,10,0.5)
  marksList.append(marks)
  st.write(i)

st.write(type(marksList))
