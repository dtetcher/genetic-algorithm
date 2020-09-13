import abc
from abstract.fitness import FitnessFunction
from typing import List


class IPopulationUnit(abc.ABC):

    #
    # Function to compare actual
    # length of unit with specified
    #

    @abc.abstractmethod
    def has_len(self, _len: int) -> bool:
        pass

    #
    # Phenotype getter and setter
    #

    @abc.abstractmethod
    @property
    def phenotype(self):
        return

    @abc.abstractmethod
    @phenotype.setter
    def phenotype(self, value):
        pass

    #
    # Population getter and setter
    #

    @abc.abstractmethod
    @property
    def population(self):
        return

    @abc.abstractmethod
    @population.setter
    def population(self, value):
        pass

    #
    # Fitness getter and setter
    #

    @abc.abstractmethod
    @property
    def fitness_score(self):
        return

    @abc.abstractmethod
    @fitness_score.setter
    def fitness_score(self, value):
        pass


class IPopulation(abc.ABC):

    @abc.abstractmethod
    def apply_fitness(self, func: FitnessFunction):
        pass

    @abc.abstractmethod
    def unit_length(self, value=None):
        pass

    @abc.abstractmethod
    @property
    def population(self) -> List[IPopulationUnit]:
        pass

    @abc.abstractmethod
    def get_fittest(self, count: int) -> List[IPopulationUnit]:
        pass
