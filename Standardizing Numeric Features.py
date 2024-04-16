import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Standardize numeric features
scaler = StandardScaler()
df['sales'] = scaler.fit_transform(df['sales'].values.reshape(-1, 1))

# Verify the modified dataset
print(df.head())