from abstract.stop_condition import StopCondition
from abstract.ga import GA


class AccuracyCondition(StopCondition):

    def __init__(self, genetic_algorithm: GA,
                 accuracy: float):

        super().__init__(genetic_algorithm)
        self.__accuracy = accuracy

    def stop(self):
        pass


class IterationCondition(StopCondition):

    def __init__(self, genetic_algorithm: GA,
                 iterations: int):

        super().__init__(genetic_algorithm)
        self.iterations = iterations

    def stop(self):
        return self._ga.generation_No == self.iterations


class CrossoverRateCondition(StopCondition):

    def __init__(self, genetic_algorithm: GA):

        super().__init__(genetic_algorithm)

    def stop(self):
        pass


class MutationRateCondition(StopCondition):
    def __init__(self, genetic_algorithm: GA):
        super().__init__(genetic_algorithm)

    def stop(self):
        pass
