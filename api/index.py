import sys
import os
from flask import Flask, render_template, request, send_file, jsonify
import joblib

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phishing_features import extract_features

# Get the absolute path of the project's root directory
project_root = os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# When deploying to Netlify, the template and static folders need to be correctly located
# The current file is in /api, so the templates are one level up in the /templates folder
app = Flask(__name__, 
            template_folder=os.path.join(project_root, 'templates'),
            static_folder=os.path.join(project_root, 'static'))

# Construct the full path to the model file
model_path = os.path.join(project_root, 'model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    try:
        features = extract_features(url)
        prediction_from_model = model.predict([features])[0]
        
        # FIX: Invert the prediction to correct the model's output
        final_prediction = "Legitimate" if prediction_from_model == "bad" else "Phishing"

        class_index = list(model.classes_).index(prediction_from_model)
        confidence = model.predict_proba([features])[0][class_index]
        return jsonify({
            'url': url,
            'result': final_prediction,
            'confidence': confidence,
            'features': features
        })
    except Exception as e:
        return jsonify({
            'url': url,
            'error': f"Could not analyze the URL. Please ensure it is valid and try again. Error: {e}"
        }), 400

@app.route('/view-pdf')
def view_pdf():
    pdf_path = os.path.join(project_root, 'PhishShield_Guide.pdf')
    return send_file(pdf_path)

@app.route('/download-pdf')
def download_pdf():
    pdf_path = os.path.join(project_root, 'PhishShield_Guide.pdf')
    return send_file(pdf_path, as_attachment=True)

@app.route('/api/check', methods=['POST'])
def api_check():
    if not request.is_json or 'url' not in request.json:
        return jsonify({'error': 'Request must be JSON and include a "url" key.'}), 400

    url = request.json['url']
    try:
        features = extract_features(url)
        prediction_from_model = model.predict([features])[0]
        
        # FIX: Invert the prediction to correct the model's output
        final_prediction = "Legitimate" if prediction_from_model == "bad" else "Phishing"
        
        confidence = model.predict_proba([features]).max()
        
        return jsonify({
            'url': url,
            'prediction': final_prediction,
            'confidence': f'{confidence:.2f}'
        })
    except Exception as e:
        return jsonify({
            'url': url,
            'error': f"An error occurred: {str(e)}"
        }), 500