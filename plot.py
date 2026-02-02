import matplotlib.pyplot as plt

def plot_fitness(fitness_history):
    """
    Plots Fitness vs Generation graph
    """
    plt.figure(figsize=(8, 5))
    plt.plot(fitness_history, linewidth=2)
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness Value")
    plt.title("Genetic Algorithm Convergence")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
