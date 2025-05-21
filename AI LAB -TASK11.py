import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load and preprocess the dataset
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

# Extract numeric duration
df['duration_int'] = df['duration'].str.extract('(\d+)').astype(float).fillna(0).astype(int)

# Encode categorical columns
label_encoders = {}
for col in ['country', 'rating', 'director']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Encode target column
le_type = LabelEncoder()
df['type_encoded'] = le_type.fit_transform(df['type'])  # Movie = 1, TV Show = 0

# Select features and target
X = df[['release_year', 'duration_int', 'country', 'rating', 'director']]
y = df['type_encoded']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Choose and train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("✅ Accuracy Score:", accuracy)
