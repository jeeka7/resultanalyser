import streamlit as st
import pandas as pd

batch_size = st.slider("How many students are ther in your class?",1,10)
total = st.slider("What is the maximum marks for this paper ?",5,100,100,0.5)

st.title("Result analyser")

df = pd.read_csv("report.csv")
df

st.sidebar.header("Enter marks here")
marks_form = st.sidebar.form("Enter each student marks orderwise")

roll_number = marks_form.number_input("Roll")
marks_obtained = marks_form.number_input("Marks")
add_data = options_form.form_submit_button()
if add_data:
  st.write(roll_number,marks)
  new_data = {"roll": roll_number, "marks":marks_obtained}
  df = df.append(new_data, ignore_index = True)
  df.to_csv("report.csv", index=False)
