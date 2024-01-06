import streamlit as st

name = st.text_input("Enter Your Name:")
fname = st.text_input("Enter Your Father Name:")
adr = st.text_area("Enter your Text:")
classdata=st.selectbox("Enter your class:",(1,2,3,4,5,6))

button = st.button("submit")
if button:
    st.markdown(f"""
    Name:{name}
    Father name:{fname}
    Address:{adr}
    class:{classdata}""")

