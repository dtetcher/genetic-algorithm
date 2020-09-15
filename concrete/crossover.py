import random

from abstract.crossover import CrossoverOperator
from abstract.population import Chromosome
from abstract.ga import GA


class SingleCrossover(CrossoverOperator):

    def crossover(self, ga: GA):

        if random.uniform(0, 1) > ga.crossover_chance:
            return

        # Length of single chromosome
        unit_len = ga.population.unit_length

        pairs = ga.population.get_pairs()

        for f_id, s_id in pairs.items():

            first = ga.population.population[f_id]
            second = ga.population.population[s_id]

            # From which position crossover will be started.
            #
            xover_point = random.randint(0, unit_len)

            f, s = list(first.population_val), list(second.population_val)
            for b in range(xover_point, unit_len):

                # Swapping bits between two chromosomes
                #
                f[b], s[b] = s[b], f[b]

            # Setting values back
            #
            first.population_val = ''.join(f)
            second.population_val = ''.join(s)


class DoubleCrossover(CrossoverOperator):
    def crossover(self, ga: GA):
        pass


class MultiCrossover(CrossoverOperator):
    def crossover(self, ga: GA):
        pass
