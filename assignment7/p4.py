import random

# --- Problem Data ---
values = [60, 100, 120, 90, 30]     # item values
weights = [10, 20, 30, 25, 5]       # item weights
capacity = 50                       # maximum weight limit
n_items = len(values)

# --- GA Parameters ---
POP_SIZE = 20
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.05
GENERATIONS = 50
TOURNAMENT_SIZE = 3




# Create a random binary chromosome
def create_individual():
    return ''.join(random.choice('01') for _ in range(n_items))

# Fitness: total value if within capacity, else 0
def fitness(individual):
    total_value = 0
    total_weight = 0
    for i, bit in enumerate(individual):
        if bit == '1':
            total_value += values[i]
            total_weight += weights[i]
    if total_weight > capacity:
        return 0
    return total_value

# Tournament selection
def tournament_selection(population):
    contenders = random.sample(population, TOURNAMENT_SIZE)
    return max(contenders, key=fitness)

# Single-point crossover
def single_point_crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, n_items - 1)
        child = parent1[:point] + parent2[point:]
        return child
    return parent1

# Bit flip mutation
def bit_flip_mutation(individual):
    mutated = ''
    for bit in individual:
        if random.random() < MUTATION_RATE:
            mutated += '0' if bit == '1' else '1'
        else:
            mutated += bit
    return mutated


# --- Genetic Algorithm ---
def genetic_algorithm():
    population = [create_individual() for _ in range(POP_SIZE)]

    for gen in range(GENERATIONS):
        new_population = []

        for _ in range(POP_SIZE):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)

            # Crossover + Mutation
            child = single_point_crossover(parent1, parent2)
            child = bit_flip_mutation(child)
            new_population.append(child)

        population = new_population

        # Find best of this generation
        best = max(population, key=fitness)
        best_fit = fitness(best)
        selected_items = [i+1 for i, bit in enumerate(best) if bit == '1']

        print(f"Gen {gen+1:2d}: Best = {best}, Value = {best_fit}, Items = {selected_items}")

    # Final result
    best = max(population, key=fitness)
    best_fit = fitness(best)
    selected_items = [i+1 for i, bit in enumerate(best) if bit == '1']

    print("\nFinal Best Solution:")
    print(f"Chromosome: {best}")
    print(f"Selected items: {selected_items}")
    print(f"Total value: {best_fit}")
    print(f"Total weight: {sum(weights[i] for i, bit in enumerate(best) if bit == '1')}")


# --- Run the GA ---
genetic_algorithm()
