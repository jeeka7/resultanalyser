import streamlit as st

D={}

marks1 = st.number_input('Insert marks of 1st student')
D[1] = marks1

marks2 = st.number_input('Insert marks of 2nd student')
D[2] = marks2

marks3 = st.number_input('Insert marks of 3rd student')
D[3] = marks3

st.write(D)
