import streamlit as st
import requests
import datetime

url = 'https://api.nasa.gov/planetary/apod?' \
      f'api_key={st.secrets["api_key"]}'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()  # dict type

st.set_page_config(layout = "centered")

st.header(f':blue[Welcome to my Astronomy Picture of the Day web site] :sunglasses:')
st.subheader(f'Today is: {content["date"]}')
st.subheader(content['title'])
st.image(content['url'])
st.write(content['explanation'])
