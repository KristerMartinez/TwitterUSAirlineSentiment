import streamlit as st
import joblib

# Load your trained model
model = joblib.load('finalized_model.pkl')

# Streamlit application
st.title('Sentiment Analysis Tool')

# Text input
user_input = st.text_area("Enter Text", "")

# Predict button
if st.button('Predict'):
    # You will need to vectorize the user input as well
    # Here you can load the vectorizer or redefine it
    result = model.predict([user_input])
    st.write('The sentiment is:', 'Positive' if result[0] == 1 else 'Negative')
