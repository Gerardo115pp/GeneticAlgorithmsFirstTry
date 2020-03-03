from random import randint
from Problem import Problem

class SolutionException(Exception):
    pass

class Solution:
    def __init__(self, genoma):
        self.genoma = genoma if genoma else []
        if genoma:
            self.__calculateFitness()
            if randint(0,100) < 35:
                self.__mutate()
        else:
            self.fitness_score = None
    
    def __str__(self):
        return f"fitness: {self.fitness_score}"
    
    def __calculateFitness(self):
        if self.genoma:
            self.fitness_score = Problem.singleton_problem.costFunction(self.genoma)
    
    def __getCrossoverPoint(self):
        return randint(0,Problem.singleton_problem.CoinSetSize-1)
    
    def __ensureValid(self, mutation_point, mutation=True, current_genoma=None):
        current_genoma = current_genoma if current_genoma else self.genoma
        if current_genoma[mutation_point] and mutation:
            return True
        
        elif mutation_point == 0:
            return current_genoma[1] != 1
        elif mutation_point == (len(current_genoma)-1):
            return current_genoma[len(current_genoma)-2] != 1
        else:
            return current_genoma[mutation_point-1] != 1 and current_genoma[mutation_point+1] != 1
            
            
    def __mutate(self):
        mutation_point = randint(0,len(self.genoma)-1)
        
        while not self.__ensureValid(mutation_point):
            mutation_point = randint(0,len(self.genoma)-1)
        
        self.genoma[mutation_point] = abs(self.genoma[randint(0,len(self.genoma)-1)] - 1)
    
    def reproduce(self, partner_genoma):
        childes = (self.genoma[:], partner_genoma[:])
        crossover_point = self.__getCrossoverPoint()
        for h in range(crossover_point, Problem.singleton_problem.CoinSetSize):
            childes[0][h] = partner_genoma[h]
            childes[1][h] = self.genoma[h]
            
            if childes[0][h]:
                childes[0][h] = childes[0][h] if self.__ensureValid(h, False, childes[0]) else 0
            if childes[1][h]:
                childes[1][h] = childes[1][h] if self.__ensureValid(h, False, childes[1]) else 0
             
        return [Solution(childes[0]), Solution(childes[1])]
    
    def generateInitialGenoma(self):
        if not self.genoma:
            h = 0
            while h < Problem.singleton_problem.CoinSetSize:
                gene = randint(0,1)
                if gene:
                    gene = [gene, 0] if h+1 < Problem.singleton_problem.CoinSetSize else [gene]
                    self.genoma += gene
                    h += 2
                else:
                    self.genoma.append(gene)
                    h += 1
            self.__calculateFitness()
    