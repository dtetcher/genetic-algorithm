from typing import List

from abstract.population import Chromosome


class LimitList:
    def __init__(self, population_size: int):
        self.__units: List[Chromosome] = list()
        self.__population_size = population_size

    def append(self, obj: Chromosome) -> None:
        if len(self.__units) != self.__population_size:
            self.__units.append(obj)
        else:
            self.__units.sort(key=lambda c: c.fitness_score)
            self.__units[0] = obj

    def is_full(self):
        return len(self.__units) == self.__population_size

    def __repr__(self) -> List[Chromosome]:
        return self.__units

    def __getitem__(self, item):
        return self.__units[item]

    def __len__(self):
        return len(self.__units)
