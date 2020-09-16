from datetime import datetime
from typing import List, Dict
import random

from abstract.population import IPopulation, Chromosome
from abstract.crossover import CrossoverOperator
from concrete.crossover import SingleCrossover
from abstract.scondition import StopCondition
from abstract.fitness import FitnessFunction
from abstract.ga import GA


class GeneticAlgorithm(GA):

    def __init__(self, population: IPopulation,
                 fitness_function: FitnessFunction,
                 stop_conditions: List[StopCondition] = None,
                 crossover_op: CrossoverOperator = SingleCrossover,
                 crossover_chance: float = 0.8,
                 mutation_chance: float = 0.2):
        """
        :param population: Population of chromosomes
        :param fitness_function: Function to find fitness scores
        :param stop_conditions: List of conditions when GA stop executing (Optional)
        :param crossover_op: Crossover method (Single by default)
        :param crossover_chance: Chance of crossover
        :param mutation_chance: Chance of mutation
        """
        super().__init__(population, crossover_chance, mutation_chance)

        self._Population = population
        self._fitness_F = fitness_function
        self.__stop_cond_s = stop_conditions
        self.__crossover_func = crossover_op.crossover

        # Setting up GA instance for each StopCondition class
        [sc.ga(self) for sc in self.__stop_cond_s]

    def start(self):

        print(f"{'*'*30}\nInit statistics\n{'*'*30}\n\n", self.statistics())
        self.start_point = datetime.now()

        while True:
            # Applying fitness function on our population
            #
            self._Population \
                .apply_fitness(self._fitness_F)

            # Checking stop conditions
            #
            if self.__stop_cond_s is not None \
                    and any([sc.stop() for sc in self.__stop_cond_s]):
                print(f"{'*'*30}\nFinal statistics\n{'*'*30}\n\n")
                print(self.statistics(end_stat=True))
                break

            self._selection()

            # Crossover process
            #
            self._crossover()

            # Mutation process
            #
            self._mutation()

            self.generation_no += 1

    def _selection(self):
        """
        Implementation of roulette.\n
        Where selected would be chromosomes with highest\n
        fitness scores.\n\n
        There is also chance that low-scored will survive.
        :return: Returns new population(List[Chromosome])
        """

        population_obj = self._Population

        # Sum of population fitness scores
        #
        fitness_score_sum = sum([unit.fitness_score
                                 for unit in population_obj.population])

        pop_size = len(population_obj.population)
        fittest_units = []

        # Dictionary for sectors with initial value
        #
        sectors = {-1: 0.}

        # Search for each sector size and append it to 'sectors' hash
        #
        for idx, e in enumerate(population_obj.population):
            sectors[idx] = e.fitness_score / fitness_score_sum + sectors.get(idx-1)

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
        population_obj.population = [population_obj.population[i] for i in fittest_units]

        return population_obj.population

    def _crossover(self):
        """
        Crosses two chromosomes.
        :param first: First chromosome
        :param second: Second chromosome
        :return: Crossed chromosomes
        """
        self.__crossover_func(self)

    def _mutation(self, _population: List[Chromosome] = None):
        """
        Mutation applies on chromosome pool.
        :return:
        """

        # Inner function.
        # Goal to take bit and change it to opposite value
        #
        def swap(bit: str):
            if bit in ('1', '0'):
                return '0' if int(bit) else '1'

        # Chromosome list
        population = self._Population.population \
            if _population is None \
            else _population

        # Amount of bits that will be affected
        #
        bits_to_change = int(len(population) * self.mutation_chance)

        # Two dimensional list.
        # Parent list contains lists with splitted
        # chromosome population value
        #
        mutated = [list(p.population_value) for p in population]

        # Length of single chromosome
        unit_length = self._Population.unit_length

        # Size of all population in bits
        #
        pops_size = unit_length * len(mutated)

        # Process of mutation
        for _ in range(bits_to_change):

            # Position value for single dimension array
            pos = random.randint(0, pops_size-1)

            # Position values for double dimension array.
            # 0 element - position in outer scope.
            # 1 element - in inner scope.
            #
            outer, inner = pos // unit_length, pos % unit_length

            # Process of swapping bits.
            mutated[outer][inner] = swap(str(mutated[outer][inner]))

        # Replaces old population values to newly mutated.
        #
        for idx, chromosome in enumerate(population):
            chromosome.population_value = ''.join(mutated[idx])

    def statistics(self, population: List[Chromosome] = None, end_stat: bool = False):

        def run_time(time):
            return f"{time.seconds} s" \
                if time.seconds != 0 \
                else f"{time.microseconds} ms"

        p = self._Population.population \
            if population is None \
            else population

        __ = str()
        fitness_avg = sum([c.fitness_score for c in p]) / len(p)

        for i, ch in enumerate(p):
            __ += f"\nChromosome #{i+1}:\n\n" \
                  f"Phenotype - {ch.phenotype}\n" \
                  f"Population value - {ch.population_value}\n" \
                  f"Fitness score - {ch.fitness_score}\n" \
                  f"---------------\n"

        if end_stat:
            __ += f"---------------\n" \
                  f"Fitness average = {round(fitness_avg, 2)}\n" \
                  f"Runtime: {run_time(datetime.now() - self.start_point)}\n" \
                  f"Iterations: {self.generation_no}\n"

        return __
