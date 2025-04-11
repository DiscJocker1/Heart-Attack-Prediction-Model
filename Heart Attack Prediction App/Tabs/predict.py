# import streamlit as st
# import numpy as np
import pickle


# import streamlit as st
# import torch
# import numpy as np
# import pandas as pd

# # Load the trained model
# model = torch.load("DLmodel96.pth", map_location=torch.device("cpu"))
# model.eval()

# # Define the feature names
# FEATURES = ['Age', 'Gender', 'Heart rate', 'Systolic blood pressure',
#             'Diastolic blood pressure', 'Blood sugar', 'CK-MB', 'Troponin']

# # Title & Description
# st.title("🔍 Heart Attack Prediction")
# st.markdown("""
# **Enter patient details using the sliders below.**
# The model will assess the risk of a heart attack based on medical parameters.
# """)

# # Sidebar Inputs with Help Text
# st.sidebar.header("Patient Details")
# user_data = {}

# user_data['Age'] = st.sidebar.slider("Age", min_value=18, max_value=100, value=50, help="Patient's age in years.")
# user_data['Gender'] = st.sidebar.radio("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female", help="0: Female, 1: Male")
# user_data['Heart rate'] = st.sidebar.slider("Heart Rate (bpm)", min_value=40, max_value=180, value=75, help="Resting heart rate in beats per minute.")
# user_data['Systolic blood pressure'] = st.sidebar.slider("Systolic BP (mmHg)", min_value=80, max_value=200, value=120, help="Pressure when the heart beats.")
# user_data['Diastolic blood pressure'] = st.sidebar.slider("Diastolic BP (mmHg)", min_value=50, max_value=130, value=80, help="Pressure when the heart is at rest.")
# user_data['Blood sugar'] = st.sidebar.slider("Blood Sugar (mg/dL)", min_value=50, max_value=300, value=100, help="Fasting blood glucose level.")
# user_data['CK-MB'] = st.sidebar.slider("CK-MB (ng/mL)", min_value=0.0, max_value=100.0, value=2.5, help="Creatine Kinase-MB, a heart attack marker.")
# user_data['Troponin'] = st.sidebar.slider("Troponin (ng/mL)", min_value=0.0, max_value=50.0, value=0.03, help="Cardiac troponin level, an indicator of heart injury.")

# # Convert input to dataframe
# input_df = pd.DataFrame([user_data])

# # Convert to tensor (no scaling)
# input_tensor = torch.FloatTensor(input_df.values)

# # Prediction
# with torch.no_grad():
#     output = model(input_tensor)
#     probability = torch.sigmoid(output).item()

# # Classification threshold (optimized)
# THRESHOLD = 0.5  # Adjust this based on best-performing threshold
# prediction = 1 if probability > THRESHOLD else 0

# # Display results
# st.subheader("Prediction Result")
# if prediction == 1:
#     st.error("⚠ **High Risk:** The model predicts a possible heart attack.")
# else:
#     st.success("✅ **Low Risk:** The model does not predict a heart attack.")

# st.subheader("Risk Probability")
# st.info(f"🔹 **Heart Attack Risk Probability: {probability:.4f}**")

# # Interpretation
# st.subheader("🩺 Medical Insights")
# if probability > 0.8:
#     st.warning("🚨 **Very High Risk!** Seek medical attention immediately.")
# elif probability > 0.6:
#     st.warning("⚠ **Moderate to High Risk:** Consult a doctor for further evaluation.")
# elif probability > 0.4:
#     st.info("🔹 **Mild Risk:** Maintain a healthy lifestyle and monitor your health.")
# else:
#     st.success("✅ **Low Risk:** Keep up your heart-healthy habits!")


# import streamlit as st
# import numpy as np
# import pickle

# with open("DLmodel96.pkl", "rb") as model_file:  # Ensure correct model file
#     model = pickle.load(model_file)

# def app(df, X, y):
#     """Heart Attack Prediction Page"""

#     st.title("🩺 Heart Attack Prediction")
#     st.write("This AI model predicts heart attack risk based on health metrics.")

#     # User inputs with detailed descriptions. Age	Gender	Heart rate	Systolic blood pressure	Diastolic blood pressure	Blood sugar	CK-MB	Troponin	Result
#     Age = st.slider(
#         "Age", 14, 103, 58, 
#         help="Your age in years. **Older age increases heart disease risk.**"
#     )
    
