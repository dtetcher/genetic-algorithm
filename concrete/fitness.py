from abstract.fitness import FitnessFunction


class Linear7(FitnessFunction):
    def fitness(self, x: int):
        return (x+3) ** 3 - 7
