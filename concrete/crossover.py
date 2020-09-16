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

            first: Chromosome = ga.population.population[f_id]
            second: Chromosome = ga.population.population[s_id]

            # From which position crossover will be started.
            #
            xover_point = random.randint(0, unit_len)

            f, s = list(first.population_value), list(second.population_value)

            for b in range(xover_point, unit_len):

                # Swapping bits between two chromosomes
                #
                f[b], s[b] = s[b], f[b]

            # Setting values back
            #
            first.population_value = ''.join(f)
            second.population_value = ''.join(s)


class DoubleCrossover(CrossoverOperator):
    def crossover(self, ga: GA):
        if random.uniform(0, 1) > ga.crossover_chance:
            return

        unit_len = ga.population.unit_length

        pairs = ga.population.get_pairs()

        for f_id, s_id in pairs.items():

            first: Chromosome = ga.population.population[f_id]
            second: Chromosome = ga.population.population[s_id]

            xover_point_1 = random.randint(0, int(unit_len / 2))
            xover_point_2 = random.randint(xover_point_1, unit_len)

            f, s = list(first.population_value), list(second.population_value)

            for b in range(xover_point_1, xover_point_2):
                f[b], s[b] = s[b], f[b]

            first.population_value = ''.join(f)
            second.population_value = ''.join(s)


class MultiCrossover(CrossoverOperator):
    def crossover(self, ga: GA):
        if random.uniform(0, 1) > ga.crossover_chance:
            return

        unit_len = ga.population.unit_length

        pairs = ga.population.get_pairs()

        for f_id, s_id in pairs.items():

            first: Chromosome = ga.population.population[f_id]
            second: Chromosome = ga.population.population[s_id]

            f, s = list(first.population_value), list(second.population_value)

            bits_ids = list(range(0, unit_len))
            half_len = int(unit_len / 2)

            bits_to_change = set(random.choices(bits_ids, k=half_len))

            for b in bits_to_change:
                f[b], s[b] = s[b], f[b]

            first.population_value = ''.join(f)
            second.population_value = ''.join(s)
