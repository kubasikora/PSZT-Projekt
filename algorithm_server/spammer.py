#!/usr/bin/env python

import requests
import copy
import json
import sys

import numpy as np
import scipy.io as sio
from progress.bar import IncrementalBar
from genetics import Phenotype, Judge

__URL__  = 'http://localhost:5000'
__REQUEST_NUM__ = 500

def url_factory(a,b):
    return __URL__ + '/find-distribution?A=' + str(a) + '&B=' + str(b)

def generate_name_file(A,B, conf):
    return './results/spammer/spammer_test_' + 'A=' + \
    str(A) + 'B=' + str(B) + 'epochs=' + str(conf['epochs']) + 'mi=' + \
    str(conf['mi']) +'lambda=' + str(conf['lambda']) + '.mat'

if __name__ == "__main__":
    try:
        _A_ = int(sys.argv[1])
        _B_ = int(sys.argv[2])
    except Exception:
        print("Incorrect arguments given!")
        exit()

    responses = []
    errors = []

    with open('./genetics/conf.json') as conf_file:
        conf = json.load(conf_file)
    
    cards = conf['cards']
    epochs = conf['epochs']
    num_of_cards = len(cards)
    judge = Judge(cards)

    bar = IncrementalBar('Spamming the server...', max=__REQUEST_NUM__)
    for i in range(__REQUEST_NUM__):
        try: 
            r = requests.get(url_factory(_A_, _B_))
        except Exception:
            print("Could not connect to server")
            exit()
        if r.status_code != 200:
            print("Non 2xx code returned from the server")
            exit()

        response = r.json()
        responses.append(response)

        ph = Phenotype(num_of_cards)
        for j in range(num_of_cards):
            if j+1 in response['A']:
                ph.genes[j] = True
            else:
                ph.genes[j] = False    
        judge.goal_eval(_A_, _B_, ph)
        errors.append(ph.fitness) 

        bar.next()
    bar.finish()

    filename = generate_name_file(_A_, _B_, conf)
    
    statistics = {
        "errors": np.array(errors),
    }
    sio.savemat(filename, statistics)
    
    print('Errors array saved as {0}'.format(filename))
    print('Error average: {0}'.format(np.mean(errors)))
    print('Error standard devation: {0}'.format(np.std(errors)))
    print('Error variance: {0}'.format(np.var(errors)))

