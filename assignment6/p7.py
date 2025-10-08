import random

# ----- Step 1: Define a binary chromosome -----
chromosome = "1010110"
print("Original Chromosome:", chromosome)

def bit_flip_mutation(chromosome, mutation_rate=0.2):
    
    chromosome_list = list(chromosome) 
    
    for i in range(len(chromosome_list)):
        if random.random() < mutation_rate: 
            
            chromosome_list[i] = '1' if chromosome_list[i] == '0' else '0'
            print(f"Bit at position {i} flipped!")
    
    return ''.join(chromosome_list)

mutated_chromosome = bit_flip_mutation(chromosome, mutation_rate=0.3)

print("Mutated Chromosome:", mutated_chromosome)
