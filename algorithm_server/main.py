from flask import Flask, Response, request
from flask_cors import CORS
from genetics import CardsHandler, Judge, Phenotype, Population
import os
import json
import logging

app = Flask(__name__) # utworzenie obiektu serwera
CORS(app) # włączenie mechanizmu Cross-Origin-Resource-Sharing

"""
    Zwraca informację o stanie serwera.
    Przykładowe wywołanie:
        GET localhost:5000/
    Odpowiedź:
        Algorithm server is online!
"""
@app.route("/") #scieżka do której się odwołujemy
def hello(): #handler tej ścieżki
    return "Algorithm server is online!" 
    
      


"""
    Zwraca przekazane argumenty zagregowane w tablicę
    Przykładowe wywołanie:
        GET localhost:5000/test?A=40&B=300
    Odpowiedź:
        { 
            "error": false,
            "A": [12, 12, 12, 12, 12], 
            "B": [33, 33, 33, 33, 33]
        }
"""
@app.route("/test")
def test_handler():
    try:
        a_value = request.args.get("A") #pobranie argumentu z URL
        b_value = request.args.get("B") 
        resp = {                    #utworzenie obiektu odpowiedzi
            "error": False,
            "A": 5*[int(a_value)],
            "B": 5*[int(b_value)]
        }
    except ValueError:              #handel sytuacji błędnej
        resp = {
            "error": True,
            "message": "Invalid arguments" 
        }
    except TypeError:
        resp = {
            "error": True,
            "message": "Missing arguments" 
        }
        
    #generacja odpowiedzi z typem json 
    return Response(json.dumps(resp), mimetype='application/json') 




"""
    Zwraca podział kart zgodnie z zadaniem
    Przykładowe wywołanie:
        GET localhost:5000/find-distribution?A=12&B=33
    Odpowiedź:
        { 
            "error": false,
            "A": [1, 2, 4, 10],
            "B": [3, 5, 6, 7, 8, 9]
        }
"""
@app.route("/find-distribution")
def find_distribution_handler():
    try:
        a_value = int(request.args.get("A"))
        b_value = int(request.args.get("B"))
        
    except (ValueError, TypeError):
        resp = {
            "error": True,
            "message": "Invalid arguments" 
        }
        return Response(json.dumps(resp), mimetype='application/json')

    handler = CardsHandler(a_value, b_value)
    result = handler.evaluate()
    resp = {
        "error": False,
        "A": result['A'],
        "B": result['B']
    }
    return Response(json.dumps(resp), mimetype='application/json')
	



"""
    Zwraca ustawione parametry algorytmu
    Przykładowe wywołanie:
        GET localhost:5000/parameters
    Odpowiedź:
        {
            "cards": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
            "mi": 40, 
            "lambda": 20, 
            "crosses": 2, 
            "epochs": 100
        }
"""
@app.route("/parameters")
def parameters_handler():
    with open('./genetics/conf.json') as conf_file:
        configuration = json.load(conf_file)
    return Response(json.dumps(configuration), mimetype='application/json')
    


#kodowanie odpowiedzi
app.config['RESTUFL_JSON'] = {
    'ensure_ascii': False
}

#uruchomienie serwera na porcie wskazanym przez zmienną środowiskową/domyślną wartość
port = int(os.environ.get('PORT', 5000))
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app.run(host='0.0.0.0', port=port)  
