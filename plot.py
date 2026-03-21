import matplotlib.pyplot as plt


def plot_fitness(fitness_history, optimum=None):
    plt.figure(figsize=(8, 5))
    plt.plot(fitness_history, linewidth=2, label="Best Fitness")

    if optimum is not None:
        plt.axhline(
            y=optimum,
            color="r",
            linestyle="--",
            linewidth=1.5,
            label=f"Optimum ({optimum})",
        )

    plt.xlabel("Generation")
    plt.ylabel("Best Fitness Value")
    plt.title("Genetic Algorithm Convergence")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
