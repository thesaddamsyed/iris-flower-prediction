import streamlit as st
import pickle
import os

# Fix the file path for Data.pkl
file_path = os.path.join(os.path.dirname(__file__), "Data.pkl")

# Load the model
with open(file_path, "rb") as file:
    model = pickle.load(file)

# Fix image paths
image1 = os.path.join(os.path.dirname(__file__), "Iris Flowers", "Irissetosa1.jpg")
image2 = os.path.join(os.path.dirname(__file__), "Iris Flowers", "Iris_versicolor__flo_npyvSQOSVQ8O.jpeg")
image3 = os.path.join(os.path.dirname(__file__), "Iris Flowers", "iris_virginica_virginica_lg.jpg")

def predict():
    st.title("Predicting the Iris Flower Species")
    
    sepal_length = st.number_input("Enter the Sepal Length of the Flower in cm")
    sepal_width = st.number_input("Enter the Sepal Width of the Flower in cm")
    petal_length = st.number_input("Enter the Petal Length of the Flower in cm")
    petal_width = st.number_input("Enter the Petal Width of the Flower in cm")
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    pred = st.button("Predict")

    if pred:
        op = model.predict(input_data)

        if op[0] == 0:
            st.image(image1, caption="Iris Setosa")
        elif op[0] == 1:
            st.image(image2, caption="Iris Versicolor")
        elif op[0] == 2:
            st.image(image3, caption="Iris Virginica")

predict()
