import pandas as pd

# Load dataset
df = pd.read_csv('netflix_titles.csv')

# Drop rows with nulls in critical columns
df = df.dropna(subset=['type', 'title'])

# Fill missing values for less critical columns
df['country'].fillna('Unknown', inplace=True)
df['director'].fillna('Not Specified', inplace=True)
df['cast'].fillna('Not Specified', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
df['date_added'].fillna('Unknown', inplace=True)
df['duration'].fillna('0', inplace=True)

# Convert 'duration' column to integer (extracting numbers)
# Works differently for Movies and TV Shows, so we extract numbers only
df['duration_int'] = df['duration'].str.extract('(\d+)').astype('float').fillna(0).astype('int')

# OPTIONAL: Convert 'release_year' to integer (already int in most cases)
df['release_year'] = df['release_year'].fillna(0).astype('int')

# Confirm changes
print("Updated Dataset Info:")
print(df.info())
print("\nSample Rows:")
print(df[['title', 'duration', 'duration_int']].head())
