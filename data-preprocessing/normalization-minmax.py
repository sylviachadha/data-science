# Aim - Data Normalization using minmax scaler
#-----------------------------------------------#

import pandas as pd
import os
import sklearn

os.getcwd()
os.chdir('D:\\Study\\All_datasets')

dataset = pd.read_csv('loan_small.csv')

# Drop rows with missing values
cleandata = dataset.dropna()

# Numeric columns to scale
data_to_scale = cleandata.iloc[:, 2:5]

# minmax scaler
from sklearn.preprocessing import minmax_scale
mm_scaler = minmax_scale(data_to_scale)



