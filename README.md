# Improved-Genetic-Algorithm
# Improved Genetic Algorithm

This repository contains a simplified but improved version of the Genetic Algorithm (GA) for solving permutation-based optimization problems (e.g., scheduling, TSP-like tasks).

## 🔧 Features

- **Elitism**: Best individuals are preserved each generation.
- **Tournament Selection**: Better convergence than roulette selection.
- **Order Crossover (OX)**: Suitable for permutation encoding.
- **Swap Mutation**: Maintains feasibility of individuals.
- **Local Search (Greedy 2-opt)**: Optional search refinement after each generation.
- **Random Immigration**: Adds population diversity by inserting random individuals.

## 📂 File

- `improved genetic algorithm.py`: The main Python script implementing the improved GA logic.

## 🚀 Usage

```python
from your_script import simulate_fn  # Define your evaluation function

best_ind, best_fit, history = ga_with_improvements(simulate_fn, N=20)
