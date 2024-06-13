from flask import Flask, request, render_template, redirect, url_for, Response
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import os
from dotenv import load_dotenv

load_dotenv()  # 加载 .env 文件

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # 请替换为实际的密钥

class LoginForm(FlaskForm):
    account = StringField('Account', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        input_account = form.account.data
        input_password = form.password.data
        if input_account == os.getenv('ACCOUNT') and input_password == os.getenv('PASSWORD'):
            return redirect(url_for('score'))
        else:
            return "Authentication failed!", 401
    return render_template('index.html', form=form)

@app.route('/score', methods=['GET', 'POST'])
def score():
    if request.method == 'POST':
        essay = request.form['essay']
        # 在这里添加评分逻辑
        score = len(essay)  # 示例评分逻辑
        return render_template('form.html', score=score)
    return render_template('form.html')

if __name__ == '__main__':
    print("Starting Flask app")
    app.run(host='0.0.0.0', port=5000)
    print("Flask app is running")
