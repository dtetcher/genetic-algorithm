from datetime import timedelta

from concrete.stop_condition import IterationCondition, TimeOutCondition
from concrete.population import BinaryChromosome, BinaryPopulation
from concrete.ga import GeneticAlgorithm
from concrete.fitness import Linear7


def main():
    population_size = 6
    crossover_chance = 0.7
    mutation_chance = 0.2
    lower, upper = 10, 30

    chromosomes = [BinaryChromosome(lower, upper)
                   for _ in range(population_size)]

    population = BinaryPopulation(chromosomes)

    fitness_function = Linear7()

    stop_conditions = [
        IterationCondition(iterations=100),
        TimeOutCondition(time=timedelta.min(5))
    ]

    ga = GeneticAlgorithm(population,
                          fitness_function,
                          stop_conditions,
                          crossover_chance,
                          mutation_chance)

    ga.start()


if __name__ == '__main__':
    main()
