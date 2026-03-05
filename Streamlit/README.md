Streamlit Web Application
📌 Overview

This project demonstrates how to build a simple interactive web application using Streamlit and Python.

Streamlit is an open-source Python framework used to create data apps and dashboards quickly using only Python, without requiring front-end development skills.

The goal of this project is to create a lightweight web interface for displaying data, running scripts, and interacting with users.

🚀 Features

Build interactive web applications using Python

Display text, tables, and charts

Accept user input through widgets

Rapid development with minimal code

Easy deployment and sharing

🛠️ Technologies Used

Python 3

Streamlit

Streamlit allows developers to convert Python scripts into web apps with built-in widgets and visualization capabilities.

📂 Project Structure
Streamlit/
│
├── app.py
├── requirements.txt
└── README.md
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/Mks604/Gen_AI-Week_1.git
2️⃣ Navigate to the Streamlit Folder
cd Gen_AI-Week_1/Streamlit
3️⃣ Install Required Packages
pip install streamlit
▶️ Running the Application

Run the Streamlit application using:

streamlit run app.py

After running the command, the application will open in your browser at:

http://localhost:8501
💻 Example Streamlit Code
import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name}! Welcome to Streamlit.")
📸 Example Use Cases

Data dashboards

Machine learning model demos

Data visualization apps

Interactive analytics tools

Rapid prototyping of web apps

⚠️ Notes

Streamlit apps run locally by default.

The page automatically refreshes whenever the code is updated.

Additional libraries like Pandas, Matplotlib, or Plotly can be used for data visualization.



📜 License

This project is open-source and available under the MIT License.
