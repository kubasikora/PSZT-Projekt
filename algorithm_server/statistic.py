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
__REQUEST_NUM__ = 1000
__MAX_EPOCH__ = 100
__CONF_FILE_PATH__ = './genetics/conf.json'

def url_factory(a,b):
    return __URL__ + '/find-distribution?A=' + str(a) + '&B=' + str(b)

def generate_name_file(A,B):
    return './results/statistic/statisticA=' + str(A) + 'B=' + str(B) + '.mat'

if __name__ == "__main__":
    try:
        _A_ = int(sys.argv[1])
        _B_ = int(sys.argv[2])
    except Exception:
        print("Incorrect arguments given!")
        exit()
    try:
            
        averages = []
        variances = []
        devations = []

        with open(__CONF_FILE_PATH__) as conf_file:
            global_conf = json.load(conf_file)

        cards = global_conf['cards']
        num_of_cards = len(cards)

        judge = Judge(cards)

        bar = IncrementalBar('Spamming the server...', max=__MAX_EPOCH__)
        bar.update()
        for i in range(__MAX_EPOCH__):
            responses = []
            errors = []

            tmp_conf = copy.deepcopy(global_conf)
            tmp_conf['epochs'] = i+1 
            tmp_conf_json = json.dumps(tmp_conf)

            conf_file = open(__CONF_FILE_PATH__, "w")
            conf_file.write(tmp_conf_json)
            conf_file.close()

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
                
            averages.append(np.mean(errors))
            variances.append(np.var(errors))
            devations.append(np.std(errors))
            bar.next()
        bar.finish()


        # save statistics to matlab
        statistics = {
            "avg": np.array(averages),
            "var": np.array(variances), 
            "std": np.array(devations),
        }

        filename = generate_name_file(_A_, _B_)
        sio.savemat(filename, statistics)
        
        # revert conf file to original 
        conf_file = open(__CONF_FILE_PATH__, "w")
        conf_file.write(json.dumps(global_conf))
        conf_file.close()

        print('Statistics saved as {0}'.format(filename))
    except (KeyboardInterrupt, Exception):
        print("\nTest interrupted. Reverting global config file...")
        conf_file = open(__CONF_FILE_PATH__, "w")
        conf_file.write(json.dumps(global_conf))
        conf_file.close()


