# Aim - Data Normalization using standard scaler (z score)
#----------------------------------------------------------#

import pandas as pd
import os
import sklearn

os.getcwd()
os.chdir('D:\\Study\\All_datasets')

dataset = pd.read_csv('loan_small.csv')

# Drop rows with missing values
cleandata = dataset.dropna()

# We drop all the missing rows cz our aim is to just
# see normalization, size of data not v.imp

# Extract numeric columns in another df (columns 2,3,4)
data_to_scale = cleandata.iloc[:, 2:5]

# import standard scaler
# StandardScaler uses z score method of data standardization
# Standardscalar is a class so we first create object of it
from sklearn.preprocessing import StandardScaler
scaler_ = StandardScaler()

# Use fit_transform method, requires i/p data which will be
# first fitted and then transformed
ss_scaler = scaler_.fit_transform(data_to_scale)



