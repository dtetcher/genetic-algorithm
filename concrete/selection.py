from typing import List
import random

from abstract.population import OptimizationMode, Chromosome
from abstract.operators import SelectionOperator
from abstract.ga import GA


class RouletteWheelSelection(SelectionOperator):

    def __init__(self):
        optimization_modes = {OptimizationMode.Maximization, }

        super().__init__(optimization_modes)

    def selection(self, ga: GA):
        """
                Implementation of roulette.\n
                Where selected would be chromosomes with highest\n
                fitness scores.\n\n
                There is also chance that low-scored will survive.
                :return: Returns new population(List[Chromosome])
                """

        population_obj = ga.population

        fitness_score_sum = sum([unit.fitness_score
                                 for unit in population_obj.population])

        pop_size = len(population_obj.population)
        fittest_units = []

        sectors = {-1: 0.}

        for idx, e in enumerate(population_obj.population):
            sectors[idx] = round(e.fitness_score / fitness_score_sum + sectors.get(idx - 1), 3)

        for _ in range(pop_size):

            selector = random.uniform(0, 1)

            for idx in sectors.keys():

                if idx + 1 in sectors.keys():

                    if sectors[idx] < selector <= sectors[idx + 1]:
                        fittest_units.append(idx + 1)

        population_obj.population = [population_obj.population[i] for i in fittest_units]

        return population_obj.population


class RankSelection(SelectionOperator):

    def __init__(self):
        optimization_modes = {OptimizationMode.Maximization,
                              OptimizationMode.Minimization}

        super().__init__(optimization_modes)

    def selection(self, ga: GA):
        pass


class TournamentSelection(SelectionOperator):

    def __init__(self):
        optimization_modes = {OptimizationMode.Maximization,
                              OptimizationMode.Minimization}

        super().__init__(optimization_modes)

    def selection(self, ga: GA):

        # 1. Take random IDs of population's units
        #    in size of half population.
        # 2. Then from population units with such id's
        #    select one with best fitness score
        #
        # Steps repeated till new generation size is reached

        population = ga.population.population
        pop_size = len(population)
        half_size = int(pop_size / 2)

        new_gen = list()

        while len(new_gen) != pop_size:

            ids = set(random.choices(range(0, pop_size), k=half_size))

            tour_winners: List[Chromosome] = [population[i] for i in ids]
            winner = sorted(tour_winners, key=lambda x: x.fitness_score)[-1]

            new_gen.append(winner)

        ga.population.population = new_gen
