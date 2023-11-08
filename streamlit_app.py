import streamlit as st
import pandas as pd
import snowflake.connector

st.title('My Parents New Healthy Diner')
st.write("Hello *world!* st.write")
st.text("Hello using st.text")

st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = st.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
st.dataframe(fruits_to_show)

#New section to display fruityvice api response
st.header('Fruityvice Fruit Advice!')
###########################################################################################
st.header('Fruityvice Fruit Advice!')
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ',fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# st.text(fruityvice_response.json())

# take the json version of the response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output it the screen as a table
st.dataframe(fruityvice_normalized)

##############################################################################################
# my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# st.text("Hello from Snowflake:")
# st.text(my_data_row)


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
st.text("The fruit load list contains:")
st.text(my_data_row)



