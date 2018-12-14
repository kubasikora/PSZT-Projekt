from .Phenotype import Phenotype    
import random
from functools import cmp_to_key

class Population:
    def __init__(self, params, judge, a, b):
        if not isinstance(a, (int, float)): 
            raise TypeError
        if not isinstance(b, (int, float)):
            raise TypeError

        self.params = params
        self.parents = []
        self.judge = judge
        self.a = a
        self.b = b

    def push_phenotype(self, phenotype):
        if not isinstance(phenotype, Phenotype):
            raise TypeError
        self.parents.append(phenotype)

    def generate_random_population(self):
        for i in range(self.params['mi']):
            p = Phenotype(len(self.params['cards']))
            p.generate_random_genes()
            r = self.judge.goal_eval(self.a, self.b, p)
            self.parents.append(p)

    def get_the_best_error(self):
        self.parents.sort(key=lambda ph: ph.fitness)
        return self.parents[0].genes

    def create_next_epoch(self):
        kids = []

        for i in range(self.params['lambda']):
            [father, mother] = random.sample(self.parents, 2)
            kid = mother.crossover(father, self.params['crosses'])
            self.judge.goal_eval(self.a, self.b, kid)
            kids.append(kid)

        merged_phenotypes = kids + self.parents
        merged_phenotypes.sort(key=lambda ph: ph.fitness)

        #strategia elitarna 
        next_population = Population(self.params, self.judge, self.a, self.b)
        for i in range(self.params['mi']):
            next_population.push_phenotype(merged_phenotypes[i])

        return next_population
    