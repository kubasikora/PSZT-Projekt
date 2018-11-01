from flask import Flask, Response, request
from flask_cors import CORS
import os
import json

app = Flask(__name__) # utworzenie obiektu serwera
CORS(app) # włączenie mechanizmu Cross-Origin-Resource-Sharing

"""
    Zwraca informację o stanie serwera.
    Przykładowe wywołanie:
        GET localhost:5000
    Odpowiedź:
        Algorithm server is online!
"""
@app.route("/") #scieżka do której się odwołujemy
def hello(): #handler tej ścieżki
    return "Algorithm server is online!" 
    
      
"""
    Zwraca przekazane argumenty w odpowiedzi typu JSON
    Przykładowe wywołanie:
        GET localhost:5000?A=40&B=300
    Odpowiedź:
        {
            A: 50
            B: 300
        }
"""
@app.route("/test")
def test_handler():
    a_value = request.args.get("A") #pobranie argumentu z URL
    b_value = request.args.get("B") 
    try:
        resp = {                    #utworzenie obiektu odpowiedzi
            "error": False,
            "A": int(a_value),
            "B": int(b_value)
        }
    except ValueError:              #handel sytuacji błędnej
        resp = {
            "error": True,
            "message": "Invalid arguments" 
        }
        
    #generacja odpowiedzi z typem json 
    return Response(json.dumps(resp), mimetype='application/json') 


#kodowanie odpowiedzi
app.config['RESTUFL_JSON'] = {
    'ensure_ascii': False
}

#uruchomienie serwera na porcie wskazanym przez zmienną środowiskową/domyślną wartość
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
 
   
