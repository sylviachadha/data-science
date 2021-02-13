# Aim - Import file and access elements
#-----------------------------------------#

import pandas as pd
import os
# When we import a library all the available functions and
# attributes within it are available to the current program.

# Get cwd and change cwd
os.getcwd()
os.chdir('D:\\Study\\All_datasets')

# read csv file using pandas
dataset = pd.read_csv('loan_small.csv')

# dataset is of type dataframe and size 16*7 as shown
# df is a 2 dimensional table structure array (16 rows & 7 columns)
# Index starts from 0, we can access data using these indices

# Access data of dataframe using iloc(index location)
# Accessing first 3 rows and 1st and 2nd col gender and id

subset = dataset.iloc[0:3, 1:3]

# Accessing the data using column names
subsetN = dataset[['Gender', 'ApplicantIncome']][0:3]

# csv - comma separated file
# tsv - tab separated file

# Read tsv file
datasetT = pd.read_csv('Loan_small_tsv.txt', sep='\t')