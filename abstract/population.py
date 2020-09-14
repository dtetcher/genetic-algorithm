from typing import List
import abc

from abstract.fitness import FitnessFunction


class Chromosome(abc.ABC):
    """
    Class represents a single unit of genetic population.
    """

    @abc.abstractmethod
    def has_len(self, _len: int) -> bool:
        """
        Function to compare actual
        length to the length of specified unit.
        :param _len:
        :return: Bool
        """
        pass

    @abc.abstractmethod
    def phenotype(self, value=None):
        """
        Phenotype getter and setter.\n
        Normal representation of chromosome.
        :return:
        """
        return

    @abc.abstractmethod
    def population_val(self, value=None):
        """
        Population getter and setter.\n
        Binary representation of chromosome.
        :param value:
        :return:
        """
        pass

    @abc.abstractmethod
    def fitness_score(self, value=None):
        """
        Fitness score getter and setter.
        :param value:
        :return:
        """
        return


class IPopulation(abc.ABC):
    """
    This class used to organize population units.\n
    Class contains data which describes pop units as group\n
    Also validation, appliers functions can be written there
    """

    @abc.abstractmethod
    def apply_fitness(self, func: FitnessFunction):
        """
        Method used to apply fitness function to whole population
        :param func:
        :return:
        """
        pass

    @abc.abstractmethod
    def unit_length(self, value=None):
        """
        Getter and setter for each population units' length
        :param value:
        :return:
        """
        pass

    @abc.abstractmethod
    def population(self, value: List[Chromosome] = None) \
            -> List[Chromosome]:
        """
        Method used to set and retrieve population list
        """
        pass

    @abc.abstractmethod
    def get_fittest(self, count: int) -> List[Chromosome]:
        """
        Function returns elements which has the highest fitness score
        """
        pass

    @abc.abstractmethod
    def get_pairs(self) -> dict:
        """
        Randomly pairs population units.\n
        :return: Dictionary - key is first unit's id,
                 value is second's.
        """
        pass
