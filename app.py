import streamlit as st

st.title("GIẢI PHƯƠNG TRÌNH BẬC NHẤT")
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')

if st.button('Giải'):
  if a==0:
    st.write('Phương trình có vô số nghiệm')
  else:
    st.write('Phương trình có 1 nghiệm ' + str(-b/a))
 
