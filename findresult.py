import streamlit as st
import pandas as pd

st.title("Result analyser")

df = pd.read_csv("report.csv")
df

st.sidebar.header("Enter marks here")
marks_form = st.sidebar.form("Enter each student marks orderwise")
roll_number = marks_form.number_input("Roll",1,100,1,1)
marks_obtained = marks_form.number_input("Marks",0,100,0,0.5)
add_data = marks_form.form_submit_button()
if add_data:
  st.write(roll_number,marks)
  new_data = {"roll": roll_number, "marks":marks_obtained}
  df = df.append(new_data, ignore_index = True)
  df.to_csv("report.csv", index=False)
