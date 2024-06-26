marks = [3, 5, 7, "Rudra", 123, 456, 15, 95, 53]
print(marks)
print(marks[3])
print(marks[-3])
print(marks[len(marks)-3])

if 5 in marks:
    print("yes")
else:
    print("no")
    
print(marks[3:])
print(marks[1:5])
print(marks[1:5:2])
print(marks[1::2])

lst = [i * i for i in range(9)]
print(lst)
lst = [i * i for i in range(9) if i%2==0]
print(lst)

# Define a list
my_list = [1, 2, 3, 4, 5]

# Original list
print("Original List:", my_list)

# Modify the list
my_list[0] = 10
print("After modification:", my_list)  # Output: [10, 2, 3, 4, 5]

# Append an element to the list
my_list.append(6)
print("After append:", my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Extend the list with another list
my_list.extend([7, 8, 9])
print("After extend:", my_list)  # Output: [10, 2, 3, 4, 5, 6, 7, 8, 9]

# Remove an element from the list
my_list.remove(2)
print("After remove:", my_list)  # Output: [10, 3, 4, 5, 6, 7, 8, 9]
