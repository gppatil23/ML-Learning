import streamlit as st
import pandas as pd
import numpy as  np

st.title('Streamlit Text input')

name =st.text_input('Enter your name')

if name:
    st.write(f"Hello {name}")

age = st.slider('Age',0,100,20)
st.write(f'Your Age is {age}')


options = ['python','c++','c','java']
select = st.selectbox("select your favorite lang",options)

st.button('enter',)

if select:
    st.write(f"Your lang {select}")

# Button for uploading File
upload_file = st.file_uploader("Choose a CSV file",type='csv')

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df.head())