import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
from phishing_features import extract_features
import numpy as np

# Load the dataset - Assuming the CSV is in the project root directory
# IMPORTANT: You need to have the 'phishing_site_urls.csv' file in the same directory as this script.
try:
    df = pd.read_csv('phishing_site_urls.csv')
except FileNotFoundError:
    print("FATAL: 'phishing_site_urls.csv' not found in the project directory.")
    print("Please download the dataset and place it in the root of the project directory to train the model.")
    exit()

print("Dataset loaded successfully.")
print(f"Dataset contains {len(df)} URLs.")
print("Sample URLs from the dataset:")
print(df.head())


# Extract features and labels
print("\nExtracting features from URLs... (This may take a while)")
df['features'] = df['URL'].apply(extract_features)
X = pd.DataFrame(df['features'].tolist()) 
y = df['Label']

# Show dataset balance
print("\nDataset balance:")
print(y.value_counts())

# Split data into training and testing sets
# Using stratify to maintain the same distribution of labels in train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("\nTraining the RandomForestClassifier model...")
# Using more estimators for potentially better performance
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
print("Model training complete.")

# Evaluate the model
print("\n--- Model Evaluation ---")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print("------------------------")


# Save the trained model
joblib.dump(model, 'model.pkl')

print("\nSuccessfully trained and saved the new model as 'model.pkl'.")
