import streamlit as st

# Page title
st.title("🌟 Simple Streamlit App")

# Text input
name = st.text_input("Enter your name:")

if name:
    st.success(f"Hello, {name}! Welcome to Streamlit 👋")

# Slider example
age = st.slider("Select your age:", 1, 100, 25)
st.write(f"Your selected age is: {age}")

# Button example
if st.button("Click Me"):
    st.info("You clicked the button! 🎉")

# Checkbox example
if st.checkbox("Show a secret message"):
    st.write("🕵️‍♂️ Here's the secret message: Streamlit is awesome!")

# Radio button example
favorite_color = st.radio(
    "Pick your favorite color:",
    ["Red", "Blue", "Green", "Yellow"]
)
st.write(f"Your favorite color is: {favorite_color}")

# Sidebar example
st.sidebar.header("Sidebar Menu")
st.sidebar.write("This is a simple sidebar.")
option = st.sidebar.selectbox(
    "Choose an option:",
    ["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")