import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_curve, auc
from sklearn.model_selection import train_test_split
from web_functions import train_model

def app(df, X, y):
    """This function creates the visualization page"""
    
    # Suppress warnings
    warnings.filterwarnings('ignore')

    # Set the page title
    st.title("📊 Data Visualizations & Model Performance")

    # Debug: Show the columns of the dataframe
    st.write("Dataframe columns:", df.columns)

    # Ensure `y` contains only two unique values (0 and 1) from the 'DEATH_EVENT' column
    if len(df['Result'].unique()) != 2:
        st.error("Target variable `y` is not binary. Please check the dataset.")
        return

    # Check if 'DEATH_EVENT' exists in the dataframe
    if 'Result' not in df.columns:
        st.error("Column 'Result' not found in the dataset. Please check the dataset.")
        return

    # Show a correlation heatmap
    if st.checkbox("Show Correlation Heatmap"):
        st.subheader("🔍 Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
        

    # Show sample class distribution
    if st.checkbox("Show Class Distribution"):
        st.subheader("📌 Class Distribution")
        safe = (df['Result'] == 0).sum()
        prone = (df['Result'] == 1).sum()
        data = [safe, prone]
        labels = ['Safe', 'Prone']
        colors = sns.color_palette('pastel')[0:2]
        fig, ax = plt.subplots()
        ax.pie(data, labels=labels, colors=colors, autopct='%.0f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        st.pyplot(fig)

    # Show Histogram for age distribution
    if st.checkbox("Show Age Distribution"):
        st.subheader("Age Distribution")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.histplot(df['Age'], kde=True, color='blue', bins=20, ax=ax)
        st.pyplot(fig)

    # Show Pairplot for some features
    if st.checkbox("Show Pairplot of Features"):
        st.subheader("Pairplot of Features")
        # sns.pairplot(df[['age', 'serum_creatinine', 'platelets', 'ejection_fraction']])
        sns.pairplot(df[['Age', 'Gender', 'CK-MB', 'Troponin']])
        st.pyplot()

    # Show Violin Plot for Ejection Fraction
    if st.checkbox("Show Violin Plot for Age"):
        st.subheader("Violin Plot for Age")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.violinplot(x='Result', y='Age', data=df, ax=ax)
        st.pyplot(fig)

    # Show Violin Plot for Ejection Fraction
    if st.checkbox("Show Violin Plot for Gender"):
        st.subheader("Violin Plot for Gender")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.violinplot(x='Result', y='Gender', data=df, ax=ax)
        st.pyplot(fig)

    # Show ROC Curve
    if st.checkbox("Show ROC Curve"):
        st.subheader("Receiver Operating Characteristic Curve (ROC)")
        
        # Split the data into train/test sets
        # mapping = {"positive":1, "negative":0}

        # results=df.replace({"positive":mapping,"negative":mapping})["Result"]
        X_train, X_test, y_train, y_test = train_test_split(X, df["Result"], test_size=0.2, random_state=42)

        # Initialize and train the model
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)

        # Get predicted probabilities for the positive class (1)
        y_pred_prob = model.predict_proba(X_test)[:, 1]

        # Calculate ROC curve
        fpr, tpr, _ = roc_curve(y_test, y_pred_prob, pos_label="positive")
        roc_auc = auc(fpr, tpr)

        # Plot the ROC curve
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
        ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        ax.set(xlabel='False Positive Rate', ylabel='True Positive Rate', title='Receiver Operating Characteristic')
        ax.legend(loc='lower right')
        st.pyplot(fig)

    # Show Feature Importance (Random Forest)
    if st.checkbox("Show Feature Importance"):
        st.subheader("Feature Importance (Random Forest)")
        model = RandomForestClassifier()
        model.fit(X, df['Result'])
        feature_importance = model.feature_importances_

        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(x=X.columns, y=feature_importance, ax=ax)
        ax.set_title('Feature Importance')
        st.pyplot(fig)

    # Show Interactive Scatter Plot for Age vs Serum Creatinine (using Plotly)
    if st.checkbox("Show Interactive Scatter Plot for Age vs Serum Creatinine"):
        st.subheader("Interactive Scatter Plot")
        fig = px.scatter(df, x='Age', y='Gender', color='result', 
                         labels={'Result': 'Result'}, title="Age vs Serum Creatinine")
        st.plotly_chart(fig)

    # Train and show decision tree model
    if st.checkbox("Train and Show Decision Tree Model"):
        try:
            model, score = train_model(X, y['Result'])
            st.success(f"Model Training Completed ✅ | Accuracy: {round(score * 100, 2)}%")
        except Exception as e:
            st.error(f"Error training the model: {e}")
            return

    st.write("Select the checkboxes above to explore visualizations.")
