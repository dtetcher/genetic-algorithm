import abc

from abstract.population import Chromosome
from abstract.ga import GA


class CrossoverOperator(abc.ABC):
    @abc.abstractmethod
    def crossover(self, ga: GA):
        pass
