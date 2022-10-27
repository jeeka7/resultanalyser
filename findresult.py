import streamlit as st

D={}

st.write("what is the marks of first student?")
marks1 = st.number_input('Insert marks')
D[1] = marks1

st.write("what is the marks of first student?")
marks2 = st.number_input('Insert marks')
D[2] = marks2

st.write("what is the marks of first student?")
marks3 = st.number_input('Insert marks')
D[3] = marks3

st.write(D)
