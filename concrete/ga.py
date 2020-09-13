from abstract.population import IPopulation
from abstract.fitness import FitnessFunction
import random


class GeneticAlgorithm:

    def __init__(self, population: IPopulation,
                 fitness_function: FitnessFunction):

        self.init_population = population
        self.fitness_F = fitness_function

    def selection(self, population: IPopulation = None):

        population_obj = self.init_population.population \
            if population is None\
            else population

        # Applying fitness function on our population
        #
        population_obj \
            .apply_fitness(self.fitness_F)
        
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
            sectors[idx] = fitness_score_sum / e.fitness_score + sectors[idx-1]

        # Loop to get fittest units for selection       1i 0 21     2i 21 67    3i 67 9     4i 9 3
        # Executes 'size of population' times
        #
        for _ in range(pop_size):
            selector = random.uniform(0, 1)

            for k, v in sectors.items():
                if k+1 in sectors.keys():
                    if sectors[k] < selector <= sectors[k+1]:
                        fittest_units.append(sectors.get(k+1))

        return [population_obj.population[i] for i in fittest_units]

    def crossover(self):
        pass

    def mutation(self):
        pass
