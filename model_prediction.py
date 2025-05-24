def get_model_output(self):
    # Assuming you have a preloaded model and input pipeline
    prediction = your_model.predict(input_data)
    direction = decode_prediction(prediction)  # e.g., convert [0, 1, 0, 0] to "down"
    return direction
