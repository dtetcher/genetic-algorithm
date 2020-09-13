import random
from typing import List
from abstract.population import IPopulationUnit, IPopulation
from abstract.fitness import FitnessFunction


class Chromosome(IPopulationUnit):
    # Phenotype - an integer representation of chromosome
    # Population - binary representation

    def __init__(self, l_border, u_border, value: int = None):
        if value is not None:
            if not l_border <= value <= u_border:
                raise ValueError("Chromosome value must be in specified range.")
            self.__phenotype = value
        else:
            self.__phenotype = random.uniform(l_border, u_border)
        self.__population = bin(self.__phenotype)
        self.__fitness_score: float = 0.

    def has_len(self, _len: int) -> bool:
        return _len == len(self.population[2:])

    @property
    def phenotype(self):
        return self.__phenotype

    @property
    def population(self):
        return self.__population

    @property
    def fitness_score(self):
        return self.__fitness_score
    

class BinaryPopulation(IPopulation):

    def __init__(self, input_set: List[IPopulationUnit], unit_length: int):

        if not all(unit.has_len(unit_length) for unit in input_set):
            raise ValueError("Population elements should be equal in their size.")

        self.__population = input_set
        self.__unit_length = unit_length

    def unit_length(self, value=None):

        if value is not None:
            self.__unit_length = value

        else:
            return self.__unit_length

    @property
    def population(self):
        return self.__population

    def get_fittest(self, count: int) -> List[IPopulationUnit]:

        return sorted(self.__population,
                      key=lambda unit: unit.fitness_score,
                      reverse=True)[:count]

    def apply_fitness(self, func: FitnessFunction):

        for unit in self.__population:
            unit.fitness_score = func.fitness(unit.phenotype)
