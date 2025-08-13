# import libraries
import streamlit as st
import home
import eda 
import predict as predict

# bagian dalam sidebar
with st.sidebar:
    st.write("# Page Navigation")

    # toggle pilih halaman
    page = st.selectbox("Select Page", ("Home" "EDA", 'Predict Hiring and Rating'))

    # test
    st.write(f'You are in: {page} page')

    st.write('## About')
    # magic
    '''
    Page ini berisikan hasil analisis data terhadap pemain di FIFA 2024
    dan juga prediksi rating pemain berdasarkan atribut yang dimiliki
    '''

# bagian luar sidebar
if page == 'Home':
    eda.run()
elif page == 'EDA':
    eda.run()
else:
    predict.run()
