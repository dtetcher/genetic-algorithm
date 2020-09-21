from datetime import datetime
from typing import List
import random

from abstract.operators import *
from concrete.crossover import SingleCrossover
from abstract.scondition import StopCondition
from concrete.mutation import BitFlipMutation
from abstract.population import *
from .list import LimitList
from abstract.ga import GA


class GeneticAlgorithm(GA):
    def __init__(self, population: Population,
                 fitness_function: FitnessFunction,
                 selection_op: SelectionOperator,
                 crossover_op: CrossoverOperator = SingleCrossover,
                 mutation_op: MutationOperator = BitFlipMutation,
                 stop_conditions: List[StopCondition] = None,
                 crossover_chance: float = 0.8,
                 mutation_chance: float = 0.2,
                 ):
        """
        :param population: Population of chromosomes
        :param fitness_function: Function to find fitness scores
        :param stop_conditions: List of conditions when GA stop executing (Optional)
        :param crossover_op: Crossover method (Single by default)
        :param crossover_chance: Chance of crossover
        :param mutation_chance: Chance of mutation
        """

        self._Population = population
        self._fitness_F = fitness_function
        self.__stop_cond_s = stop_conditions

        self.__selection_op = selection_op
        self.__crossover_op = crossover_op
        self.__mutation_op = mutation_op

        self.__accuracy_list = LimitList(len(self._Population.population))

        # Setting up GA instance for each StopCondition class
        [sc.ga(self) for sc in self.__stop_cond_s]

        super().__init__(population, self.__accuracy_list, crossover_chance, mutation_chance)

    def start(self, mode: OptimizationMode):

        print(f"{'*'*30}\nInit statistics\n{'*'*30}\n\n", self.statistics())
        self.start_point = datetime.now()

        while True:
            # Applying fitness function on our population
            #
            self._Population \
                .apply_fitness(self._fitness_F, mode)

            # Checking stop conditions
            #
            if self.__stop_cond_s is not None \
                    and any([sc.stop() for sc in self.__stop_cond_s]):

                print(f"{'*'*30}\nFinal statistics\n{'*'*30}\n\n")
                print(self.statistics(end_stat=True))
                break

            self._selection(mode)

            # Crossover process
            #
            self._crossover()

            # Mutation process
            #
            self._mutation()

            # Increment generation
            self.generation_no += 1

            # Append best chromosome to accuracy list
            self.__accuracy_list \
                .append(
                    self.population.get_fittest(1)[0])

    def _selection(self, mode: OptimizationMode):
        """
        Creates a new generation
        :param mode:
        :return:
        """
        if mode in self.__selection_op.modes:
            return self.__selection_op.selection(self)
        else:
            raise ValueError(f"Selection operator {self.__selection_op} does not support {mode} mode.")

    def _crossover(self):
        """
        Crosses two chromosomes.
        :param first: First chromosome
        :param second: Second chromosome
        :return: Crossed chromosomes
        """
        self.__crossover_op.crossover(self)

    def _mutation(self):
        """
        Apply mutation on chromosomes
        :return:
        """
        self.__mutation_op.mutation(self)

    def statistics(self, population: List[Chromosome] = None, end_stat: bool = False):

        def run_time(time):
            return f"{time.seconds}.{time.microseconds} seconds"

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
