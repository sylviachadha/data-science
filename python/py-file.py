# File Handling
# File Functions Open, Read, Write and Close

import os

# Get current working directory
os.getcwd()

# Change current working directory
os.chdir('D:\\Study\\All_datasets')

# OPen file
cityTemp = open("citytemp.csv", 'r')  # open file for reading
# Other modes of opening can be w - write r - read a - append
# w overwrites existing records while append appends at end
# if file does not exist both w and a will create the file

citywrite = open('citywrite.csv', 'a') # open file for writing

rec1 = cityTemp.readline() # reads one record

rec2 = cityTemp.readlines() # reads all lines starting from pointer

# Data Processing

city, temperature, unit = rec1.split(',')

# To apply arithmetic operation to convert temp u need to
# change temperature from string to int or float
temperature = (float(temperature) - 32) * 5/9

# Write record to a file
# To write u need to open in append mode, to write u need
# to open in write mode
cityTemp = open("citytemp.csv", 'a')
cityTemp.write(rec1)

# Closing file
cityTemp.close()

# After closing cannot read file, need to re-open again
# Process data using loops
# seek keyword

# Open file again
cityTemp = open("citytemp.csv", 'r')

# Either re-open file or use seek to get pointer to first line
cityTemp.seek(0) # to get pointer on first line
for records in cityTemp:
    records = records.rstrip('\n')
    print(records)




















