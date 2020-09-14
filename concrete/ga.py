from typing import List
import random

from abstract.population import IPopulation, Chromosome
from abstract.stop_condition import StopCondition
from abstract.fitness import FitnessFunction
from abstract.ga import GA


class GeneticAlgorithm(GA):

    def __init__(self, population: IPopulation,
                 fitness_function: FitnessFunction,
                 stop_conditions: List[StopCondition],
                 crossover_chance: float,
                 mutation_chance: float):
        """
        :param population: Population of chromosomes
        :param fitness_function: Function to find fitness scores
        :param stop_conditions: List of conditions when GA stop executing
        :param crossover_chance: Chance of crossover
        :param mutation_chance: Chance of mutation
        """

        self._Population = population
        self._fitness_F = fitness_function
        self.__Pc = crossover_chance
        self.__Pm = mutation_chance
        self.__stop_cond_s = stop_conditions

        self._new_population = None
        self._generation_num = 0

    def start(self):
        pass

    def selection(self):
        """
        Implementation of roulette.\n
        Where selected would be chromosomes with highest\n
        fitness scores.\n\n
        There is also change that low-scored will survive.
        :return: Returns new population(List[Chromosome])
        """

        population_obj = self._Population

        # # Applying fitness function on our population
        # #
        # population_obj \
        #     .apply_fitness(self._fitness_F)
        
        # Sum of population fitness scores
        # 
        fitness_score_sum = sum([unit.fitness_score
                                 for unit in population_obj.population()])

        pop_size = len(population_obj.population())

        fittest_units = []

        # Dictionary for sectors with initial value
        #
        sectors = {-1: 0.}

        # Search for each sector size and append it to 'sectors' hash
        #
        for idx, e in enumerate(population_obj.population()):
            sectors[idx] = fitness_score_sum / e.fitness_score() + sectors[idx-1]

        # Loop to get fittest units for selection
        # Executes 'size of population' times
        #
        for _ in range(pop_size):
            # Random value used to select unit
            selector = random.uniform(0, 1)

            for idx in sectors.keys():

                # Loop will not iterate over last element
                # To prevent IndexError. However using 'next to current'
                # element to compute chance of selection unit allows us to
                # neglect this iteration
                #
                if idx+1 in sectors.keys():

                    # If selector in sector then add its id to list
                    # for creation of the next population
                    #
                    if sectors[idx] < selector <= sectors[idx+1]:
                        fittest_units.append(idx+1)

        # Replace old population
        self._new_population = [population_obj.population()[i] for i in fittest_units]

        return self._new_population

    def crossover(self, first: Chromosome, second: Chromosome):
        """
        Crosses two chromosomes.
        :param first: First chromosome
        :param second: Second chromosome
        :return: Crossed chromosomes
        """

        # Length of single chromosome
        unit_len = self._Population.unit_length()

        # Lists of first' and second's chromosome bits.
        #
        f, s = list(first.population()), list(second.population())

        # From which position crossover will be started.
        #
        wildcard = random.randint(0, unit_len)

        for b in range(wildcard, unit_len):

            # Swapping of bits between two chromosomes
            #
            f[b], s[b] = s[b], f[b]

        # Returns two string with affected chromosomes
        return ''.join(f), ''.join(s)

    def mutation(self, _population: List[Chromosome] = None):
        """
        Mutation applies on chromosome pool.
        :return:
        """

        # Inner function.
        # Goal to take bit and change it to opposite value
        #
        def swap(bit: str):
            if bit in ('1', '0'):
                return '0' if bool(bit) else '1'

        # Chromosome list
        population = self._new_population \
            if _population is None \
            else _population

        # Amount of bits that will be affected
        #
        bits_to_change = int(len(population) * self.__Pm)

        # Two dimensional list.
        # Parent list contains lists with splitted
        # chromosome population value
        #
        mutated = [list(p) for p in population]

        # Length of single chromosome
        unit_length = self._Population.unit_length()

        # Size of all population in bits
        #
        pops_size = unit_length * len(mutated)

        # Process of mutation
        for _ in range(bits_to_change):
            # Position value for single dimension array
            pos = random.randint(0, pops_size)

            # Position values for double dimension array.
            # 0 element - position in outer scope.
            # 1 element - in inner scope.
            #
            positions = str(pos / unit_length).split('.')
            outer, inner = int(positions[0]), int(positions[1]) - 1

            # Process of swapping bits.
            mutated[outer][inner] = swap(mutated[outer][inner])

        # Replaces old population values to newly mutated.
        #
        [p.population(''.join(m)) for p in population for m in mutated]

    @property
    def generation_No(self):
        return self._generation_num
