import streamlit as st

from langchain_helper import generate_restaurant_name_and_items

st.title("Restaurant Name & Menu Generator")
cuisine = st.sidebar.selectbox(
    "Pick a Cuisine", ("Indian", "Mexican", "Italian", "Arabic", "American")
)

if cuisine:
    response = generate_restaurant_name_and_items(cuisine)
    st.header(response["restaurant_name"])
    menu_items = response["menu_items"].split(":")[-1].split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)
