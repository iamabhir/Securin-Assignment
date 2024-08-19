import itertools
from collections import Counter

# Representing Die A and Die B as arrays and for last function this represents original die
die_A = [1, 2, 3, 4, 5, 6]
die_B = [1, 2, 3, 4, 5, 6]

print("Part A")
def total_combinations(die_A, die_B):
    # Number of faces on each die
    num_faces_A = len(die_A)
    num_faces_B = len(die_B)
    
    # Total combinations is the product of the number of faces on both dice
    total_combinations = num_faces_A * num_faces_B
    
    print(f"1. Total combinations possible: {total_combinations}")
    print("\n")
    
    return total_combinations

# Calculate total combinations
total_combinations(die_A, die_B)

def display_combination_distribution(die_A, die_B):
    # Create a 6x6 matrix to store the sums
    matrix = []
    
    # Loop through all combinations of Die A and Die B
    for i in range(len(die_A)):
        row = []
        for j in range(len(die_B)):
            # Calculate the sum of the current combination
            sum_of_dice = die_A[i] + die_B[j]
            row.append(sum_of_dice)
        matrix.append(row)
    
    # Display the matrix
    print("2. Combination Distribution (6x6 Matrix):")
    for row in matrix:
        print(row)
    print("\n")

# Display the combination distribution
display_combination_distribution(die_A, die_B)

def calculate_probabilities(die_A, die_B):
    # Dictionary to hold the frequency of each sum
    sum_counts = Counter()
    
    # Calculate the frequency of each sum
    for i in range(len(die_A)):
        for j in range(len(die_B)):
            sum_of_dice = die_A[i] + die_B[j]
            sum_counts[sum_of_dice] += 1
    
    # Total number of combinations
    total_combinations = len(die_A) * len(die_B)
    
    # Calculate and print the probabilities
    print("3. Probability of each possible sum:")
    for sum_value in range(2, 13):  # Possible sums range from 2 to 12
        probability = sum_counts[sum_value] / total_combinations
        print(f"P(Sum = {sum_value}) = {sum_counts[sum_value]}/{total_combinations} = {probability:.4f}")

# Calculate and display probabilities
calculate_probabilities(die_A, die_B)

print("\n")

print("Part B")

def undoom_dice(die_A, die_B):
    # Initialize new die arrays
    new_die_A = [1, 1, 1, 1, 1, 1]  # We ensure all values are ≤ 4 for Die A
    new_die_B = []
    
    # Reattach spots to Die B to maintain the same sum probabilities
    for i in range(6):
        new_die_B.append(die_A[i] + die_B[i] - new_die_A[i])
    
    return new_die_A, new_die_B

# Transform the doomed dice
new_die_A, new_die_B = undoom_dice(die_A, die_B)

# Display the results
print("New Die A:", new_die_A)
print("New Die B:", new_die_B)
