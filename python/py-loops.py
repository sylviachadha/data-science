# Loops / iterative statement
# for loop and while loop

# while loop
# for variables in collection/sequence:
#     statements

i = 0
while i < 10:
    print(i)
    i = i + 2


# Using Boolean variable
# Initially set to True
var1 = True
i = 0

while var1:
    print(i)
    i = i + 2
    if i >= 10:
        var1 = False


# for loop - no conditional check only sequence

name = "Sylvia"

for letters in name:
    print(letters)

# for loop in sequence
for i in range(0,10,2):
    print(i)
else:
    print("Outside for loop", str(i))







