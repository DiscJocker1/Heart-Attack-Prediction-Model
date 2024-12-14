"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Machine Learning & AI Algorithms</b> for the Heart Attack Prediction.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Health Biometric values:")

    # Take input of features from the user.
    rad = st.slider("Radius", float(df["radius_mean"].min()), float(df["radius_mean"].max()))
    tex = st.slider("Texture", float(df["texture_mean"].min()), float(df["texture_mean"].max()))
    per = st.slider("Perimeter", float(df["perimeter_mean"].min()), float(df["perimeter_mean"].max()))
    are = st.slider("Area", float(df["area_mean"].min()), float(df["area_mean"].max()))
    smo = st.slider("Smoothness", float(df["smoothness_mean"].min()), float(df["smoothness_mean"].max()))
    com = st.slider("Compactness", float(df["compactness_mean"].min()), float(df["compactness_mean"].max()))
    con = st.slider("Concavity", float(df["compactness_mean"].min()), float(df["compactness_mean"].max()))
    sym = st.slider("Symmetry", float(df["symmetry_mean"].min()), float(df["symmetry_mean"].max()))
    fad = st.slider("Fractal Dimension", float(df["fractal_dimension_mean"].min()), float(df["fractal_dimension_mean"].max()))
       


    rad = st.slider("Age", float(df["radius_mean"].min()), float(df["radius_mean"].max()))
    tex = st.slider("Texture", float(df["texture_mean"].min()), float(df["texture_mean"].max()))
    per = st.slider("Perimeter", float(df["perimeter_mean"].min()), float(df["perimeter_mean"].max()))
    are = st.slider("Area", float(df["area_mean"].min()), float(df["area_mean"].max()))
    smo = st.slider("Smoothness", float(df["smoothness_mean"].min()), float(df["smoothness_mean"].max()))
    com = st.slider("Compactness", float(df["compactness_mean"].min()), float(df["compactness_mean"].max()))
    con = st.slider("Concavity", float(df["compactness_mean"].min()), float(df["compactness_mean"].max()))
    sym = st.slider("Symmetry", float(df["symmetry_mean"].min()), float(df["symmetry_mean"].max()))
    fad = st.slider("Fractal Dimension", float(df["fractal_dimension_mean"].min()), float(df["fractal_dimension_mean"].max()))
       



    # Age: Slider for numerical value
    st.write("""
    ### Age
    This model utilizes the individual's age as part of the identification process. The age range in this dataset is between 45 and 93 years.
    """)
    age = st.slider("Age", 45, 93, 60)

    # Anaemia: Checkbox for binary yes/no (0 or 1)
    st.write("""
    ### Anaemia
    Anaemia is a condition in which the body does not have enough healthy red blood cells. It is recorded as 0 (no) or 1 (yes).
    """)
    anaemia = st.selectbox("Anaemia", [0, 1], index=0)  # Default to 0 (no)

    # Creatinine Phosphokinase (CPK): Slider for numerical value
    st.write("""
    ### Creatinine Phosphokinase (CPK)
    Creatinine Phosphokinase (CPK) is an enzyme found in the heart, brain, and skeletal muscles. Elevated levels can indicate damage to these tissues.
    """)
    cpk = st.slider("Creatinine Phosphokinase", 0, 6000, 100)  

    # Diabetes: Checkbox for binary yes/no (0 or 1)
    st.write("""
    ### Diabetes
    Diabetes is a health condition that affects how your body turns food into energy. It is recorded as `0` (no) or `1` (yes).
    """)
    diabetes = st.selectbox("Diabetes", [0, 1], index=0)  # Default to 0 (no)

    # Ejection Fraction (EF): Slider for percentage (0-100)
    st.write("""
    ### Ejection Fraction (EF)
    Ejection Fraction is a percentage that measures how much blood the left ventricle of the heart pumps out with each contraction. It helps assess heart function.
    """)
    ef = st.slider("Ejection Fraction (EF)", 0, 100, 50)  # Example range

    # High Blood Pressure: Checkbox for binary yes/no (0 or 1)
    st.write("""
    ### High Blood Pressure
    High Blood Pressure occurs when the pressure in your blood vessels is higher than normal. It is recorded as `0` (no) or `1` (yes).
    """)
    high_blood_pressure = st.selectbox("High Blood Pressure", [0, 1], index=0)  # Default to 0 (no)

    # Platelets: Slider for numerical value
    st.write("""
    ### Platelets
    Platelets are small blood cells that help prevent bleeding by forming clots. The normal platelet count is typically between 150,000 and 450,000 per microliter of blood.
    """)
    platelets = st.slider("Platelets", 0, 800000, 200000)  # Example range

    # Serum Creatinine: Slider for numerical value
    st.write("""
    ### Serum Creatinine
    Serum Creatinine is a waste product filtered out of the blood by the kidneys. High levels can indicate poor kidney function.
    """)
    serum_creatinine = st.slider("Serum Creatinine", 0.5, 10.0, 1.0)  # Example range

    # Serum Sodium: Slider for numerical value
    st.write("""
    ### Serum Sodium
    Serum Sodium levels indicate the amount of sodium in the blood, which is important for maintaining fluid balance and proper muscle and nerve function.
    """)
    serum_sodium = st.slider("Serum Sodium", 100, 160, 140)  # Example range

    # Sex: Selectbox for Male/Female
    st.write("""
    ### Sex
    This feature indicates the sex of the patient, recorded as either `Male` or `Female`.
    """)
    sex = st.selectbox("Sex", ['Male', 'Female'])

    # Smoking: Checkbox for binary yes/no (0 or 1)
    st.write("""
    ### Smoking
    Smoking is a habit that can lead to various health complications. It is recorded as `0` (no) or `1` (yes).
    """)
    smoking = st.selectbox("Smoking", [0, 1], index=0)  # Default to 0 (no)

    # Follow-up time in hospital: Slider for numerical value (time in days)
    st.write("""
    ### Follow-up Time in Hospital
    This feature indicates the patient's follow-up time in hospital after a cardiac event. The value is given in days.
    """)
    follow_up_time = st.slider("Follow-up Time in Hospital (days)", 1, 1000, 200)  # Example range

    # Display all the inputs (for debugging or further use)
    st.write(f"**Age**: {age}")
    st.write(f"**Anaemia**: {anaemia}")
    st.write(f"**Creatinine Phosphokinase**: {cpk}")
    st.write(f"**Diabetes**: {diabetes}")
    st.write(f"**Ejection Fraction (EF)**: {ef}")
    st.write(f"**High Blood Pressure**: {high_blood_pressure}")
    st.write(f"**Platelets**: {platelets}")
    st.write(f"**Serum Creatinine**: {serum_creatinine}")
    st.write(f"**Serum Sodium**: {serum_sodium}")
    st.write(f"**Sex**: {sex}")
    st.write(f"**Smoking**: {smoking}")
    st.write(f"**Follow-up Time**: {follow_up_time} days")


    # Create a list to store all the features
    features = [rad,tex,per,are,smo,com,con,sym,fad]

    # Create a button to predict
    if st.button("Predict!"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        st.info("Prediction was sucessful...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is at risk of a Heart Attack!!")
        else:
            st.success("The person is not at risk of a Heart Attack")

        # Print teh score of the model 
        st.write("The model has an accuracy of ", round((score*100)),"%")