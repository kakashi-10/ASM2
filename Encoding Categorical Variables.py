import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('product_data.csv')

# Encode categorical variables using LabelEncoder
encoder = LabelEncoder()
df['category_encoded'] = encoder.fit_transform(df['category'])

# Verify the modified dataset
print(df.head())