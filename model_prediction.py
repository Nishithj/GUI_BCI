'''def get_model_output(self):
    # Assuming you have a preloaded model and input pipeline
    prediction = your_model.predict(input_data)
    direction = decode_prediction(prediction)  # e.g., convert [0, 1, 0, 0] to "down"
    return direction'''

import joblib
import numpy as np

# Load the model and scaler once
model = joblib.load(r"C:\Users\HP\Desktop\ensemble_model.pkl")
scaler = joblib.load(r"C:\Users\HP\Desktop\scaler.pkl")

'''def get_model_output(input_data):
    """
    input_data: should be shaped and preprocessed the same way as training data.
    Expected shape: (1, n_channels * n_timepoints * ...)
    """
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    # Decode prediction into direction (e.g., class 0 = 'up', etc.)
    class_to_direction = {0: "up", 1: "down", 2: "left", 3: "right"}
    return class_to_direction.get(prediction[0], "up")'''

def get_model_output(input_data):
    print("📡 get_model_output() called")
    print("Input shape:", input_data.shape)

    input_scaled = scaler.transform(input_data)
    probs = model.predict_proba(input_scaled)
    print("📊 Class Probabilities:", probs[0])

    prediction = model.predict(input_scaled)

    class_to_direction = {0: "up", 1: "down", 2: "left", 3: "right"}
    direction = class_to_direction.get(prediction[0], "up")
    
    print("🔁 Predicted class:", prediction[0], "→", direction)
    return direction


if __name__ == "__main__":
    print("✅ Model and scaler loaded.")
    
    # Simulate 4 test samples, each of shape (1, 7260)
    for i in range(4):
        fake_input = np.random.rand(1, 7260)  # Must match model input size

        direction = get_model_output(fake_input)
        print(f"🎯 Sample {i+1}: Predicted Direction → {direction}")


