import matplotlib.pyplot as plt

# Discrete fuzzy set
elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N']
membership_values = [0.2, 0.8, 0.6, 0.2, 0.4, 0.9, 0.1, 0.7, 
                     0.3, 0.4, 0.6, 0.1, 0.9, 0.8]

# Plotting
plt.figure(figsize=(10, 5))
plt.stem(elements, membership_values, basefmt=" ")
plt.ylim(0, 1.1)  # Membership values are always between 0 and 1
plt.xlabel("Elements")
plt.ylabel("Membership Values")
plt.title("Discrete Fuzzy Set")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
