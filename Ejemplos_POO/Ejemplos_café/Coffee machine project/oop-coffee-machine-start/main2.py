from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import streamlit as st
# STEP4: Aplicacion streamlit
st.title("Coffee Machine App")
st.write("Enjoy your coffee today!")

col1, col2 = st.columns([1, 1])
with col1:
    lat = st.number_input("Introducir Elección (latte/espresso/cappuccino):", value='espresso')
with col2:
    lon = st.number_input("Introducir Dinero:", value=0.0, format="%.6f", step=0.000001)

fetch_button = st.button("Make Coffee")