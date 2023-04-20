import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topics.csv")

with st.form(key="email_form", clear_on_submit=True):
    user_email = st.text_input("Your email address:")
    msg_topic = st.selectbox("Select topic", df["topic"])
    raw_message = st.text_area("Your message:")
    message = f"""\
Subject: New email from {user_email} - Python Simple Website

From: {user_email}
Topic: {msg_topic}

{raw_message}
"""

    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.success("Your email was sent successfully and we will respond shortly!\n Thank you for contacting us.")
