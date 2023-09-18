import streamlit;
import pandas;

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");

streamlit.title('My parents new Healthy Diner');

streamlit.header('Breakfast Favorites');

streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal');
streamlit.text(' 🥗 Kale, SPinach & Rocket Smoothie');
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg');
streamlit.text(' 🥑🍞 Avocato Toast');

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.dataframe(my_fruit_list)
