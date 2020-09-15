from datetime import timedelta

from abstract.scondition import StopCondition


class AccuracyCondition(StopCondition):

    def __init__(self, accuracy: float):

        super().__init__()
        self.__accuracy = accuracy

    def stop(self):
        return False


class IterationCondition(StopCondition):

    def __init__(self, iterations: int):

        super().__init__()
        self.__iterations = iterations

    def stop(self):
        return self.ga().generation_no == self.__iterations


class TimeOutCondition(StopCondition):

    def __init__(self, time: timedelta):

        super().__init__()
        self.__time = time

    def stop(self) -> bool:
        time_limit = self.ga().start_point + self.__time
        now = time_limit.now()
        return now > time_limit


class CrossoverRateCondition(StopCondition):
    def __init__(self):
        super().__init__()

    def stop(self):
        return False


class MutationRateCondition(StopCondition):
    def __init__(self):
        super().__init__()

    def stop(self):
        return False
