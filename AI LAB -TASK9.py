import pandas as pd

# Load the dataset
df = pd.read_csv('netflix_titles.csv')

# Display basic information
print("Dataset Shape:", df.shape)
print("\nData Types and Missing Values:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# Summary statistics
print("\nSummary Statistics (Numerical):")
print(df.describe())
print("\nSummary Statistics (Categorical):")
print(df.describe(include='object'))

# Missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Unique values per column
print("\nUnique Values Per Column:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()}")

# Value counts
print("\nValue Counts for 'type':")
print(df['type'].value_counts())

print("\nTop 10 Countries by Number of Titles:")
print(df['country'].value_counts().head(10))

print("\nDistribution of Ratings:")
print(df['rating'].value_counts())
