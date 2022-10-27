import streamlit as st

batch_size = st.slider('How many students are there?', 0, 10)

st.write(batch_size)

D={}

for i in range(1,batch_size+1):
    roll = i
    marks = st.number_input('Insert marks')
    D[roll] = marks
print(D)
df=pd.DataFrame(D)
print(df)
