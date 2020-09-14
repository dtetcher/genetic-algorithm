from datetime import datetime
from typing import List
import abc

from abstract.population import Chromosome


class GA(abc.ABC):

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def _selection(self):
        pass

    @abc.abstractmethod
    def _crossover(self, first: Chromosome, second: Chromosome):
        pass

    @abc.abstractmethod
    def _mutation(self, _population: List[Chromosome] = None):
        pass

    @abc.abstractmethod
    @property
    def generation_No(self):
        return

    @abc.abstractmethod
    @property
    def start_point(self) -> datetime:
        pass
