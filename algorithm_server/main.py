from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World!"
    
    
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
    
   
