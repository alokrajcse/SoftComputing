# Membership values
Mary = 0.8
Ram = 0.65

# Fuzzy operations
not_Mary = 1 - Mary
mary_and_ram = min(Mary, Ram)
mary_or_ram = max(Mary, Ram)
mary_implies_ram = max(1 - Mary, Ram)

# Print results
print("Mary is not efficient:", round(not_Mary, 2))
print("Mary is efficient AND Ram is efficient:", round(mary_and_ram, 2))
print("Mary is efficient OR Ram is efficient:", round(mary_or_ram, 2))
print("If Mary is efficient THEN Ram is efficient:", round(mary_implies_ram, 2))
