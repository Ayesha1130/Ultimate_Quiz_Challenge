import streamlit as st
import random
import time

st.markdown(
    """
    <style>
          .stApp { 
             background-color: #121212; 
            } 

           .big-font { 
             font-size: 26px !important; 
             font-weight: bold; 
             color: #FFA500; 
            }

            .correct { 
                color: #00FF00; 
                font-weight: bold; 
                font-size: 22px; 
            }

            .incorrect { 
                color: #FF4B4B; 
                font-weight: bold; 
                font-size: 22px; 
            }

            div[data-testid="stRadio"] label { 
                color: #FAFAFA !important; 
                font-weight: bold; 
                font-size: 20px; 
            }

            div[data-testid="stRadio"] div { 
                color: #FAFAFA !important; 
                font-size: 18px; 
                font-weight: bold; 
            }

            .stProgress > div > div { 
                background-color: #00FF00 !important; 
            }

            .stButton button { 
                background-color: #AA104F !important; 
                color: #FAFAFA !important; 
                font-weight: bold !important; 
                border-radius: 8px !important; 
                padding: 10px 20px !important; 
                transition: all 0.3s ease-in-out !important; 
            }

            .stButton button:hover { 
                background-color: #2DC071 !important; 
                color: black !important; 
                border: none; 
            }

    </style>
    """,
    unsafe_allow_html=True,
)

# Fun title with emojis
st.markdown("<h1 style='text-align: center; color: white;'>🙋 Welcome to the Ultimate Quiz Challenge!</h1>", unsafe_allow_html=True)

# Define the kids-friendly quiz questions in English
questions = [
     {
        "question": "What is the keyword used to define a function in Python?",
        "options": ["def", "function", "create", "fun"],
        "answer": "def",
    },
    {
        "question": "Which of the following is used to start a comment in Python?",
        "options": ["#", "//", "/*", "<!--"],
        "answer": "#",
    },
    {
        "question": "Which Python library is commonly used for data analysis?",
        "options": ["matplotlib", "numpy", "pandas", "os"],
        "answer": "pandas",
    },
    {
        "question": "What will be the output of the following code: `print(2 + 3 * 4)`?",
        "options": ["14", "20", "10", "8"],
        "answer": "14",
    },
    {
        "question": "Which function is used to get the length of a list in Python?",
        "options": ["len()", "size()", "length()", "count()"],
        "answer": "len()",
    },
    {
        "question": "Which data structure in Python is immutable?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": "Tuple",
    },
    {
        "question": "Which of the following is used to import libraries in Python?",
        "options": ["import", "include", "load", "using"],
        "answer": "import",
    },
    {
        "question": "What is the output of `print(type(3.14))`?",
        "options": ["float", "int", "str", "None"],
        "answer": "float",
    },
    {
        "question": "What does `len()` function do in Python?",
        "options": ["Returns the size of a list", "Returns the sum of elements", "Counts the number of characters in a string", "Both A and C"],
        "answer": "Both A and C",
    },
    {
        "question": "Which of the following is a Python keyword?",
        "options": ["for", "while", "if", "all of the above"],
        "answer": "all of the above",
    },
]

# Initial question setup
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question
question = st.session_state.current_question

# Display question box with background color
st.markdown(f"<div style='font-size: 30px; color: green; font-weight: bold;'>{question['question']}</div>", unsafe_allow_html=True)

# Radio buttons for options
option = st.radio("Choose Your Answer", question['options'], key="answer", index=0, help="Pick one of the options below!")

# Custom Submit button with style
submit_button = st.button("🚀 Submit Answer", key="submit", help="Click to check your answer!")

# When the submit button is clicked
if submit_button:
    if option == question['answer']:
        
        st.success("🎉 Correct Answer! You're awesome! 💪")
        st.balloons()  # Fun balloons animation on correct answer
    else:
        st.error(f"Oops! ❌ Wrong Answer! The correct answer is: {question['answer']}")
    
    # Show a fun message before the next question appears
    st.markdown("<h3 style='text-align: center; color: #ff6347;'>Get ready for the next question! 🎉</h3>", unsafe_allow_html=True)
    
    # Wait a moment before showing the next question
    time.sleep(10)
    
    # Choose a new random question and reload
    st.session_state.current_question = random.choice(questions)
    st.rerun()

st.header("Created with ❤️ by Ayesha Iqbal")

