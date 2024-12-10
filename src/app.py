import streamlit as st

st.title("¡Hola mundo!")
st.write("Esta es una app de prueba en Streamlit.")

num1 = st.number_input("Introduce el primer numero")
num2 = st.number_input("Introduce el segundo numero")

if num1 and num2:
    st.write(f"La suma es {num1 + num2}")