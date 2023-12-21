import streamlit as st
from functions import *

st.title("Todo App")
st.subheader("Made in python by akash")
st.write("Click on the checkboxes to complete the todo")
todos = get_todos()
for i in todos:
    st.checkbox(i)

x = st.text_input(label="Enter a Todo below", placeholder="Remind be about...")
print(x)