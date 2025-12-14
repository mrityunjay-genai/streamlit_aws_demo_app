import streamlit as st

st.title("Simple Calculator App")

a = st.number_input("Enter the first number:", value=0.0, format="%.4f")
operation = st.selectbox("Select operation:", ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)"])
b = st.number_input("Enter the second number:", value=0.0, format="%.4f")

result = None
error = ""

if st.button("Calculate"):
    try:
        if operation == "Add (+)":
            result = a + b
        elif operation == "Subtract (-)":
            result = a - b
        elif operation == "Multiply (×)":
            result = a * b
        elif operation == "Divide (÷)":
            if b == 0:
                error = "Cannot divide by zero!"
            else:
                result = a / b
    except Exception as e:
        error = f"Error: {str(e)}"

# Display result or error
if result is not None:
    st.success(f"Result: {result}")
elif error:
    st.error(error)