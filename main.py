from datetime import timedelta

from concrete.scondition import TimeOutCondition, IterationCondition
from concrete.population import BinaryChromosome, BinaryPopulation
from concrete.crossover import SingleCrossover
from concrete.ga import GeneticAlgorithm
from concrete.fitness import Linear7


def main():

    population_size = 6
    crossover_chance = 0.7
    mutation_chance = 0.2
    lower, upper = 0, 60

    chromosomes = [BinaryChromosome(lower, upper)
                   for _ in range(population_size)]

    population = BinaryPopulation(chromosomes)

    fitness_function = Linear7()

    stop_conditions = [
        IterationCondition(iterations=10),
        # TimeOutCondition(time=timedelta(seconds=4))
    ]

    crossover_operator = SingleCrossover()

    ga = GeneticAlgorithm(population,
                          fitness_function,
                          stop_conditions,
                          crossover_operator,
                          crossover_chance,
                          mutation_chance)

    ga.start()


if __name__ == '__main__':
    main()
