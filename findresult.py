import streamlit as st
import pandas as pd

batch_size = st.slider('How many students are there?', 0, 10)

st.write(batch_size)
D={}
# Add student information
# to the dictionary
for i in range(1,batch_size+1):
    roll = i
    marks = int(input('Enter Marks: '))
    D[roll] = marks
st.write(D)
df=pd.DataFrame(D)
st.write(df)
