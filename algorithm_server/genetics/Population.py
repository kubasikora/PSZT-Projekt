from .Phenotype import Phenotype    

class Population:
    def __init__(self, params, judge, a, b):
        self.params = params
        self.parents = []
        self.judge = judge
        self.a = a
        self.b = b

    def push_phenotype(self, phenotype):
        self.parents.append(phenotype)

    def generate_random_population(self):
        for i in range(self.params['mi']):
            p = Phenotype(len(self.params['cards']))
            p.generate_random_genes()
            r = self.judge.goal_eval(self.a, self.b, p)
            self.parents.append(p)

    def create_next_epoch():
        print('dipa') 