import abc

from abstract.ga import GA


class StopCondition(abc.ABC):
    def __init__(self, genetic_algorithm: GA):
        self.__ga = genetic_algorithm

    @abc.abstractmethod
    def stop(self) -> bool:
        pass

    @property
    def _ga(self) -> GA:
        return self.__ga
