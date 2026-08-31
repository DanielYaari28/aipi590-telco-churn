import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score
)

import matplotlib.pyplot as plt
import seaborn as sns

churn = pd.read_csv(
    r"C:\Users\dyaar\Downloads\Telco-Customer-Churn.csv"
)

#print(churn.head())

#churn.info()

#print("\nMissing values:")
#print(churn.isnull().sum())

churn["TotalCharges"] = pd.to_numeric(
    churn["TotalCharges"],
    errors="coerce"
)

print("\nMissing TotalCharges after conversion:")
print(churn["TotalCharges"].isnull().sum())


# Remove rows with missing TotalCharges
churn = churn.dropna(subset=["TotalCharges"])

# Verify cleaning
#print("\nDataset shape after cleaning:")
#print(churn.shape)

#print("\nMissing values after cleaning:")
#print(churn.isnull().sum())

# Check distribution of target variable
#print("\nChurn counts:")
#print(churn["Churn"].value_counts())

print("\nChurn percentages:")
print(churn["Churn"].value_counts(normalize=True))

# Plot churn distribution
plt.figure(figsize=(6, 4))

sns.countplot(data=churn, x="Churn")

plt.title("Distribution of Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.show()

# Separate predictors and target
X = churn.drop(columns=["Churn", "customerID"])
y = churn["Churn"]

# Convert target to binary
y = y.map({"No": 0, "Yes": 1})

# Convert categorical predictors to dummy variables
X = pd.get_dummies(X, drop_first=True, dtype=int)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training set:", X_train.shape)
print("Test set:", X_test.shape)

# Scale continuous features
continuous_features = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()

scaler = StandardScaler()

X_train_scaled[continuous_features] = scaler.fit_transform(
    X_train[continuous_features]
)

X_test_scaled[continuous_features] = scaler.transform(
    X_test[continuous_features]
)

# Create logistic regression model
log_model = LogisticRegression(max_iter=1000)

# Train model
log_model.fit(X_train_scaled, y_train)

# Predict churn class
y_pred = log_model.predict(X_test_scaled)

# Predict probability of churn
y_prob = log_model.predict_proba(X_test_scaled)[:, 1]

# Evaluate model performance
print("\nModel Performance:")

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No Churn", "Churn"],
    yticklabels=["No Churn", "Churn"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Logistic Regression Confusion Matrix")
plt.show()