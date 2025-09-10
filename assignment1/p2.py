import matplotlib.pyplot as plt

# Discrete universe of x values
x_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Calculate membership values μx = x / 10
membership_values = [x / 10 for x in x_values]

# Plot
plt.stem(x_values, membership_values, basefmt=" ")
plt.xlabel("x")
plt.ylabel("μx")
plt.title("Discrete Fuzzy Set: μx = x/10")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
