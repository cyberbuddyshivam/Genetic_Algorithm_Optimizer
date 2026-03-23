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


def plot_comparison(ga_history, gd_history, optimum=None):
    plt.figure(figsize=(8, 5))
    plt.plot(ga_history, linewidth=2, label="Genetic Algorithm", color="blue")
    plt.plot(gd_history, linewidth=2, label="Gradient Descent", color="green")

    if optimum is not None:
        plt.axhline(
            y=optimum,
            color="r",
            linestyle="--",
            linewidth=1.5,
            label=f"Optimum ({optimum})",
        )

    plt.xlabel("Iteration")
    plt.ylabel("Fitness Value")
    plt.title("GA vs Gradient Descent Convergence")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
