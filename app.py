from flask import Flask, request, render_template
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/score', methods=['POST'])
def score():
    essay = request.form['essay']
    print(f"Received essay: {essay}")  # 添加调试信息

    if not essay:
        return render_template('form.html', score=None)

    try:
        score = calculate_score(essay)
        return render_template('form.html', score=score)
    except Exception as e:
