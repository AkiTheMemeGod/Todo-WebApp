import streamlit as st
from functions import *
todos = get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    put_todos(todos)
    st.session_state["new_todo"] = None


st.title("Todo App")
st.subheader("Made in python by akash")
st.write("Click on the checkboxes to complete the todo")
for index, i in enumerate(todos):
    box = st.checkbox(i, key=i)
    if box:
        todos.pop(index)
        put_todos(todos)
        del st.session_state[i]
        st.rerun()

st.text_input(label="Enter a Todo below", placeholder="Remind be about...",
                  on_change=add_todo, key="new_todo")
