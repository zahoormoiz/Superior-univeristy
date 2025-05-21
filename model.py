import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv('netflix_titles.csv')

# Fill missing values
df['country'].fillna('Unknown', inplace=True)
df['director'].fillna('Not Specified', inplace=True)
df['cast'].fillna('Not Specified', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
df['date_added'].fillna('Unknown', inplace=True)
df['duration'].fillna('0', inplace=True)
df['type'].fillna('Movie', inplace=True)
df['release_year'] = df['release_year'].fillna(0).astype(int)
df['duration_int'] = df['duration'].str.extract('(\d+)').astype(float).fillna(0).astype(int)

# Label Encoding
le_country = LabelEncoder()
le_rating = LabelEncoder()
le_director = LabelEncoder()
le_type = LabelEncoder()

df['country_enc'] = le_country.fit_transform(df['country'])
df['rating_enc'] = le_rating.fit_transform(df['rating'])
df['director_enc'] = le_director.fit_transform(df['director'])
df['type_enc'] = le_type.fit_transform(df['type'])  # 1 = Movie, 0 = TV Show

# Features & Target
X = df[['release_year', 'duration_int', 'country_enc', 'rating_enc', 'director_enc']]
y = df['type_enc']

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, 'model.pkl')
joblib.dump(le_country, 'le_country.pkl')
joblib.dump(le_rating, 'le_rating.pkl')
joblib.dump(le_director, 'le_director.pkl')
joblib.dump(le_type, 'le_type.pkl')

print("✅ Model and encoders saved!")
