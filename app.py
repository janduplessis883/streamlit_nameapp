import streamlit as st
import requests

st.title('Name Submission App')

# Streamlit code to get user input
name = st.text_input("Enter your name:")

if st.button("Submit"):
    # Code to send data via webhook
    webhook_url = "https://eoqeefvce3v8qg4.m.pipedream.net"
    
    payload = {
        "name": name
    }
    
    response = requests.post(webhook_url, json=payload)
    
    if response.status_code == 200:
        st.success("Successfully sent your name!")
    else:
        st.error("Failed to send your name.")
