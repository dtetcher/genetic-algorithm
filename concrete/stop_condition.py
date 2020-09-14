from datetime import timedelta

from abstract.stop_condition import StopCondition
from abstract.ga import GA


class AccuracyCondition(StopCondition):

    def __init__(self, genetic_algorithm: GA,
                 accuracy: float):

        super().__init__(genetic_algorithm)
        self.__accuracy = accuracy

    def stop(self):
        return False


class IterationCondition(StopCondition):

    def __init__(self, iterations: int,
                 genetic_algorithm: GA = None):

        super().__init__(genetic_algorithm)
        self.__iterations = iterations

    def stop(self):
        return self._ga.generation_No == self.__iterations


class TimeOutCondition(StopCondition):

    def __init__(self, time: timedelta,
                 genetic_algorithm: GA = None):

        super().__init__(genetic_algorithm)
        self.__time = time

    def stop(self) -> bool:
        time_limit = self._ga.start_point + self.__time
        now = time_limit.now()
        return now > time_limit


class CrossoverRateCondition(StopCondition):

    def __init__(self, genetic_algorithm: GA = None):

        super().__init__(genetic_algorithm)

    def stop(self):
        return False


class MutationRateCondition(StopCondition):
    def __init__(self, genetic_algorithm: GA = None):
        super().__init__(genetic_algorithm)

    def stop(self):
        return False
