from datetime import timedelta

from abstract.scondition import StopCondition


class AccuracyCondition(StopCondition):

    def __init__(self):
        super().__init__()

    def stop(self):
        _list = self.ga().accuracy_list

        is_full = _list.is_full()
        not_empty = len(_list) != 0
        fitness_equal = all([e.fitness_score == _list[0].fitness_score
                            for e in _list])

        # Stop condition achieved only when
        # the following 3 conditions return True
        #
        return fitness_equal and not_empty and is_full


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
