import pandas as pd

# Load the dataset
df = pd.read_csv('feedback_data.csv')

# Check for duplicates
print(df.duplicated().sum())

# Remove duplicates based on selected columns
df.drop_duplicates(subset=['customer_id', 'timestamp'], keep='first', inplace=True)

# Verify the modified dataset
print(df.head())