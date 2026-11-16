import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    app_name = os.environ.get('APP_NAME', 'default-demo')
    return f'Hello from container! App: {app_name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)