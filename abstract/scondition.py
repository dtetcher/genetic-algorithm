import abc

from abstract.ga import GA


class StopCondition(abc.ABC):
    # def __init__(self):
    #     self.__ga: GA = GA()

    @abc.abstractmethod
    def stop(self) -> bool:
        pass

    def ga(self, genetic_algorithm: GA = None) -> GA:
        if genetic_algorithm is not None:
            self.__ga = genetic_algorithm
        else:
            return self.__ga
