# Aim - One hot encoding for categorical variables
#-------------------------------------------------#

import pandas as pd
import os

os.getcwd()
os.chdir('D:\\Study\\All_datasets')

dataset = pd.read_csv('loan_small.csv')

# Fill missing values
dt = dataset.copy()

# Replacing categorical values with mode
cols = ['Gender', 'Area', 'Loan_Status']
dt[cols] = dt[cols].fillna(dt.mode().iloc[0])

# Replacing numerical values with mean
cols2 = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']
dt[cols2] = dt[cols2].fillna(dt.mean())
print(dt.isnull().sum(axis=0))

# Remove Loan id cz it is just like idetifier it will have no
# impact on the predictions

# axis=0 means talking about rows and axis=1 means talking about columns
df2 = dataset.drop(['Loan_ID'], axis=1)

# Create dummy variables
# dummies function
df2 = pd.get_dummies(df2)






