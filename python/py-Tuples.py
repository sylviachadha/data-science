# Python - tuples

# Like lists and array it is also a sequence/collection of elements
# and its values can be accessed using index.
# Instead of square brackets, use normal bracket
# Tuple - u cannot add or remove elements, whole tuple will
# need to be deleted. Can only access elements.
# Tuples are faster, useful when passing data to dbms
# can use tuples when u have values which u do not wish to change

# Define tuple
t1 = (1,2,3,4,5)

# Access elements of tuple
print(t1[1])

# Length of tuple
len(t1)

# Define another tuple
t2 = (6,7,8)

# Concatenation of tuples
concat = t1 + t2
print(concat)

