from typing import List
import random
import abc

from abstract.fitness import FitnessFunction


class Chromosome(abc.ABC):
    """
    Class represents a single unit of genetic population.
    """

    def __init__(self, phenotype, pop, fs):
        self.__phenotype = phenotype
        self.__population_value = pop
        self.__fitness_score = fs

    def has_len(self, _len: int) -> bool:
        """
        Function to compare actual
        length to the length of specified unit.
        :param _len:
        :return: Bool
        """
        return _len == len(self.population_val)

    @property
    def phenotype(self):
        return self.__phenotype

    @phenotype.setter
    def phenotype(self, value):
        self._phenotype_setter(value)

    def _phenotype_setter(self, value):
        self.__phenotype = value

    @property
    def population_val(self):
        return self.__population_value

    @population_val.setter
    def population_val(self, value):
        self._pop_val_setter(value)

    def _pop_val_setter(self, value):
        self.__population_value = value

    @property
    def fitness_score(self):
        return self.__fitness_score

    @fitness_score.setter
    def fitness_score(self, value):
        self._fitness_score_setter(value)

    def _fitness_score_setter(self, value):
        self.__fitness_score = value


class IPopulation(abc.ABC):
    """
    This class used to organize population units.\n
    Class contains data which describes pop units as group\n
    Also validation, appliers functions can be written there
    """
    def __init__(self, input_set: List[Chromosome]):

        random_unit_length = len(random.choice(input_set)
                                 .population_val)

        if not all(unit.has_len(random_unit_length) for unit in input_set):
            raise ValueError("Population elements should be equal in their size.")

        self.__population = input_set
        self.__unit_length = random_unit_length

    @abc.abstractmethod
    def apply_fitness(self, func: FitnessFunction):
        """
        Method used to apply fitness function to whole population
        :param func:
        :return:
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

    @property
    def unit_length(self):
        """
        Getter for each population units' length
        :param value:
        :return:
        """
        return self.__unit_length

    @unit_length.setter
    def unit_length(self, value: int):
        """
        Method used to set population list
        """
        self.__unit_length = value

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        self.__population = value
