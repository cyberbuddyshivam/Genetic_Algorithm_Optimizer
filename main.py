import random
import tkinter as tk
from tkinter import ttk, messagebox

from ga import GeneticAlgorithm
from functions import FUNCTION_INFO, gradient_descent
from plot import plot_fitness, plot_comparison


def is_1d_function(info):
    return info["min_dimensions"] == 1 and info["max_dimensions"] == 1


class GAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Genetic Algorithm Optimizer")
        self.root.geometry("960x960")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.root, text="Genetic Algorithm Optimizer", font=("Arial", 16, "bold")
        )
        title.pack(pady=10)

        tk.Label(self.root, text="Select Function:").pack()
        self.function_var = tk.StringVar()
        self.function_dropdown = ttk.Combobox(
            self.root, textvariable=self.function_var, state="readonly"
        )
        self.function_dropdown.pack(pady=5)
        self.function_dropdown.bind("<<ComboboxSelected>>", self.on_function_change)

        self.dimensions_frame = tk.Frame(self.root)
        self.dimensions_frame.pack(pady=5)

        self.dimensions_label = tk.Label(self.dimensions_frame, text="Dimensions:")
        self.dimensions_label.pack(side=tk.LEFT)
        self.dimensions_var = tk.StringVar(value="2")
        self.dimensions_spinbox = tk.Spinbox(
            self.dimensions_frame,
            from_=2,
            to=20,
            textvariable=self.dimensions_var,
            width=10,
        )
        self.dimensions_spinbox.pack(side=tk.LEFT)

        self.init_function_dropdown()

        tk.Label(self.root, text="Population Size:").pack()
        self.population_entry = tk.Entry(self.root)
        self.population_entry.pack()
        self.population_entry.insert(0, "100")

        tk.Label(self.root, text="Number of Generations:").pack()
        self.generations_entry = tk.Entry(self.root)
        self.generations_entry.pack()
        self.generations_entry.insert(0, "500")

        tk.Label(self.root, text="Mutation Rate (0–1):").pack()
        self.mutation_entry = tk.Entry(self.root)
        self.mutation_entry.pack()
        self.mutation_entry.insert(0, "0.1")

        tk.Label(self.root, text="Seed (for reproducibility):").pack()
        self.seed_entry = tk.Entry(self.root)
        self.seed_entry.pack()
        self.seed_entry.insert(0, "15")

        tk.Button(
            self.root,
            text="Run Optimization",
            command=self.run_ga,
            bg="#4CAF50",
            fg="white",
            width=20,
        ).pack(pady=15)

        self.compare_button = tk.Button(
            self.root,
            text="Compare with Gradient Descent",
            command=self.compare_gd,
            bg="#2196F3",
            fg="white",
            width=20,
        )
        self.compare_button.pack(pady=5)

        self.result_label = tk.Label(
            self.root, text="Result will appear here", font=("Arial", 11), fg="blue"
        )
        self.result_label.pack(pady=10)

    def init_function_dropdown(self):
        all_functions = list(FUNCTION_INFO.keys())
        self.function_dropdown["values"] = all_functions
        self.function_dropdown.current(0)
        self.on_function_change()

    def on_function_change(self, event=None):
        function_name = self.function_var.get()
        if not function_name:
            return

        info = FUNCTION_INFO[function_name]

        if is_1d_function(info):
            self.dimensions_var.set("1")
            self.dimensions_spinbox.config(state="disabled")
            self.dimensions_label.config(text="Dimensions: 1 (fixed)")
        else:
            current_dims = self.dimensions_var.get()
            try:
                dims = int(current_dims)
            except ValueError:
                dims = 2
            dims = max(info["min_dimensions"], min(dims, info["max_dimensions"]))
            self.dimensions_var.set(str(dims))
            self.dimensions_spinbox.config(state="normal")
            self.dimensions_spinbox.config(from_=info["min_dimensions"])
            self.dimensions_spinbox.config(to=info["max_dimensions"])
            self.dimensions_label.config(text="Dimensions:")

        if info.get("has_gradient"):
            self.compare_button.pack(pady=5)
        else:
            self.compare_button.pack_forget()

    def run_ga(self):
        try:
            function_name = self.function_var.get()
            info = FUNCTION_INFO[function_name]

            dims = int(self.dimensions_var.get())
            population = int(self.population_entry.get())
            generations = int(self.generations_entry.get())
            mutation_rate = float(self.mutation_entry.get())
            seed_str = self.seed_entry.get().strip()
            seed = int(seed_str) if seed_str else None

            if not (0 <= mutation_rate <= 1):
                raise ValueError("Mutation rate must be between 0 and 1")

            if not (info["min_dimensions"] <= dims <= info["max_dimensions"]):
                raise ValueError(
                    f"Function requires {info['min_dimensions']}-{info['max_dimensions']} dimensions"
                )

            ga = GeneticAlgorithm(
                function=info["function"],
                dimensions=dims,
                population_size=population,
                generations=generations,
                mutation_rate=mutation_rate,
                bounds=info["bounds"],
                seed=seed,
            )

            best_x, best_fx, history = ga.run()

            x_str = ", ".join(f"{xi:.4f}" for xi in best_x)

            if info["optimum_value"] is not None:
                error = abs(best_fx - info["optimum_value"])
                result_text = (
                    f"Best Solution: [{x_str}]\n"
                    f"Best Fitness: {best_fx:.6f}\n"
                    f"Optimum: {info['optimum_value']} at {info['optimum_desc']}\n"
                    f"Error: {error:.6f}"
                )
            else:
                result_text = f"Best Solution: [{x_str}]\nBest Fitness: {best_fx:.6f}"

            self.result_label.config(text=result_text)

            plot_fitness(history, optimum=info.get("optimum_value"))

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def compare_gd(self):
        try:
            function_name = self.function_var.get()
            info = FUNCTION_INFO[function_name]

            dims = int(self.dimensions_var.get())
            population = int(self.population_entry.get())
            generations = int(self.generations_entry.get())
            mutation_rate = float(self.mutation_entry.get())
            seed_str = self.seed_entry.get().strip()
            seed = int(seed_str) if seed_str else None

            if not (0 <= mutation_rate <= 1):
                raise ValueError("Mutation rate must be between 0 and 1")

            if not (info["min_dimensions"] <= dims <= info["max_dimensions"]):
                raise ValueError(
                    f"Function requires {info['min_dimensions']}-{info['max_dimensions']} dimensions"
                )

            ga = GeneticAlgorithm(
                function=info["function"],
                dimensions=dims,
                population_size=population,
                generations=generations,
                mutation_rate=mutation_rate,
                bounds=info["bounds"],
                seed=seed,
            )

            ga_best_x, ga_best_fx, ga_history = ga.run()

            if seed is not None:
                random.seed(seed)

            lower, upper = info["bounds"]
            initial_point = [random.uniform(lower, upper) for _ in range(dims)]

            gd_best_fx, gd_best_x, gd_history = gradient_descent(
                initial_point, iterations=generations, bounds=info["bounds"]
            )

            ga_x_str = ", ".join(f"{xi:.4f}" for xi in ga_best_x)
            gd_x_str = ", ".join(f"{xi:.4f}" for xi in gd_best_x)

            result_text = (
                f"=== Genetic Algorithm ===\n"
                f"Solution: [{ga_x_str}]\n"
                f"Fitness: {ga_best_fx:.6f}\n\n"
                f"=== Gradient Descent ===\n"
                f"Solution: [{gd_x_str}]\n"
                f"Fitness: {gd_best_fx:.6f}\n\n"
            )

            if info["optimum_value"] is not None:
                ga_error = abs(ga_best_fx - info["optimum_value"])
                gd_error = abs(gd_best_fx - info["optimum_value"])
                result_text += (
                    f"Optimum: {info['optimum_value']} at {info['optimum_desc']}\n"
                    f"GA Error: {ga_error:.6f}\n"
                    f"GD Error: {gd_error:.6f}"
                )

            self.result_label.config(text=result_text)

            plot_comparison(ga_history, gd_history, optimum=info.get("optimum_value"))

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = GAApp(root)
    root.mainloop()
