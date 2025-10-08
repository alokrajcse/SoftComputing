def triangular(x, a, b, c):
    """Triangular membership function"""
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
    elif x == b:
        return 1

# Fuzzy sets
Hot = (25, 35, 40)
High_Fan = (60, 80, 100)

# Input temperature
temp = 30

# Step 1: Fuzzification
mu_hot = triangular(temp, *Hot)
print("Membership of Hot at 30°C:", mu_hot)

# Step 2: Apply Rule -> Output fuzzy set clipped at mu_hot
import numpy as np

x_vals = np.linspace(60, 100, 100)  # Fan speed range
mu_high_fan = [min(triangular(x, *High_Fan), mu_hot) for x in x_vals]

# Step 3: Defuzzification using centroid method
numerator = sum(x * mu for x, mu in zip(x_vals, mu_high_fan))
denominator = sum(mu_high_fan)

fan_speed = numerator / denominator if denominator != 0 else None
print("Defuzzified Fan Speed:", fan_speed)
