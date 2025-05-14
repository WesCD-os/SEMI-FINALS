import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1>NAME : LOUIES ANDRE TABANAO</h1>'
            '<h1>COURSE : BSIT</h1>'
            '<h1>SUBJECT : SYSTEM INTEGRATION</h1>')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
