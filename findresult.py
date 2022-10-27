import streamlit as st

st.title("My app is deployed on cloud and is working")

import sys
import pandas as pd
batch_size=int(input("how many students are there in your class?"))
if batch_size >10:
    sys.exit("Batch size cannot be greater than 10")
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
