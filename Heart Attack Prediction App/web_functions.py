"""This module contains necessary function needed"""

# Import necessary modules
import numpy as np
import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
import streamlit as st

# from pandas import Series, DataFrame,read_csv
# from sklearn.utils import shuffle
# import sklearn as sklearn
# import matplotlib.pyplot as plt
# from sklearn import tree
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeRegressor
# from sklearn import metrics, svm
# from sklearn.model_selection import train_test_split

@st.cache()
def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('CardiologyScienceFairDataset.csv')

    # Rename the column names in the DataFrame.
    
    # Perform feature and target split
    # X = df[['age_mean','anaemia_mean','cpk_mean','diabetes_mean','ef_mean','high_blood_pressure_mean','platelets_mean','serum_creatinine_mean','serum_sodium_mean','sex_mean', 'smoking_mean', 'follow_up_time_mean']]
    # y = df['diagnosis']
    X = df
    y = df
    return df, X, y

@st.cache()
def train_model(X, y):
    """This function trains the model and return the model and model score"""
    # Create the model
    # model = DecisionTreeClassifier(
    #         ccp_alpha=0.0, class_weight=None, criterion='entropy',
    #         max_depth=4, max_features=None, max_leaf_nodes=None,
    #         min_impurity_decrease=0.0, min_samples_leaf=1, 
    #         min_samples_split=2, min_weight_fraction_leaf=0.0,
    #         random_state=42, splitter='best'
    #     )
    # # Fit the data on model
    # model.fit(X, y)
    # # Get the model score
    # score = model.score(X, y)

    # # Return the values
    # return model, score
    pass
import pickle
import sklearn
def predict(X, y, features):
    #load model
    model = pickle.load(open("./model.pkl","rb"))

    #preprocess data
    features[9] = 1 if features[9]=="Male" else 0
    # do prediction
    prediction = model.predict_proba(np.array(features).reshape(1, -1))
    # get outcome
    outcome = np.argmax(prediction[0])
    # return outcome and probability
    return outcome, prediction[0][outcome]

    # return prediction, score
    # return 1, 0.5
