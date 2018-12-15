from .Phenotype import Phenotype
import json

"""
    IMPORTANT INFO:
        IF GENE IS TRUE THEN IT IS ASSIGNED TO A GROUP
        ELSE IT IS ASSIGNED TO B GROUP 

"""

class Judge:
    def __init__(self, cards):
        self.cards = cards
        self.cards_length = len(self.cards)
        self.cards_sum = sum(self.cards) 

    def goal_eval(self, a, b, phenotype):
        a_value = 0

        for i in range(self.cards_length):
            if(phenotype.genes[i]):
                a_value = a_value + self.cards[i]
        
        b_value = self.cards_sum - a_value

        error = (a-a_value)**2 + (b-b_value)**2
        phenotype.set_fitness(error)
        return error

