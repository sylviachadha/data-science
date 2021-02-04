# Lists in Python - imp data type of python
# ------------------------------------------
# Sequence of elements, similar to array in other
# programming languages

# Elements are indexed, index starts at 0

# Declare and initialize list
list1 = ["Sylvia","Manuj","Payal"]

# Access elements
print(list1[2])

# Operations in list

# Add elements to list
list1.append("Akash")
print(list1)

# Update list - change sylvia to jennifer
list1[0] = "Jennifer"
print(list1)

# Delete an element in list
del list1[2]
print(list1)

# Get the length of list
print(len(list1))

# Concatenate 2 lists
list2 = ["a","b","c"]

conlist = list1 + list2
print(conlist)

# Sort content of list
# Cannot assign ans to a variable cz function
# sort does not return anything
list1.sort()



# Multidimensional Lists (Lists within a list)
# Multidimensional lists is in form of rows and columns (or table)

twodlist = [["Sylvia","Manuj","Lisa"],[123,345,567]]
# Below First [0] tells us which list we want to access (row) and
# second [1] tells us which element within that list we want
# to access (column)

print(twodlist[0])

print(twodlist[0][1])

# To access 567
print(twodlist[1][2])



# Slicing of Multidimensional/ creating sublists
sublist = []

list = [["a","b","c",],[1,2,3]]

# Using for loop so lists will come one by one
for alllists in list:
    sublist.append(alllists[0:2])
