import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'
if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))