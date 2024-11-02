import streamlit as st
from transformers import pipeline

# Initialize the NLP model (you can choose a different model if needed)
model_name = "distilbert-base-uncased"
nlp_model = pipeline("fill-mask", model=model_name)

# Function to provide recommendations based on symptoms
def get_recommendation(symptoms):
    # Simple logic for demonstration purposes (replace with actual model logic)
    if "rash" in symptoms.lower():
        return "It might be a skin issue. Consider visiting a Dermatologist."
    elif "headache" in symptoms.lower():
        return "It could be related to your nervous system. A Neurologist may help."
    elif "pregnant" in symptoms.lower() or "pregnancy" in symptoms.lower():
        return "It's best to consult an Obstetrician/Gynecologist."
    elif "stomach" in symptoms.lower() or "abdominal" in symptoms.lower():
        return "You might need to see a Gastroenterologist."
    elif "chest pain" in symptoms.lower():
        return "It could be heart-related; please consult a Cardiologist."
    elif "tired" in symptoms.lower() or "fatigue" in symptoms.lower():
        return "It may require a check-up with an Internal Medicine doctor."
    elif "eye" in symptoms.lower() or "vision" in symptoms.lower():
        return "You should see an Ophthalmologist."
    elif "child" in symptoms.lower():
        return "For children, a Pediatrician is recommended."
    else:
        return "Please consult a Family Medicine doctor for further assessment."

# Streamlit App
st.title("Health Chatbot")
st.subheader("Describe your symptoms to get a recommendation.")

# Input field for user symptoms
symptoms = st.text_input("What symptoms are you experiencing?")

# Button to get recommendation
if st.button("Get Recommendation"):
    if symptoms:
        recommendation = get_recommendation(symptoms)
        st.write(recommendation)
    else:
        st.warning("Please enter your symptoms.")

