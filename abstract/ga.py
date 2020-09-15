from datetime import datetime
from typing import List
import abc

from abstract.population import IPopulation
from abstract.population import Chromosome


class GA(abc.ABC):

    def __init__(self, population: IPopulation,
                 crossover_chance: float,
                 mutation_chance: float):

        self.__population = population
        self.__start_point: datetime = datetime.min
        self.__generation_num: int = 0
        self.__Pc = crossover_chance
        self.__Pm = mutation_chance

    # # #
    # METHODS
    # # #

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def _selection(self):
        pass

    @abc.abstractmethod
    def _crossover(self):
        pass

    @abc.abstractmethod
    def _mutation(self, _population: List[Chromosome] = None):
        pass

    # # #
    # PROPERTIES
    # # #

    @property
    def population(self) -> IPopulation:
        return self.__population

    @property
    def start_point(self) -> datetime:
        return self.__start_point

    @start_point.setter
    def start_point(self, value: datetime):
        self.__start_point = value

    @property
    def generation_no(self) -> int:
        return self.__generation_num

    @generation_no.setter
    def generation_no(self, value: int):
        self.__generation_num = value

    @property
    def crossover_chance(self):
        return self.__Pc

    @property
    def mutation_chance(self):
        return self.__Pm

