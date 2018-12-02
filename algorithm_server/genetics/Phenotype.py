import random

class Phenotype:
    def __init__(self, num):
        self.num = num
        self.genes = [False] * self.num     
    
    def generate_random_genes(self):
        for i in range(self.num):
            if(random.random() > 0.5):
                self.genes[i] = True

    def print(self):
        print(self.genes)

    def set_fitness(self, fitness):
        self.fitness = fitness

    def crossover(self, phenotype, crosses):
        new_phenotype = Phenotype(self.num)
        
        #losowanie bez zwracania
        positions = list(range(0, self.num - 2))
        cross_positions = random.sample(positions, crosses)
        cross_positions.sort()

        parent_id = True
        for i in range(self.num):
            if(parent_id):
                new_phenotype.genes[i] = self.genes[i]
            else:
                new_phenotype.genes[i] = phenotype.genes[i]

            if i in cross_positions:
                parent_id = not parent_id
                cross_positions.remove(i)
        new_phenotype.mutate()
        return new_phenotype

    def mutate(self):
        p = 1/(10*self.num)
        for i in range(self.num):
            if(random.random() < p):
                self.genes[i] = not self.genes[i]


