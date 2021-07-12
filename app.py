import streamlit as st
import joblib
model = joblib.load('Twitter_Reviews')
st.title('Twitter Reviews Classifier')
ip = st.text_input('Enter your Tweet')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
