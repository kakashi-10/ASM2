import pandas as pd

# Load the dataset
df = pd.read_csv('defects_data.csv')

# Check for missing values
print(df.isnull().sum())

# Handle missing values by filling with the mean
df['defects'].fillna(df['defects'].mean(), inplace=True)

# Alternatively, drop rows with missing values
# df.dropna(inplace=True)

# Verify the modified dataset
print(df.head())