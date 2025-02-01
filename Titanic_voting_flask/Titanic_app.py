from flask import Flask, request, render_template
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
#model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
voting_clf= pickle.load(open("iris_voting_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        age = float(request.form['age'])
        fare = float(request.form['fare'])
        sibsp = int(request.form['sibsp'])
        parch = int(request.form['parch'])

        # Prepare input for prediction
        input_data = np.array([[age, fare, sibsp, parch]])
        # Prepare input for scaling
        scaled_input=scaler.transform(input_data)

        # Make prediction
        prediction = voting_clf.predict(scaled_input)

        # Prepare result text
        prediction_text = f"Prediction: {'Survived' if prediction[0] == 1 else 'Not Survived'}"

    except Exception as e:
        prediction_text = f"Error: {str(e)}"

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
