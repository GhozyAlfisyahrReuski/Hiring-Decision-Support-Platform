# import libraries
import streamlit as st
import eda, deployment.predict as predict

# bagian dalam sidebar
with st.sidebar:
    st.write("# Page Navigation")

    # toggle pilih halaman
    page = st.selectbox("Pilih Halaman", ("EDA", 'Predict Rating'))

    # test
    st.write(f'Halaman yang dituju {page}')

    st.write('## About')
    # magic
    '''
    Page ini berisikan hasil analisis data terhadap pemain di FIFA 2024
    dan juga prediksi rating pemain berdasarkan atribut yang dimiliki
    '''

# bagian luar sidebar
if page == 'EDA':
    eda.run()

else:
    predict.run()