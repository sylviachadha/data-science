# Aim - Label encoding for categorical variables
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


# Maths is the basis of ML, whether we talk about Regression,
# Classification or any other algorithm based on math equations
# Maths Equations in form of numbers, so we do not feed the
# categorical variables directly, rather code them to numbers

# Label encoding using pandas (can also use sklearn)

# Check datatypes
print(dt.dtypes)
# Change datatypes
dt[cols] = dt[cols].astype('category')
print(dt.dtypes)

# cat.codes change categorical to numerical values
for columns in cols:
    dt[columns] = dt[columns].cat.codes

