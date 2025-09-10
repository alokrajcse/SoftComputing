import numpy as np

# Define membership functions
def mu_A(x):
    return x / (1 + x)

def mu_B(x):
    return 2 - x

def check_contains():
    xs = np.linspace(0, 5, 100) 
    for x in xs:
        if mu_B(x) > mu_A(x):  
            return False
    return True

if check_contains():
    print("A contains B (B is a fuzzy subset of A).")
else:
    print("A does not contain B.")
