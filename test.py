from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
