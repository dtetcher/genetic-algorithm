import random

from abstract.operators import MutationOperator
from abstract.ga import GA


class BitFlipMutation(MutationOperator):
    def mutation(self, ga: GA):
        """
                Mutation applies on chromosome pool.
                :return:
                """

        def flip(bit: str):
            if bit in ('1', '0'):
                return '0' if int(bit) else '1'

        population = ga.population.population

        bits_to_change = int(len(population) * ga.mutation_chance)

        mutated = [list(p.population_value) for p in population]

        unit_length = ga.population.unit_length

        pops_size = unit_length * len(mutated)

        for _ in range(bits_to_change):
            pos = random.randint(0, pops_size - 1)

            outer, inner = pos // unit_length, pos % unit_length

            mutated[outer][inner] = flip(str(mutated[outer][inner]))

        for idx, chromosome in enumerate(population):
            chromosome.population_value = ''.join(mutated[idx])


class SwapBitMutation(MutationOperator):
    def mutation(self, ga: GA):

        population = ga.population.population
        bits_to_change = int(len(population) * ga.mutation_chance)

        mutated = [list(p.population_value) for p in population]
        m = mutated

        unit_length = ga.population.unit_length
        pops_size = unit_length * len(mutated)

        for _ in range(bits_to_change):
            pos1 = random.randint(0, pops_size - 1)
            pos2 = random.randint(0, pops_size - 1)

            out1, in1 = pos1 // unit_length, pos1 % unit_length
            out2, in2 = pos2 // unit_length, pos2 % unit_length

            m[out1][in1], m[out2][in2] = m[out2][in2], m[out1][in1]

        for idx, chromosome in enumerate(population):
            chromosome.population_value = ''.join(mutated[idx])


class InverseMutation(MutationOperator):
    def mutation(self, ga: GA):

        population = ga.population.population
        bits_to_change = int(len(population) * ga.mutation_chance)

        mutated = [list(p.population_value) for p in population]
        m = mutated

        unit_length = ga.population.unit_length
        pops_size = unit_length * len(mutated)

        for _ in range(bits_to_change):
            pos1 = random.randint(0, pops_size - 1)
            pos2 = pos1 + 1

            out1, in1 = pos1 // unit_length, pos1 % unit_length
            out2, in2 = pos2 // unit_length, pos2 % unit_length

            m[out1][in1], m[out2][in2] = m[out2][in2], m[out1][in1]

        for idx, chromosome in enumerate(population):
            chromosome.population_value = ''.join(mutated[idx])