#     Gender = st.selectbox(
#         "Sex (0 = Female, 1 = Male)", [0, 1], 
#         help="Sex can influence heart disease risk. **Men (1) generally have a higher risk than women (0).**"
#     )

#     Heart_Rate = st.selectbox(
#         "Anaemia (0 = No, 1 = Yes)", [0, 1], 
#         help="Anaemia is a condition where you have fewer red blood cells, reducing oxygen delivery to tissues. **Normal: No anaemia (0).**"
#     )

#     cpk = st.slider(
#         "Creatinine Phosphokinase (CPK)", 0, 6000, 100, 
#         help="CPK is an enzyme released when the heart or muscles are damaged. **Normal: 10-120 U/L. High CPK (>200) may indicate muscle or heart damage.**"
#     )

#     diabetes = st.selectbox(
#         "Diabetes (0 = No, 1 = Yes)", [0, 1], 
#         help="Diabetes increases the risk of heart disease by causing high blood sugar levels. **Normal: No diabetes (0).**"
#     )

#     ef = st.slider(
#         "Ejection Fraction (EF %)", 0, 100, 50, 
#         help="EF measures how well your heart pumps blood per beat. **Normal: 55-70%.** **Below 40% may indicate heart failure.**"
#     )

#     high_bp = st.selectbox(
#         "High Blood Pressure (0 = No, 1 = Yes)", [0, 1], 
#         help="High blood pressure (hypertension) puts extra strain on the heart. **Normal: <120/80 mmHg.**"
#     )

#     platelets = st.slider(
#         "Platelets", 0, 850000, 250000, 
#         help="Platelets help with blood clotting. **Normal: 150,000 - 450,000 per µL.** **Too low (<150,000) or too high (>450,000) can indicate issues.**"
#     )

#     serum_creatinine = st.slider(
#         "Serum Creatinine", 0.1, 10.0, 1.0, 
#         help="Creatinine is a waste product from muscles, filtered by the kidneys. **Normal: 0.6 - 1.3 mg/dL.** **High levels (>1.5) may indicate kidney issues.**"
#     )

#     serum_sodium = st.slider(
#         "Serum Sodium", 100, 150, 137, 
#         help="Sodium helps regulate blood pressure and fluid balance. **Normal: 135 - 145 mEq/L.** **Low (<135) or high (>145) levels can indicate problems.**"
#     )

#     sex = st.selectbox(
#         "Sex (0 = Female, 1 = Male)", [0, 1], 
#         help="Sex can influence heart disease risk. **Men (1) generally have a higher risk than women (0).**"
#     )

#     smoking = st.selectbox(
#         "Smoking (0 = No, 1 = Yes)", [0, 1], 
#         help="Smoking damages blood vessels and increases heart disease risk. **Normal: Non-smoker (0).**"
#     )

#     time = st.slider(
#         "Follow-up Time (Days)", 1, 300, 130, 
#         help="Number of days since the first observation in the dataset."
#     )

#     # Collect input features
#     features = np.array([[age, anaemia, cpk, diabetes, ef, high_bp, platelets, serum_creatinine, serum_sodium, sex, smoking, time]])

#     # 🔥 Scale the user input using the trained scaler
#     features_scaled = scaler.transform(features)

#     if st.button("Predict!"):
#         prediction = model.predict(features_scaled)[0]
#         confidence = model.predict_proba(features_scaled)[0][prediction]

#         if prediction == 1:
#             st.error(f"🚨 High risk of heart attack! Confidence: {confidence:.2%}")
#         else:
#             st.success(f"✅ Low risk of heart attack. Confidence: {confidence:.2%}")

import streamlit as st
import numpy as np
import torch
import pickle
import time

