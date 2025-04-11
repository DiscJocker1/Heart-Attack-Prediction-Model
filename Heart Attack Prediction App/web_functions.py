import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, f1_score
import pandas as pd
import numpy as np

# # Load trained model
# with open("model-2.pkl", "rb") as model_file:  # Make sure this matches your downloaded model
#     model = pickle.load(model_file)

# # Load saved scaler
# with open("scaler.pkl", "rb") as scaler_file:
#     scaler = pickle.load(scaler_file)

# Define Attention Layer



def load_data():
    
    """Loads and preprocesses the dataset for the Streamlit app."""
    # df = pd.read_csv("CardiologyScienceFairDataset.csv")
    df = pd.read_csv("Medicaldataset.csv")

    # Define X (features) and y (target)
    # X = df.drop(columns=["DEATH_EVENT"])
    # y = df["DEATH_EVENT"]

    X = df.drop(columns=["Result"])
    y = df["Result"]

    return df, X, y

def train_model(X, y):
    """Trains a new model and returns it along with accuracy score."""
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest model
    rf = RandomForestClassifier(n_estimators=300, max_depth=20, min_samples_split=5, min_samples_leaf=1, random_state=42)  # Use the same best params
    rf.fit(X_train, y_train)

    # Get accuracy score
    accuracy = accuracy_score(y_test, rf.predict(X_test))

    return rf, accuracy

def predict(features):
    """Predicts heart attack risk based on input features"""

    # Scale the input features
    features_scaled = scaler.transform(np.array(features).reshape(1, -1))

    # Make prediction
    prediction = model.predict(features_scaled)[0]
    confidence = model.predict_proba(features_scaled)[0][prediction]

    return prediction, confidence
