import random

# ----- Step 1: Define a binary chromosome -----
chromosome = "1101010"
print("Original Chromosome:", chromosome)

# ----- Step 2: Random Resetting Mutation Function -----
def random_resetting_mutation(chromosome, mutation_rate=0.2):
    """
    Performs random resetting mutation on a binary string.
    Each bit has a probability 'mutation_rate' to be flipped (0→1 or 1→0).
    """
    chromosome_list = list(chromosome)  # convert string to list for easy modification
    
    for i in range(len(chromosome_list)):
        if random.random() < mutation_rate:
            # Flip the bit (0 -> 1 or 1 -> 0)
            chromosome_list[i] = '1' if chromosome_list[i] == '0' else '0'
            print(f"Bit at position {i} mutated!")

    return ''.join(chromosome_list)

# ----- Step 3: Apply Mutation -----
mutated_chromosome = random_resetting_mutation(chromosome, mutation_rate=0.3)

print("Mutated Chromosome:", mutated_chromosome)
