import random

# Population
population = ["01101", "11000", "10110", "00111", "10101", "00010"]

# Fitness function: count of '1's
def fitness(chromosome):
    return chromosome.count('1')

# Compute fitness for each chromosome
fitness_values = [fitness(ch) for ch in population]
print("Population:", population)
print("Fitness values:", fitness_values, "\n")

# ----------------------------
# 1. Roulette Wheel Selection
# ----------------------------
def roulette_wheel_selection(pop, fitness_values):
    total_fitness = sum(fitness_values)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, f in enumerate(fitness_values):
        current += f
        if current > pick:
            return pop[i]

selected_rw = [roulette_wheel_selection(population, fitness_values) for _ in range(2)]
print("Roulette Wheel Selected:", selected_rw)

# ----------------------------
# 2. Tournament Selection
# ----------------------------
def tournament_selection(pop, fitness_values, k=3):
    selected = random.sample(list(zip(pop, fitness_values)), k)
    # Pick the best among the tournament participants
    selected.sort(key=lambda x: x[1], reverse=True)
    return selected[0][0]

selected_tour = [tournament_selection(population, fitness_values) for _ in range(2)]
print("Tournament Selected:", selected_tour)

# ----------------------------
# 3. Rank Selection
# ----------------------------
def rank_selection(pop, fitness_values):
    sorted_pop = sorted(list(zip(pop, fitness_values)), key=lambda x: x[1])
    ranks = [i + 1 for i in range(len(sorted_pop))]
    total_rank = sum(ranks)
    pick = random.uniform(0, total_rank)
    current = 0
    for i, rank in enumerate(ranks):
        current += rank
        if current > pick:
            return sorted_pop[i][0]

selected_rank = [rank_selection(population, fitness_values) for _ in range(2)]
print("Rank Selected:", selected_rank)
