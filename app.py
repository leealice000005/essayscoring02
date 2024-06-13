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
    print(f"Received essay: {essay}")

    if not essay:
        return render_template('form.html', score=None)

    try:
        score = calculate_score(essay)
        return render_template('form.html', score=score)
    except Exception as e:
        return render_template('form.html', score=f'Error: {e}')

def calculate_score(essay):
    tfidf = TfidfVectorizer()
    lr = LinearRegression()

    X_train = ["example text", "another example", "more text data for training"]
    y_train = [1, 2, 3]

    tfidf.fit(XTrain)
    X_train_transformed = tfidf.transform(XTrain)
    lr.fit(X_train_transformed, y_train)

    X = tfidf.transform([essay])
    score = lr.predict(X)
    return round(score[0], 2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
