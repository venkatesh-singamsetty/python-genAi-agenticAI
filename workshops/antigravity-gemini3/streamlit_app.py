import streamlit as st
from calculator import add, subtract, multiply, divide

st.title("Simple Calculator")

# Input
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.success(f"The result is: {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.success(f"The result is: {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.success(f"The result is: {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        if result == "Error! Division by zero.":
            st.error(result)
        else:
            st.success(f"The result is: {result}")
