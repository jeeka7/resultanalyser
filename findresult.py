import streamlit as st
import pandas as pd

batch_size = st.slider('How many students are there?', 1, 10)

st.write(batch_size)

D={}

for i in range(1,batch_size+1):
    roll = i
    st.write(i,student information)
    marks = st.number_input('Insert marks')
    D[roll] = marks
    st.write(marks)
st.write(D)
df=pd.DataFrame(D)
st.write(df)
