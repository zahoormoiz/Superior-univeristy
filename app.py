from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoders
model = joblib.load('model.pkl')
le_country = joblib.load('le_country.pkl')
le_rating = joblib.load('le_rating.pkl')
le_director = joblib.load('le_director.pkl')
le_type = joblib.load('le_type.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        release_year = int(request.form['release_year'])
        duration = int(request.form['duration'])
        country = le_country.transform([request.form['country']])[0]
        rating = le_rating.transform([request.form['rating']])[0]
        director = le_director.transform([request.form['director']])[0]

        features = np.array([[release_year, duration, country, rating, director]])
        prediction = model.predict(features)[0]
        result = le_type.inverse_transform([prediction])[0]

        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
