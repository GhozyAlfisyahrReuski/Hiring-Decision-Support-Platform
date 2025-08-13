# import libraries
import streamlit as st
import home
import eda 
import predict as predict

# bagian dalam sidebar
with st.sidebar:
    st.write("# Page Navigation")

    # toggle pilih halaman
    page = st.selectbox("Select Page", ("Home", "EDA", 'Predict Hiring and Rating'))

    # test
    st.write(f'You are in: {page} page')

    st.write('## About')
# magic
'''
The **CitoConnect Hiring Decision Support Platform** helps companies make **data-driven hiring decisions**.  
It predicts a candidate’s hiring outcome, calculates an overall score, and highlights the most important factors.  

Designed to improve efficiency, reduce bias, and provide fair, explainable results,  
CitoConnect empowers HR teams to hire **smarter and faster**.
'''


# bagian luar sidebar
if page == 'Home':
    home.run()
elif page == 'EDA':
    eda.run()
else:
    predict.run()
