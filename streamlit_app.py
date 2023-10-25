import streamlit as st
import pandas as pd
st.title('My Parents New Healthy Diner')
st.write("Hello *world!*")
st.text("Hello using st.text")

st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

st.multiselect("Pick some fruits:",list(my_fruit_list.index))

#display the table on the page
st.dataframe(my_fruit_list)

