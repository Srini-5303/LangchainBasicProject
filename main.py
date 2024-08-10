import streamlit as st

import langchain_helper


st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine",("Indian","Mexican","Arabic","Italian","Spanish","American"))


if cuisine:
    response = langchain_helper.generate_rest_name_and_menu(cuisine)
    st.header(response['restaurant_name'].strip())

    menu_items = response['menu_items'].strip().split(',')

    st.write("**MENU ITEMS**")
    for item in menu_items:
        st.write(item)