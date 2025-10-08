
A = [(1, 0.1), (2, 0.5), (3, 0.9), (4, 0.9), (5, 0.7)]
max_mu = max(mu for _, mu in A)
max_elements = [x for x, mu in A if mu == max_mu]
height_method = max_elements
FoM = max_elements[0]
LoM = max_elements[-1]
MoM = sum(max_elements) / len(max_elements)
print("Fuzzy Set A:", A)
print("Maximum Membership Value:", max_mu)
print("Height Method:", height_method)
print("First of Maxima (FoM):", FoM)
print("Last of Maxima (LoM):", LoM)
print("Mean of Maxima (MoM):", MoM)
