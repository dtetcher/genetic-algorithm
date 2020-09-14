from typing import List
import random

from abstract.population import Chromosome, IPopulation
from abstract.fitness import FitnessFunction
from helpers import binary


class BinaryChromosome(Chromosome):

    def __init__(self, a, b, value: int = None):

        if value is not None:

            if not a <= value <= b:
                raise ValueError("Chromosome value must be in specified range.")

            self.__phenotype = value
        else:
            self.__phenotype = random.uniform(a, b)

        self.__population_G = binary.to_gray(bin(self.__phenotype))
        self.__fitness_score: float = 0.

    def has_len(self, _len: int) -> bool:
        return _len == len(self.population_val())

    def phenotype(self, value=None):
        if value is not None:
            self.__phenotype = value
        else:
            return self.__phenotype

    def population_val(self, value=None):
        if value is not None:
            self.__population_G = value
        else:
            return self.__population_G

    def fitness_score(self, value=None):
        if value is not None:
            self.__fitness_score = value
        else:
            return self.__fitness_score
    

class BinaryPopulation(IPopulation):

    def __init__(self, input_set: List[Chromosome]):

        random_unit_length = len(random.choice(input_set)
                                 .population_val())

        if not all(unit.has_len(random_unit_length) for unit in input_set):
            raise ValueError("Population elements should be equal in their size.")

        self.__population = input_set
        self.__unit_length = random_unit_length

    def unit_length(self, value=None):
        if value is not None:
            self.__unit_length = value
        else:
            return self.__unit_length

    def population(self, value=None):
        if value is not None:
            self.__population = value
        else:
            return self.__population

    def get_fittest(self, count: int) -> List[Chromosome]:

        return sorted(self.__population,
                      key=lambda unit: unit.fitness_score,
                      reverse=True)[:count]

    def get_pairs(self) -> dict:
        ids = [i for i in range(len(self.__population))]
        pairs = {}

        while len(ids) != 0:
            k = ids.pop(random.choice(ids))
            v = ids.pop(random.choice(ids))
            pairs[k] = v

        return pairs

    def apply_fitness(self, func: FitnessFunction):

        for unit in self.__population:
            unit.fitness_score = func.fitness(unit.phenotype())

