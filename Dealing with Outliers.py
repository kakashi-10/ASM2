import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('cycle_times.csv')

# Detect outliers using z-score
z_scores = np.abs((df['cycle_time'] - df['cycle_time'].mean()) / df['cycle_time'].std())
outliers = df[z_scores > 3]

# Remove outliers
df = df[z_scores <= 3]

# Verify the modified dataset
print(df.head())