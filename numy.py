# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)
print(type(np_height))

# Element wise calculation
# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
# Subsetting

# For a boolean response

# Print only those observations above 23

print(bmi[bmi > 24])
print (bmi > 24)

# Exercice

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)    

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np.array(np_weight_kg*0.45359237)

# Print out np_weight_lbs
print(np_weight_kg)
print(np_weight_lbs)