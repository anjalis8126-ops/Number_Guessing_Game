import streamlit as st
import random
import string
from collections import Counter

st.set_page_config(
    page_title="Python Project 02",
    page_icon="🎮",
    layout="centered"
)

st.title("🎮 Number Guessing Game & Word Counter")
st.write("Python Programming Virtual Internship Project")

st.divider()

# SIDEBAR MENU

option = st.sidebar.radio(
    "Choose a Project",
    ["Number Guessing Game", "Word Counter"]
)


# NUMBER GUESSING GAME

if option == "Number Guessing Game":

    st.header("🎯 Number Guessing Game")

    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.finished = False

    if st.button("Start New Game"):
        st.session_state.secret = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.finished = False

    guess = st.number_input(
        "Guess a number between 1 and 100",
        min_value=1,
        max_value=100,
        step=1
    )

    if st.button("Submit Guess"):

        if not st.session_state.finished:

            st.session_state.attempts += 1

            if guess == st.session_state.secret:

                score = max(
                    0,
                    (8 - st.session_state.attempts) * 10
                )

                st.success("🎉 Congratulations! Correct Guess!")
                st.write("Attempts:", st.session_state.attempts)
                st.write("Your Score:", score)

                st.session_state.finished = True

            elif guess < st.session_state.secret:
                st.warning("Too Low! Try a Higher Number.")

            else:
                st.warning("Too High! Try a Lower Number.")

            st.write(
                "Attempts used:",
                st.session_state.attempts
            )

            if st.session_state.attempts >= 7:
                if not st.session_state.finished:
                    st.error("Game Over!")
                    st.write(
                        "Correct number:",
                        st.session_state.secret
                    )
                    st.session_state.finished = True


# WORD COUNTER

elif option == "Word Counter":

    st.header("📝 Word Counter")

    st.write("Upload a text file to analyze its words.")

    uploaded_file = st.file_uploader(
        "Upload your TXT file",
        type=["txt"]
    )

    if uploaded_file is not None:

        text = uploaded_file.getvalue().decode("utf-8")

        words = text.lower().translate(
            str.maketrans("", "", string.punctuation)
        ).split()

        frequency = Counter(words)

        st.success("File uploaded successfully!")

        st.metric("Total Words", len(words))

        st.subheader("Word Frequency Analysis")

        if frequency:

            for word, count in frequency.most_common():
                st.write(f"**{word}** : {count}")

        else:
            st.info("No words found in this file.")

st.divider()

st.caption("Developed by Anjali | Python Internship Project")