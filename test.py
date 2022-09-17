#importing required libraries

import streamlit as st



#adding a radio button

ques = st.radio(

    "Do you like coding?",

    ('Yes','No'))



#specifying what should be display when the radio button is selected

if ques == 'Yes':

    st.write('You like coding.')

else:

    st.write("You do not like coding.")