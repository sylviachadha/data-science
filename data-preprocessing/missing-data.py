# Aim- data preprocess, handle missing data
#--------------------------------------------#

import pandas as pd
import os

os.getcwd()
os.chdir('D:\\Study\\All_datasets')

dataset = pd.read_csv('loan_small.csv')

# Find out which columns have missing values and how many
dataset.isnull().sum(axis=0)

# nan - not a number
# ML algo's cannot understand missing values
# Deal with missing values
# 1. If rows with missing values are not too many, we can completely remove them
# Not best method because u remove the data
cleandata = dataset.dropna()

# If want to remove rows which have missing values in a particular column only
cleandata = dataset.dropna(subset=['Loan_Status'])

# Replace missing values with either mode or mean for remaining columns
# Mode for the categorical data and mean for the numerical variables

# Copy the dataset
dt = dataset.copy()

# Replace categorical values with mode
cols = ['Gender', 'Area', 'Loan_Status']

# fillna function that fills / replaces nan values

# iloc[0] allows to pick up only 1st mode incase there is more than 1 mode
# all cols mentioned will be replaced with their respective model values
dt[cols] = dt[cols].fillna(dt.mode().iloc[0])
# To check count again to verify if categorical values have been replaced
dt.isnull().sum(axis=0)

# Replacing the numerical missing values
cols2 = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']
dt[cols2] = dt[cols2].fillna(dt.mean())
print(dt.isnull().sum(axis=0))


