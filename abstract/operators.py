import abc

from abstract.population import OptimizationMode
from abstract.ga import GA
from typing import Set


class SelectionOperator(abc.ABC):

    def __init__(self, opt_modes: Set[OptimizationMode]):
        self._OptimumModes = opt_modes

    @property
    def modes(self) -> Set[OptimizationMode]:
        return self._OptimumModes

    @abc.abstractmethod
    def selection(self, ga: GA):
        pass


class CrossoverOperator(abc.ABC):
    @abc.abstractmethod
    def crossover(self, ga: GA):
        pass


class MutationOperator(abc.ABC):
    @abc.abstractmethod
    def mutation(self, ga: GA):
        pass
