from datetime import timedelta

from concrete.scondition import *
from concrete.population import *
from concrete.selection import *
from concrete.crossover import *
from concrete.mutation import *
from concrete.fitness import *
from concrete.ga import *


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
        AccuracyCondition(),
        IterationCondition(iterations=10_000),
        TimeOutCondition(time=timedelta(minutes=1)),
    ]

    selection_operator = TournamentSelection()
    crossover_operator = MultiCrossover()
    mutation_operator = BitFlipMutation()

    ga = GeneticAlgorithm(population=population,
                          fitness_function=fitness_function,
                          stop_conditions=stop_conditions,
                          selection_op=selection_operator,
                          crossover_op=crossover_operator,
                          mutation_op=mutation_operator,
                          crossover_chance=crossover_chance,
                          mutation_chance=mutation_chance)

    ga.start(OptimizationMode.Minimization)


if __name__ == '__main__':
    main()
