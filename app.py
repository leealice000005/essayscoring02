from flask import Flask, request, Response
import os
from dotenv import load_dotenv

load_dotenv()  # 加载 .env 文件

app = Flask(__name__)

def check_auth(username, password):
    return username == os.environ.get('HTTP_AUTH_USER') and password == os.environ.get('HTTP_AUTH_PASSWORD')

def authenticate():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

@app.route('/')
def index():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    return "Hello, authenticated world!"

if __name__ == '__main__':
    print("Starting Flask app")
    app.run(host='0.0.0.0', port=5000)
    print("Flask app is running")
