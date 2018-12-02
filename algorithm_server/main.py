from flask import Flask, Response, request
from flask_cors import CORS
from genetics import CardsHandler, Judge, Phenotype, Population
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
	
#kodowanie odpowiedzi
app.config['RESTUFL_JSON'] = {
    'ensure_ascii': False
}

#uruchomienie serwera na porcie wskazanym przez zmienną środowiskową/domyślną wartość
port = int(os.environ.get('PORT', 5000))

p = Population({
    "mi": 10,
    "cards": [1,2,3,4,5,6,7,8,9,10]
}, Judge([1,2,3,4,5,6,7,8,9,10]),
10,
20)
p.generate_random_population()



app.run(host='0.0.0.0', port=port)  
