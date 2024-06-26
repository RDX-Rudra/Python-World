def print_pattern(n):
    for i in range(1, n + 1):
        print(str(i) * i)

# Define the number of lines for the pattern
num_lines = 5

# Print the pattern
print_pattern(num_lines)

def print_pattern(n):
    for i in range(1, n + 1):
        print(' '.join(str(i) for _ in range(i)))

# Define the number of lines for the pattern
num_lines = 5

# Print the pattern
print_pattern(num_lines)
