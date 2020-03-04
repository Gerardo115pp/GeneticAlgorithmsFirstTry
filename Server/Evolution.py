from Problem import Problem
from Solution import Solution, randint


class EvolutionException(Exception):
    pass

class Evolution:
    def __init__(self, coin_set=None, max_chances=100):
        if not Problem.singleton_problem:
            Problem(coin_set)
        self.__population_size = 10
        self.population = self.__createInitialPopulation()
        self.best_fit = None
        self.__current_generation = 1
        self.max_chances = max_chances
        self.__same_best_chances = self.max_chances

    @property
    def GenerationsNeed(self):
        return self.__current_generation

    def runEvolutionLoop(self):
        while True:
            self.__crossover()
            if self.__checkTermination():
                #print(f"Best fit: {self.best_fit.fitness_score}\nGenes: {self.best_fit.genoma}")
                break
            #print(f"Developing generation {self.__current_generation} with best fit of {self.best_fit}")
        return self.best_fit    

    def __selectionOfTheFittests(self):
        sorted_population = sorted(self.population, key=lambda s: s.fitness_score)[::-1]
        return sorted_population[0]

    def deleteTwoLessFited(self):
        sorted_population = sorted(self.population, key=lambda s: s.fitness_score)
        self.population.remove(sorted_population[0])
        self.population.remove(sorted_population[1])

    def __checkTermination(self):
        current_best = self.__selectionOfTheFittests()
        if not self.best_fit: 
            self.best_fit = current_best
        else:
            if current_best.fitness_score > self.best_fit.fitness_score:
                self.best_fit = current_best
                self.__same_best_chances = self.max_chances
            else:
                if not self.__same_best_chances:
                    return True
                self.__same_best_chances -= 1
        return False
    
    def getProblem(self):
        return Problem.singleton_problem.StrCoinSetSize
           
    def __FitnessChoice(self):
        total_fitness = sum([s.fitness_score for s in self.population])
        if total_fitness == 0:
            return randint(0, len(self.population)-1)
        
        random_fitness_number = randint(0, total_fitness + 1)
        selection_index = 0
        Fit_Solution = self.population[selection_index].fitness_score
        while Fit_Solution < random_fitness_number and selection_index < len(self.population)-1:
            selection_index += 1
            Fit_Solution += self.population[selection_index].fitness_score
        return selection_index
            

    def __crossover(self):
        
        father = self.population[self.__FitnessChoice()]
        mother = self.population[self.__FitnessChoice()]
        while father == mother:
            mother = self.population[self.__FitnessChoice()]
        offsprings = mother.reproduce(father.genoma)
        self.deleteTwoLessFited()
        self.population += offsprings
        self.__current_generation += 1  
        
    def __createInitialPopulation(self):
        population = []
        for h in range(self.__population_size):
            population.append(Solution(None))
            population[h].generateInitialGenoma()        
        return population
        

if __name__ == "__main__":
    evolution = Evolution()
    evolution.runEvolutionLoop()
    