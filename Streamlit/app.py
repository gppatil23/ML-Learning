import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit" )

#Displaying Simple Text
st.write("This is a simple Streamlit app.")
#remember streamlit runs only in python file(.py) file

#printing simple Dataframe
df = pd.DataFrame({
    'First Col' : [1,2,3,4],
    'Second col': [20,5,40,50]
})

st.write(df)

#creating a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data) 

