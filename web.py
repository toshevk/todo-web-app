import streamlit as st
import functions

tasks = functions.get_todos()


def add_task():
    input_task = st.session_state["input_new_task"]
    input_task = str(input_task[:1]).capitalize() + input_task[1:] + '\n'
    tasks.append(input_task)
    functions.write_todos(tasks)
    st.session_state["input_new_task"] = ""


st.title("My Todo App")
st.subheader("Welcome to my first Python app!")
st.write("This app is part of my Python course, "
         "and it aims to increase your productivity.")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_todos(tasks)
        del st.session_state[task]
        st.experimental_rerun()

st.text_input(label="Add a new task:", on_change=add_task, key="input_new_task")
