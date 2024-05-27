# Part 1: Create a variable pi and check its data type
pi = 22 / 7
data_type_pi = type(pi)
print(f"The data type of pi is: {data_type_pi}")

# Part 2: Explanation about reserved keyword 'for'
# Uncommenting the next line will result in a syntax error.
# for = 4

# Explanation:
# The variable name 'for' cannot be used because it is a reserved keyword in Python.

# Part 3: Calculate Simple Interest
P = 1000  # Principal amount
R = 5     # Rate of interest
T = 3     # Time in years

Simple_Interest = (P * R * T) / 100
print(f"The Simple Interest for 3 years is: {Simple_Interest}")
