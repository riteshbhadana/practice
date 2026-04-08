import streamlit as st

st.title("my name is ")

name = st.text_input("name")

if st.button("submit"):
    st.write("hell", name)

import streamlit as st

st.title("User Input App")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", 1, 100)

if st.button("Submit"):
    st.write("Hello", name)
    st.write("Your age is", age)
    st.success("Submitted Successfully!")