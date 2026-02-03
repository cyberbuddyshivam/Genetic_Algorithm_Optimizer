import random

class GeneticAlgorithm:
    def __init__(
        self,
        function,
        population_size=20,
        generations=50,
        mutation_rate=0.1,
        lower_bound=-10,
        upper_bound=10
    ):
        self.function = function
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        self.population = []
        self.best_solution = None
        self.best_fitness = float("inf")
        self.fitness_history = []

    # Step 1: Initialize population
    def initialize_population(self):
        self.population = [
            random.uniform(self.lower_bound, self.upper_bound)
            for _ in range(self.population_size)
        ]

    # Step 2: Fitness evaluation
    def fitness(self, x):
        return self.function(x)

    # Step 3: Selection (Tournament Selection)
    def selection(self):
        tournament = random.sample(self.population, 3)
        tournament.sort(key=self.fitness)
        return tournament[0]

    # Step 4: Crossover
    def crossover(self, parent1, parent2):
        alpha = random.random()
        child = alpha * parent1 + (1 - alpha) * parent2
        return child

    # Step 5: Mutation
    def mutate(self, x):
        if random.random() < self.mutation_rate:
            x += random.uniform(-1, 1)
        # Clip x to stay within bounds
        if x < self.lower_bound:
            x = self.lower_bound
        elif x > self.upper_bound:
            x = self.upper_bound
        return x

    # Step 6: Run Genetic Algorithm
    def run(self):
        random.seed(15)
        self.initialize_population()

        for generation in range(self.generations):
            # Track best solution
            best_in_generation = min(self.population, key=self.fitness)
            best_fitness = self.fitness(best_in_generation)

            if best_fitness < self.best_fitness:
                self.best_fitness = best_fitness
                self.best_solution = best_in_generation

            self.fitness_history.append(self.best_fitness)

            # Elitism: preserve best individual from last generation
            new_population = [best_in_generation]
            
            for _ in range(self.population_size - 1):
                parent1 = self.selection()
                parent2 = self.selection()

                child = self.crossover(parent1, parent2)
                child = self.mutate(child)

                new_population.append(child)

            self.population = new_population

        return self.best_solution, self.best_fitness, self.fitness_history
