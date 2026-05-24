# =========================================================
# ROAD ACCIDENT SEVERITY PREDICTION PROJECT
# USING YOUR ACTUAL DATASET COLUMNS
# =========================================================

# =========================
# IMPORT LIBRARIES
# =========================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns

import joblib

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("traffic_accidents.csv")

# =========================
# SHOW DATA
# =========================

print(df.head())

print("\nDataset Shape:")
print(df.shape)

# =========================
# SELECT IMPORTANT COLUMNS
# MAX 10 INPUT COLUMNS
# =========================

df = df[[
    
    'traffic_control_device',
    'weather_condition',
    'lighting_condition',
    'first_crash_type',
    'trafficway_type',
    'alignment',
    'roadway_surface_cond',
    'road_defect',
    'crash_hour',
    'crash_day_of_week',
    
    # TARGET COLUMN
    'crash_type'

]]

# =========================
# REMOVE MISSING VALUES
# =========================

df = df.dropna()

# =========================
# SHOW CLEANED DATA
# =========================

print("\nCleaned Dataset Shape:")
print(df.shape)

# =========================
# ENCODE CATEGORICAL DATA
# =========================

label_encoder = LabelEncoder()

for column in df.columns:
    
    df[column] = label_encoder.fit_transform(df[column])

# =========================
# INPUT AND OUTPUT
# =========================

X = df.drop('crash_type', axis=1)

y = df['crash_type']

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42

)

# =========================
# CREATE MODEL
# =========================

model = RandomForestClassifier(

    n_estimators=100,
    random_state=42

)

# =========================
# TRAIN MODEL
# =========================

model.fit(X_train, y_train)

# =========================
# PREDICTION
# =========================

y_pred = model.predict(X_test)

# =========================
# ACCURACY
# =========================

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(accuracy)

# =========================
# CLASSIFICATION REPORT
# =========================

print("\nClassification Report:\n")

print(classification_report(y_test, y_pred))

# =========================
# CONFUSION MATRIX
# =========================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:\n")
print(cm)

# =========================
# CONFUSION MATRIX GRAPH
# =========================

plt.figure(figsize=(10,7))

sns.heatmap(cm, annot=True, fmt='d')

plt.title("Confusion Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.show()

# =========================
# FEATURE IMPORTANCE
# =========================

importance = pd.DataFrame({

    'Feature': X.columns,
    'Importance': model.feature_importances_

})

importance = importance.sort_values(

    by='Importance',
    ascending=False

)

print("\nFeature Importance:\n")

print(importance)

# =========================
# FEATURE IMPORTANCE GRAPH
# =========================

plt.figure(figsize=(10,5))

sns.barplot(

    x='Importance',
    y='Feature',
    data=importance

)

plt.title("Feature Importance")

plt.show()

# =========================
# SAVE MODEL
# =========================

joblib.dump(model, "accident_model.pkl")

print("\nModel Saved Successfully")
