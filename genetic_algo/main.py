'''
Simple GA that finds a quick path
'''

import string
import random

STRING = 'This is a veeeeery long string!!'
ASCII_LIB = string.printable
N = len(STRING)


class Population:

    def __init__(
        self, population_size=2000, top_fittest=0.5, mutation_rate=0.009
        ):
        self.generation = 0
        self.population_size = population_size
        self.mating_pool_size = int(population_size*top_fittest)
        self.mutation_rate = mutation_rate
        self.population = [
            self.generate_random_genome() for _ in range(self.population_size)
            ]
        self.generate_population_fitness()
        self.parents = [' '*N]*self.population_size

    @staticmethod
    def generate_random_genome():
        return ''.join(random.choice(ASCII_LIB) for i in range(N))

    @staticmethod
    def cross_over(parent1, parent2):
        random_split = random.randint(0, N)
        return parent1[:random_split] + parent2[random_split:]

    def fitness(self, genome_correct, population_genome):
        assert len(genome_correct) == len(population_genome)
        return sum([
            1 if i[0] == i[1] else 0
            for i in zip(genome_correct, population_genome)
            ])/self.population_size

    def generate_population_fitness(self):
        self.fitness_scores = [
            self.fitness(STRING, genome) for genome in self.population
            ]

    def get_average_fitness(self):
        return sum(self.fitness_scores)/self.population_size

    def select_fittest(self):
        individual_fitness = [*zip(self.population, self.fitness_scores)]
        sorted_by_fitness = sorted(
            individual_fitness, key=lambda tup: tup[1], reverse=True
            )

        self.parents = [
            i[0] for i in sorted_by_fitness[:self.mating_pool_size]
            ]

    def mutate_popoulation(self):
        mutation_indices = random.sample(
            range(self.population_size),
            int(self.mutation_rate*self.population_size)
            )

        for i in mutation_indices:
            idx = random.randint(0, N)
            (
                self.population[i][:idx].replace(
                    self.population[i][idx-1],
                    random.choice(ASCII_LIB)
                    ) + self.population[i][idx:]
            )

    def generate_next_population(self):
        for i in range(self.population_size):
            parent1 = random.choice(self.parents)
            parent2 = random.choice(self.parents)
            self.population[i] = self.cross_over(parent1, parent2)
        self.mutate_popoulation()
        self.generation += 1


if __name__ == "__main__":
    population = Population()
    while True:
        print(f'Generation: {population.generation}')
        if STRING in population.population:
            print('String found')
            break
        print(population.population[4])
        population.select_fittest()
        population.generate_next_population()
        population.generate_population_fitness()
