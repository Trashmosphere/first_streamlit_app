import streamlit
import pandas

streamlit.title("My Parents New Healty Diner")

streamlit.header("Breakfast Menu")

streamlit.text("🥣 Omega3 Blueberry OatMeal")
streamlit.text("🥗 Kale, Spinach and rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
