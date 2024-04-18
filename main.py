import langchain_helper as lch
import streamlit as st

st.title("Training Program Generator")

api_key = st.text_input("Enter your API key", type="password")

exercise_type = st.text_input("Enter the exercises you want to include in the program (e.g. pushups, pullups, squats)", max_chars=50)
difficulty = st.selectbox("Select the difficulty", ["beginner", "intermediate", "advanced", "other"])

if difficulty == "other":
    difficulty = st.text_input("Let's try something else! Enter the difficulty level you want to generate a program for", max_chars=25)

if st.button("Generate Training Program"):
    response = lch.generate_training_program(exercise_type, difficulty, api_key)
    st.write(response['training_program'])