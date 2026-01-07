import streamlit as st

# Add a title to your app
st.title('My First Streamlit App created by VENKATESH SINGAMSETTY')

# Add some text
st.write("Welcome! This app calculates the square of a number.")

# create an integer slider to select a number
st.header("Select a number")
number = st.slider("Pick a number", 10, 100, 25) # min, max, default

# calculate and display the square of the number
st.subheader("Result") 
squared_number = number * number
st.write(f"The square of {number} is {squared_number}.")

# st.write("---")  # add a horizontal line
