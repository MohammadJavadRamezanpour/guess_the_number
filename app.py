import numpy as np
import joblib

model = joblib.load("model.joblib")

while True:
    user_input = input(">>> ")

    if user_input.lower() == "q":
        break

    matrix_like_user_input = np.array([[float(user_input)]])
    prediction = model.predict(matrix_like_user_input)

    print(prediction[0])