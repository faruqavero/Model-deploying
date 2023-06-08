from flask import Flask, jsonify, request
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path='C:\\Users\\windows 8\\Documents\\Model Capstone\\model-1.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Define class labels
class_labels = ['ESFP', 'INFJ', 'ENFP', 'ENTP', 'ESTJ', 'ISTJ', 'ISTP', 'ESTP', 'ISFP', 'ESFJ', 'ENFJ', 'INTJ', 'INTP', 'ISFJ', 'ENTJ', 'INFP']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data
        data = request.json
        input_data = np.array(data['input']).astype(np.float32)  # Convert to FLOAT32

        # Check if input length matches the expected length
        if len(input_data) != 60:
            return jsonify({'error': 'Input length should be 60.'}), 400

        # Reshape input data
        input_data = np.reshape(input_data, (1, 60))

        print('input_data:', input_data)
        print('input:', input)

        # Set the input tensor
        interpreter.set_tensor(input_details[0]['index'], input_data)

        # Run inference
        interpreter.invoke()

        # Get the output tensor
        output_data = interpreter.get_tensor(output_details[0]['index'])
        predicted_class = int(np.argmax(output_data))  # Convert to int

        # Get the predicted label
        predicted_label = class_labels[predicted_class]

        # Prepare the response
        response = {
            'predicted_class': predicted_class,
            'predicted_label': predicted_label
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()
