# Dictionary data type in python
# stores data as a key-value pair eg 'City':'Faridabad'
# Dictionary within curly brackets
# To access value, instead of index, provide key (so no need to remember index)
# Dictionary of python r used for conversion into JSON Format which
# is also a key value pair as well as when we read JSON format
# into python.

# Define Dictionary
Address = {'Street':'180 Adams Street',
           'City':'Chicago',
           'State': 'IL',
           'Country': 'USA'}

# Access elements of dictionary
print(Address['Street'])
# U give the key name in dictionary whose value you want to access

# Operations on Dictionary
# Update dictionary

Address['Street'] = '181 Adams Street'

# Add a key-value pair to a dictionary
Address['zip code'] = 60611

# Delete a key value pair
del Address['zip code']

# Methods and Functions that can be applied on dictionary
# Get length of dictionary
length = len(Address)

# Convert the dictionary into string
str(Address)

# Get all keys in a dictionary
print(Address.keys())

# Get all values in a dictionary
print(Address.values())
