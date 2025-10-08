import random

# ----- Step 1: Initialize population -----
population_size = 6  # You can change this
max_value = 64       # x ranges from 0 to 64

# Generate random population (values between 0 and 64)
population = [random.randint(0, max_value) for _ in range(population_size)]

# Convert each value to 7-bit binary representation (since 64 -> needs 7 bits)
binary_population = [format(x, '07b') for x in population]

print("Initial Population (Binary):", binary_population)
print("Decimal Values:", population)

# ----- Step 2: Objective Function -----
def fitness(x):
    return x   # f(x) = x

# Calculate fitness values
fitness_values = [fitness(x) for x in population]
print("Fitness Values:", fitness_values)

# ----- Step 3: Tournament Selection Function -----
def tournament_selection(pop, fitness_vals, k=3):
    # Randomly select k individuals
    participants = random.sample(list(zip(pop, fitness_vals)), k)
    # Choose the one with the highest fitness
    participants.sort(key=lambda x: x[1], reverse=True)
    return participants[0][0]

# ----- Step 4: Generate Next Generation -----
next_generation = [tournament_selection(population, fitness_values) for _ in range(population_size)]

# Convert to binary for display
binary_next_gen = [format(x, '07b') for x in next_generation]

print("\nNext Generation (Decimal):", next_generation)
print("Next Generation (Binary):", binary_next_gen)
