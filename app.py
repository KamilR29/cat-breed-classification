import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Wczytanie wytrenowanego modelu
model = joblib.load("best_cat_classifier_full.pkl")

# Słowniki kodowania (zgodnie z trainingiem)
category_maps = {
    'Gender': {'male': 0, 'female': 1, 'unknown': 2},
    'Fur_colour_dominant': {
        'white': 0, 'black': 1, 'gray': 2, 'red/cream': 3, 'brown': 4,
        'cream': 5, 'unknown': 6
    },
    'Fur_pattern': {'solid': 0, 'tabby': 1, 'dirty': 2, 'unknown': 3},
    'Eye_colour': {'blue': 0, 'green': 1, 'yellow': 2, 'unknown': 3},
    'Preferred_food': {'wet': 0, 'dry': 1, 'both': 2, 'unknown': 3},
    'Country': {'france': 0, 'germany': 1, 'poland': 2, 'spain': 3, 'unknown': 4}
}

breed_labels = {
    0: "Angora", 1: "British Shorthair", 2: "Maine Coon",
    3: "Norwegian", 4: "Persian", 5: "Sphynx",
    6: "Siamese", 7: "Turkish Van", 8: "Unknown"
}

# UI
st.title("🐾 Cat Breed Classifier")
st.write("Wprowadź cechy kota, aby przewidzieć jego rasę:")

with st.form("input_form"):
    age = st.slider("Wiek kota (w miesiącach)", 1, 240, 12)
    gender = st.selectbox("Płeć", list(category_maps['Gender'].keys()))
    neutered = st.selectbox("Czy wykastrowany/wysterylizowany?", [True, False])
    body_length = st.slider("Długość ciała (cm)", 10.0, 100.0, 30.0)
    weight = st.slider("Waga (kg)", 0.5, 20.0, 4.0)
    fur_col = st.selectbox("Dominujący kolor futra", list(category_maps['Fur_colour_dominant'].keys()))
    fur_pat = st.selectbox("Wzór futra", list(category_maps['Fur_pattern'].keys()))
    eye_col = st.selectbox("Kolor oczu", list(category_maps['Eye_colour'].keys()))
    outdoor = st.selectbox("Dostęp do zewnątrz?", [True, False])
    food = st.selectbox("Preferowane jedzenie", list(category_maps['Preferred_food'].keys()))
    play = st.slider("Minut zabawy dziennie", 0, 180, 60)
    sleep = st.slider("Godzin snu dziennie", 0.0, 24.0, 12.0)
    country = st.selectbox("Kraj", list(category_maps['Country'].keys()))
    lat = st.number_input("Szerokość geograficzna", value=52.2297)
    lon = st.number_input("Długość geograficzna", value=21.0122)

    submitted = st.form_submit_button("Przewiduj rasę")

if submitted:
    # Składanie danych wejściowych
    row = {
        'Age_in_months': age,
        'Gender': category_maps['Gender'][gender],
        'Neutered_or_spayed': int(neutered),
        'Body_length': body_length / 100.0,
        'Weight': weight / 20.0,
        'Fur_colour_dominant': category_maps['Fur_colour_dominant'][fur_col],
        'Fur_pattern': category_maps['Fur_pattern'][fur_pat],
        'Eye_colour': category_maps['Eye_colour'][eye_col],
        'Allowed_outdoor': int(outdoor),
        'Preferred_food': category_maps['Preferred_food'][food],
        'Owner_play_time_minutes': play / 180.0,
        'Sleep_time_hours': sleep / 24.0,
        'Country': category_maps['Country'][country],
        'Latitude': lat,
        'Longitude': lon
    }

    input_df = pd.DataFrame([row])

    prediction = model.predict(input_df)[0]
    breed_name = breed_labels.get(prediction, "Nieznana rasa")

    st.success(f"🏷️ Przewidywana rasa kota: **{breed_name}**")
