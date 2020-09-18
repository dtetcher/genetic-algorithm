from datetime import timedelta

from concrete.scondition import IterationCondition, AccuracyCondition, TimeOutCondition
from concrete.population import BinaryChromosome, BinaryPopulation
from concrete import crossover as xover
from concrete.ga import GeneticAlgorithm
from concrete.fitness import Linear7


def main():

    population_size = 4
    crossover_chance = 0.9
    mutation_chance = 0.1
    lower, upper = 0, 60

    chromosomes = [BinaryChromosome(lower, upper)
                   for _ in range(population_size)]

    population = BinaryPopulation(chromosomes)

    # Function used to determine chromosome potential
    fitness_function = Linear7()

    stop_conditions = [
        AccuracyCondition()
        # IterationCondition(iterations=1000),
        # TimeOutCondition(time=timedelta(seconds=4)),
    ]

    crossover_operator = xover.MultiCrossover()

    ga = GeneticAlgorithm(population,
                          fitness_function,
                          stop_conditions,
                          crossover_operator,
                          crossover_chance,
                          mutation_chance)

    ga.start()


if __name__ == '__main__':
    main()
