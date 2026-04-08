import os
import numpy as np
import joblib
from django.shortcuts import render


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'ml_model', 'StellarModel.joblib')

try:
    model = joblib.load(MODEL_PATH)
    MODEL_LOADED = True
except Exception as e:
    model = None
    MODEL_LOADED = False
    print(f"[StellarAI] Could not load model: {e}")


LABEL_MAP = {
    0: 'GALAXY',
    1: 'QSO',
    2: 'STAR',
}


def get_input_features(post_data):
    required_fields = ['alpha', 'delta', 'u', 'g', 'r', 'i', 'z', 'redshift']
    form_data = {}

    for field in required_fields:
        value = post_data.get(field, '').strip()
        if value == '':
            return None, form_data, f"'{field}' is required."
        form_data[field] = value

    float_data = {}
    for field in required_fields:
        try:
            float_data[field] = float(form_data[field])
        except ValueError:
            return None, form_data, f"'{field}' must be a valid number."

    features = np.array([[
        float_data['alpha'],
        float_data['delta'],
        float_data['u'],
        float_data['g'],
        float_data['r'],
        float_data['i'],
        float_data['z'],
        float_data['redshift'],
    ]])

    return features, form_data, None


def home(request):
    return render(request, 'home.html')


def classify(request):
    if request.method == 'GET':
        return render(request, 'classifier.html')

    if not MODEL_LOADED or model is None:
        return render(request, 'classifier.html', {
            'error': "Model file not found. Place 'StellarModel.joblib' in the 'ml_model/' folder.",
            'form_data': request.POST,
        })

    features, form_data, error = get_input_features(request.POST)

    if error:
        return render(request, 'classifier.html', {
            'error': error,
            'form_data': form_data,
        })

    raw_prediction = model.predict(features)[0]

    if isinstance(raw_prediction, (int, np.integer)):
        prediction = LABEL_MAP.get(int(raw_prediction), 'UNKNOWN')
    else:
        prediction = str(raw_prediction).upper()

    return render(request, 'classifier.html', {
        'prediction': prediction,
        'form_data': form_data,
    })
