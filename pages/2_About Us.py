import streamlit as st
import streamlit as st  
from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()


st.set_page_config(page_title="test")
st.title("About this App")

st.write('''
This is a Streamlit App that 
demonstrates how to use the OpenAI API to generate text completions.''')

expand = st.expander("How to use this App")
expand.markdown('''
1. Enter your prompt in the text area.
2. Click the 'Submit' button
3. The app will generate a text completion based on your prompt''')