import streamlit as st
import pandas as pd

col1, esp, col2 = st.columns([5,1,5])

with col1:
    st.file_uploader("Dados Identificação", key='id_data')

with col2:
    st.file_uploader("Dados Validação", key='val_data')



