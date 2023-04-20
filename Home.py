import streamlit as st
import pandas

st.set_page_config(layout="wide")

first_title = "The Best Company"
first_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam cursus quam nec diam tempus, ac convallis nisi 
sollicitudin. Fusce ac ligula libero. Nullam eleifend ultrices turpis eget dictum. Duis id nunc in enim sagittis 
ornare. Quisque aliquet lorem id metus lobortis posuere. Fusce ante tellus, bibendum eget hendrerit ac, pharetra.
"""
second_title = """
Our Team

"""

st.title(first_title)
st.write(first_text)
st.subheader(second_title)

col1, gap_col1, col2, gap_col2, col3 = st.columns([2, 1, 2, 1, 2])
df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(((row["first name"] + " " + row["last name"]).title()))
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(((row["first name"] + " " + row["last name"]).title()))
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(((row["first name"] + " " + row["last name"]).title()))
        st.write(row["role"])
        st.image("images/" + row["image"])


