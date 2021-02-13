# Aim- Understanding of data - head(), shape, columns functions
#---------------------------------------------------------------#

import pandas as pd
import os

os.getcwd()
os.chdir('D:\\Study\\All_datasets')

dataset = pd.read_csv('loan_small.csv')

# Functions of pandas
#----------------------#

# 1. head - get a quick view of data
print(dataset.head())
print(dataset.head(10))

# 2. shape of a dataset
print("Shape is ", dataset.shape)

# 3. get the column names
print("Column names are", dataset.columns)

# 4. Find out columns which have missing values and what is total no of them
print("Columns with missing values ", dataset.isnull().sum(axis=0))



