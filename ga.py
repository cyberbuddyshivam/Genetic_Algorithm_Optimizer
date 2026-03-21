import random
from typing import Callable, List, Optional


class GeneticAlgorithm:
    def __init__(
        self,
        function: Callable[[List[float]], float],
        dimensions: int = 2,
        population_size: int = 50,
        generations: int = 100,
        mutation_rate: float = 0.1,
        bounds: tuple[float, float] = (-5.12, 5.12),
        seed: Optional[int] = 15,
    ):
        self.function = function
        self.dimensions = dimensions
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.lower_bound, self.upper_bound = bounds
        self.seed = seed

        self.population = []
        self.best_solution = None
        self.best_fitness = float("inf")
        self.fitness_history = []

    def initialize_population(self):
        self.population = [
            [
                random.uniform(self.lower_bound, self.upper_bound)
                for _ in range(self.dimensions)
            ]
            for _ in range(self.population_size)
        ]

    def fitness(self, individual):
        return self.function(individual)

    def selection(self):
        tournament = random.sample(self.population, 3)
        return min(tournament, key=self.fitness)

    def crossover(self, parent1, parent2):
        child = []
        for i in range(self.dimensions):
            alpha = random.random()
            gene = alpha * parent1[i] + (1 - alpha) * parent2[i]
            child.append(gene)
        return child

    def mutate(self, individual):
        for i in range(self.dimensions):
            if random.random() < self.mutation_rate:
                individual[i] += random.uniform(-1, 1)
                if individual[i] < self.lower_bound:
                    individual[i] = self.lower_bound
                elif individual[i] > self.upper_bound:
                    individual[i] = self.upper_bound
        return individual

    def run(self) -> tuple[List[float], float, List[float]]:
        if self.seed is not None:
            random.seed(self.seed)
        self.initialize_population()

        for generation in range(self.generations):
            best_in_generation = min(self.population, key=self.fitness)
            best_fitness = self.fitness(best_in_generation)

            if best_fitness < self.best_fitness:
                self.best_fitness = best_fitness
                self.best_solution = best_in_generation.copy()

            self.fitness_history.append(self.best_fitness)

            new_population = [best_in_generation.copy()]

            for _ in range(self.population_size - 1):
                parent1 = self.selection()
                parent2 = self.selection()

                child = self.crossover(parent1, parent2)
                child = self.mutate(child)

                new_population.append(child)

            self.population = new_population

        return self.best_solution, self.best_fitness, self.fitness_history