def show_animated_heart(confidence):
    import streamlit.components.v1 as components

    # Decide heart color based on risk
    if confidence < 0.33:
        heart_color = "#2ecc71"  # Green
    elif confidence < 0.66:
        heart_color = "#f1c40f"  # Yellow
    else:
        heart_color = "#e74c3c"  # Red

    heart_html = f"""
    <style>
        .pulse-heart {{
            margin: auto;
            position: relative;
            width: 100px;
            height: 90px;
        }}

        .pulse-heart::before,
        .pulse-heart::after {{
            content: "";
            position: absolute;
            top: 0;
            width: 100px;
            height: 150px;
            background: {heart_color};
            border-radius: 50px 50px 0 0;
        }}

        .pulse-heart::before {{
            left: 50px;
            transform: rotate(-45deg);
            transform-origin: 0 100%;
        }}

        .pulse-heart::after {{
            left: 0;
            transform: rotate(45deg);
            transform-origin: 100% 100%;
        }}

        .pulse {{
            animation: pulse 1s infinite;
        }}

        @keyframes pulse {{
            0% {{
                transform: scale(1);
            }}
            50% {{
                transform: scale(1.1);
            }}
            100% {{
                transform: scale(1);
            }}
        }}
    </style>

    <div class="pulse-heart pulse"></div>
    """

    components.html(heart_html, height=150)



def app(df, X, y):
    """Heart Attack Prediction Page"""

    st.title("🩺 Heart Attack Prediction")
    st.write("This AI model predicts heart attack risk based on health metrics.")

    # User inputs with detailed descriptions
    # age = st.slider("Age", 0, 100, 50, help="Your age in years.")
    age = st.slider(
    "Age (Years)", 
    0,100,50,
    help="""**Cardiovascular Risk Factor**  
    - **<45 years**: Low baseline risk  
    - **45-65 years**: Moderate risk (atherosclerosis progression)  
    - **>65 years**: High risk (arterial stiffness ↑, vascular compliance ↓)  
    **Why it matters**: Aging increases arterial plaque buildup and reduces heart elasticity.  
    **Clinical Note**: Annual cardiac screening recommended after 40."""
)
    gender = st.selectbox("Gender (0 = Female, 1 = Male)", [0, 1], help="Gender of the patient.")
    # gender = st.selectbox(
    # "Biological Sex", 
    # [0, 1],
    # format_func=lambda x: "Female" if x == 0 else "Male",
    # help="""**Hormonal Influence on CVD Risk**:  
    # - **Female (0)**: Estrogen provides pre-menopausal protection (avg. MI onset ~10 years later than males)  
    # - **Male (1)**: Higher baseline risk (androgen-driven LDL ↑)  
    # **Post-Menopause**: Female risk approaches male levels (estrogen ↓)  
    # **Key Stat**: Males have 2-3× higher age-adjusted CAD mortality."""

    # heart_rate = st.slider("Heart Rate", 40, 200, 70, help="Heart rate in beats per minute.")
    heart_rate = st.slider(
    "Heart Rate (bpm)", 
    40, 200, 70,
    help="""**Autonomic Nervous System Indicator**  
    **Normal**: 60-100 bpm (sinus rhythm)  
    **Bradycardia**: <60 bpm (athletes: normal; others: check for hypothyroidism/β-blocker use)  
    **Tachycardia**: >100 bpm (stress/anemia/hyperthyroidism)  
    **Danger Zones**:  
    - <40 bpm: Risk of syncope/ischemia  
    - >140 bpm: Cardiac output ↓, O2 demand ↑  
    **Prognosis**: Every 10 bpm ↑ → 10-20% CVD mortality ↑"""
)
    # systolic_bp = st.slider("Systolic Blood Pressure", 80, 200, 120, help="Systolic blood pressure in mmHg.")
    # diastolic_bp = st.slider("Diastolic Blood Pressure", 40, 120, 80, help="Diastolic blood pressure in mmHg.")
    systolic_bp = st.slider(
    "Systolic BP (mmHg)", 
    80, 200, 120,
    help="""**Vascular Resistance Metric**  
    **Classification**:  
    - Optimal: <120  
    - Elevated: 120-129  
    - Stage 1 HTN: 130-139  
    - Stage 2 HTN: ≥140  
    - Crisis: >180 (immediate intervention needed)  
    **Pathology**: Sustained >140 mmHg → endothelial damage → atherosclerosis acceleration"""
)

    diastolic_bp = st.slider(
        "Diastolic BP (mmHg)", 
        40, 120, 80,
        help="""**Coronary Perfusion Pressure**  
        **Critical Thresholds**:  
        - <60 mmHg: Coronary filling compromised  
        - >90 mmHg: Left ventricular hypertrophy risk ↑  
        **Pulse Pressure**: (Systolic - Diastolic) >60 mmHg → arterial stiffness marker"""
    )
    blood_sugar = st.selectbox("Blood Sugar (>120 = 1, <=120 = 0)", [0, 1], help="Blood sugar level (mg/dL). Diabetes Diagnostic -> Normal : <100, Prediabetes: 100-125, Diabetes: ≥126, Hyperglycemia Effects: Endothelial dysfunction + Oxidative stress ↑ + HbA1c >6.5% → 2× CVD risk ")
