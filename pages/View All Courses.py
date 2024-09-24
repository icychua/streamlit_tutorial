import streamlit as st
import pandas as pd
import json
import streamlit as st  
from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

#st.title("All courses")

filepath = './data/courses-full.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)

df = pd.DataFrame(dict_of_courses)
df = df.transpose().reset_index().iloc[:,1:]
st.dataframe(df)