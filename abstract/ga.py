from typing import List
import abc

from abstract.population import Chromosome


class GA(abc.ABC):

    @abc.abstractmethod
    def selection(self):
        pass

    @abc.abstractmethod
    def crossover(self, first: Chromosome, second: Chromosome):
        pass

    @abc.abstractmethod
    def mutation(self, _population: List[Chromosome] = None):
        pass

    @abc.abstractmethod
    @property
    def generation_No(self):
        return
