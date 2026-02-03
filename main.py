import tkinter as tk
from tkinter import ttk, messagebox

from ga import GeneticAlgorithm
from functions import FUNCTIONS
from plot import plot_fitness


class GAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Genetic Algorithm Optimizer")
        self.root.geometry("450x450")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="Genetic Algorithm Optimizer",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)

        # Function selection
        tk.Label(self.root, text="Select Function:").pack()
        self.function_var = tk.StringVar()
        self.function_dropdown = ttk.Combobox(
            self.root,
            textvariable=self.function_var,
            values=list(FUNCTIONS.keys()),
            state="readonly"
        )
        self.function_dropdown.pack(pady=5)
        self.function_dropdown.current(0)

        # Population size
        tk.Label(self.root, text="Population Size:").pack()
        self.population_entry = tk.Entry(self.root)
        self.population_entry.pack()
        self.population_entry.insert(0, "7")

        # Generations
        tk.Label(self.root, text="Number of Generations:").pack()
        self.generations_entry = tk.Entry(self.root)
        self.generations_entry.pack()
        self.generations_entry.insert(0, "50")

        # Mutation rate
        tk.Label(self.root, text="Mutation Rate (0–1):").pack()
        self.mutation_entry = tk.Entry(self.root)
        self.mutation_entry.pack()
        self.mutation_entry.insert(0, "0.1")

        # Run button
        tk.Button(
            self.root,
            text="Run Optimization",
            command=self.run_ga,
            bg="#4CAF50",
            fg="white",
            width=20
        ).pack(pady=15)

        # Output
        self.result_label = tk.Label(
            self.root,
            text="Result will appear here",
            font=("Arial", 11),
            fg="blue"
        )
        self.result_label.pack(pady=10)

    def run_ga(self):
        try:
            population = int(self.population_entry.get())
            generations = int(self.generations_entry.get())
            mutation_rate = float(self.mutation_entry.get())

            if not (0 <= mutation_rate <= 1):
                raise ValueError("Mutation rate must be between 0 and 1")

            function_name = self.function_var.get()
            function = FUNCTIONS[function_name]

            ga = GeneticAlgorithm(
                function=function,
                population_size=population,
                generations=generations,
                mutation_rate=mutation_rate
            )

            best_x, best_fx, history = ga.run()

            self.result_label.config(
                text=f"Best Solution: x = {best_x:.4f}\nBest Fitness: {best_fx:.6f}"
            )

            plot_fitness(history)

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = GAApp(root)
    root.mainloop()
