import streamlit as st
import pyshorteners as pyst
import clipboard

shortener = pyst.Shortener()
st.markdown("<h1 style='text-align:center;'>URLs Shortener</h1>", unsafe_allow_html=True)
form = st.form("name")
url = form.text_input("Url Here")
st_btn = form.form_submit_button("submit")
if st_btn:
    shorted = shortener.tinyurl.short(url)
    st.write(f"Shortened URL: {shorted}")
 




