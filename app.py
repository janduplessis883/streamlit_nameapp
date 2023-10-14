import streamlit as st
import requests
import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns 


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

st.markdown('### Load CSV from GitHub into DataFrame')

if st.button("Load csv from GitHub to DataFrame"):
    # Assuming the 'names.csv' file is available at this URL
    url = 'https://raw.githubusercontent.com/janduplessis883/streamlit_nameapp/master/names.csv'
    
    data = pd.read_csv(url)
    
    # Display the DataFrame
    st.write(data.head())
    
# Automatically Display the DataFrame
url = 'https://raw.githubusercontent.com/janduplessis883/streamlit_nameapp/master/names.csv'
data = pd.read_csv(url)
st.write("Here's the DataFrame:")
st.write(data)

# Automatically Display the Seaborn Plot
st.write("And here's the Seaborn Plot:")

# Create a new figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create the barplot on the "ax" axis
sns.barplot(x='City', y='Age', data=data, ax=ax, color='#a62a99')

# Add title to the plot
ax.set_title('Age by Name')

# Show the plot in Streamlit
st.pyplot(fig)