from coin_set import default_coin_set


class ProblemException(Exception):
    pass

class Problem:
    singleton_problem = None
    
    @staticmethod
    def inicializeSingletonProblem(probelm):
        # if Problem.singleton_problem:
        #     raise ProblemException("singelton reference to probelm was already set")
        Problem.singleton_problem = probelm 
    
    def __init__(self, coin_set=None):
        self.__coin_set = coin_set if coin_set else default_coin_set
        self.__length_of_coin_set = len(self.__coin_set)
        self.__maximun_fitness_value = sum(self.__coin_set)
        Problem.inicializeSingletonProblem(self)
        
    @property
    def MexFitness(self):
        return self.__maximun_fitness_value

    @property
    def CoinSet(self):
        return self.__coin_set

    @property
    def CoinSetSize(self):
        return self.__length_of_coin_set
    
    @property
    def StrCoinSetSize(self):
        return " ".join(map(lambda x: str(x),self.__coin_set))
        
    def costFunction(self, solution):
        value = 0
        if len(solution) != len(self.__coin_set):
            raise ProblemException(f"The size of solution ({len(solution)}) does not match the size of the coin set({len(self.__coin_set)})")    
        for h in range(len(solution)):
            gene = solution[h]
            if gene:
                value += self.__coin_set[h]
        return value