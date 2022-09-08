import streamlit as st

col1, esp, col2, esp, col3 = st.columns([2,1,2,1,2])

with col1:
    st.number_input("X Lag", 0, 10, key="xlag")

with col2:
    st.number_input("Y Lag", 0, 10, key="ylag")

with col3:
    st.number_input("NL Degree", 1, 5, key="degree")

if st.checkbox("e"):
    st.number_input("e Lag", 0, 10, key="elag")
else: st.session_state.elag = 0

st.selectbox("Estimação de parâmetros e regressores", ["m1", "m2", "m3", "m4"], key="method")

st.session_state