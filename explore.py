import pandas as pd

# Load the data
df = pd.read_csv("data/retail_sales.csv")

# Basic look at the DataFrame
print("Shape (rows, columns):", df.shape)   # expect (5000, 6)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nInfo:")
df.info()

print("\nSummary statistics:")
print(df.describe())

print("\nMissing values per column:")
print(df.isna().sum())