#     blood_sugar = st.slider(
#     "Blood Sugar level (mg/dL)", 
#     50, 400, 95,
#     help="""**Diabetes Diagnostic**  
#     **Normal**: <100  
#     **Prediabetes**: 100-125  
#     **Diabetes**: ≥126  
#     **Hyperglycemia Effects**:  
#     - Endothelial dysfunction  
#     - Oxidative stress ↑  
#     - HbA1c >6.5% → 2× CVD risk"""
# )
    # ck_mb = st.slider("CK-MB", 0, 1000, 10, help="CK-MB enzyme level.")
    # troponin = st.slider("Troponin", 0, 100, 0, help="Troponin level.")
    ck_mb = st.slider(
        "CK-MB Mass (μg/L)", 
        0, 1000, 10,
        help="""**Cardiac-Specific Isoenzyme**  
        **Normal**: <5 μg/L (or <5% of total CK)  
        **Peak**: 12-24h post-MI (vs. troponin 12h)  
        **Clinical Use**:  
        - Re-infarction detection (falls faster than troponin)  
        - Post-PCI monitoring"""
    )

    troponin = st.slider(
    "High-Sensitivity Troponin (ng/L)", 
    0, 100, 0,
    help="""**Gold Standard for Myocardial Injury**  
    **Normal**: <14 ng/L (99th percentile)  
    **Gray Zone**: 14-52 ng/L → repeat testing needed  
    **AMI Diagnostic**: >52 ng/L + rising pattern  
    **Half-life**: 7-10 days (vs. CK-MB 24h)  
    **Specificity**: 95% for cardiac vs skeletal muscle"""
)

    # Collect input features
    features = np.array([[age, gender, heart_rate, systolic_bp, diastolic_bp, blood_sugar, ck_mb, troponin]])

    # # Load model
    # model_path = st.text_input("Enter model path (.pth):", "DLmodel96.pth")

    # try:
    #     model = load_model(model_path)

    #     if st.button("Predict!"):
    #         probs = predict_pytorch(model, features)
    #         prediction = (probs > 0.5).astype(int)[0][0]  # Convert probabilities to binary prediction
    #         confidence = probs[0][0]  # Get the probability for the positive class

    #         if prediction == 1:
    #             st.error(f"🚨 High risk of heart attack! Confidence: {confidence:.2%}")
    #         else:
    #             st.success(f"✅ Low risk of heart attack. Confidence: {confidence:.2%}")

    # except Exception as e:
    #     st.error(f"Error: {str(e)}")


    if st.button("Predict!"):
        with open("DLmodel96.pkl", "rb") as model_file:  # Ensure correct model file
            model = pickle.load(model_file)
            print(model)
            
            features = torch.from_numpy(features).type(torch.float32)
            print(features)
            prediction = model(features)[0]
            # probs = torch.sigmoid(prediction).numpy()
            probs = torch.sigmoid(prediction).detach().numpy()

            print(probs)
            # confidence = model.predict_proba(features)[0][prediction]

            # if prediction == 1:
            #     st.error(f"🚨 High risk of heart attack! Confidence: ")#{confidence:.2%}")
            # else:
            #     st.success(f"✅ Low risk of heart attack. Confidence: ")#{confidence:.2%}")

            # if prediction == 1:
            #     st.error(f"🚨 High risk of heart attack! Confidence: {probs[0]:.2%}")
            # else:
            #     st.success(f"✅ Low risk of heart attack. Confidence: {probs[0]:.2%}")

                # Raw prediction score (logits → sigmoid → prob)
            probs = torch.sigmoid(prediction)
            confidence = probs.item()


            # # 🎯 Pulse heart animation before showing result
            # show_animated_heart()
            # time.sleep(1.5)  # Let the heart pulse before revealing result
            show_animated_heart(confidence)

            time.sleep(1.5)




            if confidence >= 0.5:
                st.error(f"🚨 High risk of heart attack! Confidence: {confidence * 100:.2f}%")
                prediction = 1
            else:
                st.success(f"✅ Low risk of heart attack. Confidence: {confidence * 100:.2f}%")
                prediction = 0