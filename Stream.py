from Imoveis import imoveis
import streamlit as st

click_button = st.button("CalcularImoveis")

if click_button:
    st.dataframe(imoveis())