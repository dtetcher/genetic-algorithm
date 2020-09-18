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

            phenotype = value
        else:
            phenotype = random.randint(a, b)


        population_g = binary.to_gray(bin(phenotype),
                                      # If translate maximal possible value to binary format
                                      # then we can get length of chromosome population.
                                      len(bin(b)[2:]))
        fitness_score = 0.
        super().__init__(phenotype, population_g, fitness_score)

    def _population_value_setter(self, value):
        self._population_value = value
        self.phenotype = int(binary.from_gray(value), 2)


class BinaryPopulation(IPopulation):

    def __init__(self, input_set: List[Chromosome]):
        super().__init__(input_set)

    def apply_fitness(self, func: FitnessFunction):

        for unit in self.population:
            unit.fitness_score = func.fitness(unit.phenotype)

    def get_fittest(self, count: int = 1) -> List[Chromosome]:

        return sorted(self.population,
                      key=lambda unit: unit.fitness_score,
                      reverse=True)[:count]

    def get_pairs(self) -> dict:
        ids = [i for i in range(len(self.population))]
        pairs = {}

        while len(ids) != 0:

            k = random.choice(ids)
            ids.remove(k)

            v = random.choice(ids)
            ids.remove(v)

            pairs[k] = v

        return pairs


