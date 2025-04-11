# # import streamlit as st
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# # import numpy as np
# # import pandas as pd
# # import pickle
# # from sklearn.metrics import confusion_matrix, classification_report

# # # Load the trained model
# # with open("DLmodel96.pkl", "rb") as model_file:
# #     model = pickle.load(model_file)

# # def app():
# #     """This function creates the Model Insights & Explainability page"""
# #     st.title("📊 Model Insights & Explainability")
# #     st.write("Understand how the AI model makes predictions.")
    
# #     # Feature Importance
# #     st.header("🔍 Feature Importance")
# #     if hasattr(model, "feature_importances_"):
# #         feature_names = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction', 
# #                          'high_blood_pressure', 'platelets', 'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']
# #         feature_importance = model.feature_importances_
# #         df_importance = pd.DataFrame({"Feature": feature_names, "Importance": feature_importance})
# #         df_importance = df_importance.sort_values(by="Importance", ascending=False)
        
# #         fig, ax = plt.subplots()
# #         sns.barplot(x=df_importance["Importance"], y=df_importance["Feature"], ax=ax, palette="Blues_r")
# #         ax.set_title("Feature Importance in Prediction Model")
# #         st.pyplot(fig)
# #     else:
# #         st.warning("Feature importance not available for this model.")
    
# #     # Model Performance Metrics
# #     st.header("📈 Model Performance")
# #     st.write("See how well the model performs on test data.")
    
# #     # Load test data
# #     test_data = pd.read_csv("CardiologyScienceFairDataset.csv")  # Using the correct dataset
# #     X_test = test_data.drop(columns=["DEATH_EVENT"])
# #     y_test = test_data["DEATH_EVENT"]
    
# #     # Scale X_test before prediction
# #     X_test_scaled = scaler.transform(X_test)

# #     y_pred = model.predict(X_test_scaled)
# #     cm = confusion_matrix(y_test, y_pred)
    
# #     fig, ax = plt.subplots()
# #     sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Heart Failure', 'Heart Failure'],
# #                 yticklabels=['No Heart Failure', 'Heart Failure'], ax=ax)
# #     ax.set_xlabel("Predicted")
# #     ax.set_ylabel("Actual")
# #     ax.set_title("Confusion Matrix")
# #     st.pyplot(fig)
    
# #     # Classification Report
# #     report = classification_report(y_test, y_pred, output_dict=True)
# #     df_report = pd.DataFrame(report).transpose()
# #     st.dataframe(df_report)

# import streamlit as st
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import pandas as pd
# import pickle
# from sklearn.metrics import confusion_matrix, classification_report
# import torch
# from sklearn.preprocessing import StandardScaler

# # Load the trained deep learning model
# with open("DLmodel96.pkl", "rb") as model_file:
#     model = pickle.load(model_file)

# # Load the new dataset
# medical_data = pd.read_csv("Medicaldataset.csv")

# # Assuming the model expects specific features (X) and target (y) based on the new dataset
# # Adjust these features based on the columns in your dataset
# X = medical_data.drop(columns=["Result"])  # Replace with your target column if necessary
# y = medical_data["Result"]  # Assuming "DEATH_EVENT" is your target column

# # Standardize or scale the input features if necessary
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# def app():
#     """This function creates the Model Insights & Explainability page"""
#     st.title("📊 Model Insights & Explainability")
#     st.write("Understand how the AI model makes predictions.")
    
#     # Feature Importance - Since it's a neural network, we'll visualize using SHAP or similar
#     st.header("🔍 Feature Importance")
#     try:
#         import shap
        
#         # Convert the dataset to a tensor
#         X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
        
#         # Use SHAP for deep learning models
#         background = X_tensor[:100]  # Take a small sample for background dataset
#         explainer = shap.DeepExplainer(model, background)
        
#         # Set check_additivity=False to avoid the sum difference error
#         shap_values = explainer.shap_values(X_tensor[:200], check_additivity=False)  # Explaining the first 200 instances
        
#         # Plot SHAP summary
#         st.set_option('deprecation.showPyplotGlobalUse', False)
#         shap.summary_plot(shap_values[0], X.iloc[:200], show=False)
#         st.pyplot()
        
#     except ImportError:
#         st.warning("SHAP is not installed or model doesn't support SHAP explanation.")
#     except Exception as e:
#         st.warning(f"An error occurred during SHAP explanation: {e}")

    
#     # Model Performance Metrics
#     st.header("📈 Model Performance")
#     st.write("See how well the model performs on test data.")
    
#     # Scale X before prediction
#     X_scaled_test = scaler.transform(X)
    
#     # Make predictions
#     y_pred = model.predict(X_scaled_test)
    
#     # Confusion Matrix
#     cm = confusion_matrix(y, y_pred)
    
#     fig, ax = plt.subplots()
#     sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Heart Attack', 'Heart Attack'],
#                 yticklabels=['No Heart Attack', 'Heart Attack'], ax=ax)
#     ax.set_xlabel("Predicted")
#     ax.set_ylabel("Actual")
#     ax.set_title("Confusion Matrix")
#     st.pyplot(fig)
    
#     # Classification Report
#     report = classification_report(y, y_pred, output_dict=True)
#     df_report = pd.DataFrame(report).transpose()
#     st.dataframe(df_report)
