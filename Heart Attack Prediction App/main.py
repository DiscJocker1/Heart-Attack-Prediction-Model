# Import necessary Python modules
import streamlit as st

st.set_page_config(
    page_title='Heart Attack Prediction',
    layout='wide',
    initial_sidebar_state='auto'
)
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, f1_score
import pandas as pd
import numpy as np

class Attention(nn.Module):
    def __init__(self, hidden_dim):
        super(Attention, self).__init__()
        self.attn = nn.Linear(hidden_dim * 2, 1)

    def forward(self, lstm_output):
        attn_weights = torch.softmax(self.attn(lstm_output), dim=1)
        context = torch.sum(attn_weights * lstm_output, dim=1)
        return context

# Custom Focal Loss
class FocalLoss(nn.Module):
    def __init__(self, alpha=0.3, gamma=2):
        super(FocalLoss, self).__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.bce = nn.BCEWithLogitsLoss(reduction='none')

    def forward(self, logits, targets):
        bce_loss = self.bce(logits, targets)
        p_t = torch.exp(-bce_loss)
        focal_loss = self.alpha * (1 - p_t) ** self.gamma * bce_loss
        return focal_loss.mean()

# Optimized Model
class HeartAttackPredictor(nn.Module):
    def __init__(self, input_size):
        super(HeartAttackPredictor, self).__init__()
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=640, num_layers=4, batch_first=True, bidirectional=True)
        self.attention = Attention(640)
        self.norm = nn.LayerNorm(1280)
        self.fc1 = nn.Linear(1280, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 1)

        self.dropout = nn.Dropout(0.4)
        self.batchnorm1 = nn.BatchNorm1d(512)
        self.batchnorm2 = nn.BatchNorm1d(256)
        self.batchnorm3 = nn.BatchNorm1d(128)

    def forward(self, x):
        x = x.unsqueeze(1)
        lstm_out, _ = self.lstm(x)
        context = self.attention(lstm_out)
        x = self.norm(context)

        x = self.dropout(torch.relu(self.batchnorm1(self.fc1(x))))
        x = self.dropout(torch.relu(self.batchnorm2(self.fc2(x))))
        x = self.dropout(torch.relu(self.batchnorm3(self.fc3(x))))
        x = self.fc4(x)  # No sigmoid, handled by loss function
        return x

# # Configure the app
# st.set_page_config(
#     page_title='Heart Attack Prediction',
#     layout='wide',
#     initial_sidebar_state='auto'
# )

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, data, predict, visualise, about, background, myChatbotV2, info, modelVisuals, ecg_analysis, cardiac_events, significance

# ✅ Define Tabs dictionary FIRST
Tabs = {
    "Home": home,
    "About": about,
    "Background": background,
    "Cardiac Events": cardiac_events,
    "Significance": significance,
    "Data Info": data,
    "Heart Attack Prediction": predict,
    "ECG Analysis": ecg_analysis,
    "myChatbotV2": myChatbotV2,
    "Visualisation": visualise,
    "Model Insights & Explainability": modelVisuals,
    "Heart Health Resources, Tips + Info!": info
}

# Create a sidebar
# st.sidebar.title("Navigation")

# Create radio option to select the page
# page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Load the dataset (only once)
df, X, y = load_data()

# if page in ["Prediction", "Visualisation"]:
#     # Tabs[page].app(df, X, y)  # Only these need df, X, y
#     Tabs[page].app()  # Only these need df, X, y

# elif page == "Data Info":
#     Tabs[page].app(df)  # Only Data Info needs df
# else:
#     Tabs[page].app()  # Other pages (Home, About, Background, Chatbot, Model Visuals) require no arguments

# Corrected Logic: Call the appropriate app function based on the selected page
# if page in ["Prediction", "Visualisation"]:
#     Tabs[page].app(df, X, y)  # These need df, X, y

# elif page == "Data Info":
#     Tabs[page].app(df)  # Only Data Info needs df

# else:
#     Tabs[page].app()  # Other pages (Home, About, etc.) don't need any arguments


# Create sidebar navigation - SINGLE VERSION
# Configure the app
# st.set_page_config(
#     page_title='Heart Attack Prediction',
#     layout='wide',
#     initial_sidebar_state='auto'
# )

# Create sidebar navigation
with st.sidebar:
    st.title("Navigation")
    page = st.radio(
        "Pages",
        list(Tabs.keys()),
        key="main_navigation_radio"  # Unique key added here
    )

# Load data only for pages that need it
if page in ["Heart Attack Prediction", "Visualisation", "Data Info"]:
    df, X, y = load_data()

# Route to selected page
if page in ["Heart Attack Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif page == "Data Info":
    Tabs[page].app(df)
else:
    Tabs[page].app()


#cd Heart-Attack-Prediction-Model/Heart Attack Prediction App
#source venv/bin/activate         
#streamlit run main.py
# python -m venv . venv