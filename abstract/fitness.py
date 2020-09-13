import abc


class FitnessFunction(abc.ABC):
    @abc.abstractmethod
    def fitness(self, x: int):
        pass
