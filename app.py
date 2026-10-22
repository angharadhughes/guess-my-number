
import streamlit as st
import random

st.title("Welcome to Guess my Number!")
st.write("I am going to pick a Number between 1 and 100. Try your best to read my mind!")

if "the_number" not in st.session_state:
    st.session_state.the_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.hint = ""
    st.session_state.finished = False

the_number = st.session_state.the_number

st.write("thinking ...")
st.write("Okay, got my number!")

if not st.session_state.finished:
    guess = st.number_input("Take a guess:", min_value=1, max_value=100, step=1)

    if st.button("Guess!"):
        st.session_state.attempts += 1

        if guess > the_number:
            hint = "Lower ..."
        elif guess < the_number:
            hint = "Higher ..."
        else:
            hint = "Correct!"
            st.session_state.finished = True

        st.session_state.hint = hint

if st.session_state.hint:
    st.write(st.session_state.hint)

if st.session_state.finished:
    st.write("You guessed it! The number was ", the_number)
    st.write("It took you ", st.session_state.attempts, "attempts")

    if st.button("Play Again!"):
        st.session_state.the_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.hint = ""
        st.session_state.finished = False
        st.rerun()

