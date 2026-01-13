from time import perf_counter, sleep

import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


@st.cache_resource
def load_model():
    iris = load_iris()
    X, y = iris.data, iris.target_names[iris.target]
    model = RandomForestClassifier()
    model.fit(X, y)
    sleep(5)  # Simulating a long loading time
    return model


st.title("Cache Resource Example")

sepal_length = st.slider("Sepal Length", 4.0, 8.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5)
petal_length = st.slider("Petal Length", 1.0, 7.0)
petal_width = st.slider("Petal Width", 0.1, 2.5)

input_data = pd.DataFrame(
    [[sepal_length, sepal_width, petal_length, petal_width]],
    columns=["sepal_length", "sepal_width", "petal_length", "petal_width"],
)

start = perf_counter()
model = load_model()
st.write(f"Time taken to load the model: {(perf_counter() - start):.3f}s")

prediction = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)

st.write(f"Prediction: {prediction[0]}")
st.write(f"Prediction Probability: {max(prediction_proba[0])}")
