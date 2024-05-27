# List of Indian names
indian_names = ['Aarav', 'Aadhya', 'Arjun', 'Ananya', 'Ishaan', 'Aarti', 'Karthik', 'Neha', 'Rahul', 'Priya']

# List of tuples containing names and their lengths
name_lengths = [(name, len(name)) for name in indian_names]

# Print the list of tuples
for name, length in name_lengths:
    print(f"{name}: {length}")
