"""This modules contains data about my project"""

import streamlit as st

# COLOURED TEXT:
#     temperature = "-10"

#     st.write(f"temprature: :blue[{temperature}]")

# st.markdown('Streamlit is **_really_ cool**.')
# st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
# st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

def app():
    """This function create the background page"""
    
    # Add title to the home page
    st.title("Background information")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:23px;">
            Background Information for my project, the problems that are being solved by my solution, and why i did this. Its kind of cool 👍🏼
        </p>
    """, unsafe_allow_html=True)

    st.image("Heart Attack Img.jpg")
    
    st.markdown(
    """<p style="font-size:20px;">
        A heart attack occurs when an artery that sends blood and oxygen to the heart is blocked. Fatty, cholesterol-containing deposits build up over time, forming plaques in the heart's arteries. If a plaque ruptures, a blood clot can form. The clot can block arteries, causing a heart attack. During a heart attack, a lack of blood flow causes the tissue in the heart muscle to die.

Common heart attack symptoms include:

- Chest pain that may feel like pressure, tightness, pain, squeezing or aching
- Pain or discomfort that spreads to the shoulder, arm, back, neck, jaw, teeth or sometimes the upper belly
- Cold sweat
- Fatigue
- Heartburn or indigestion
- Lightheadedness or sudden dizziness
- Nausea
- Shortness of breath

Risk Factors?

- Age. Men age 45 and older and women age 55 and older are more likely to have a heart attack than are younger men and women.
- Tobacco use. This includes smoking and long-term exposure to secondhand smoke. If you smoke, quit.
- High blood pressure. Over time, high blood pressure can damage arteries that lead to the heart. High blood pressure that occurs with other conditions, such as obesity, high cholesterol or diabetes, increases the risk even more.
- High cholesterol or triglycerides. A high level of low-density lipoprotein (LDL) cholesterol (the "bad" cholesterol) is most likely to narrow arteries. A high level of certain blood fats called triglycerides also increases heart attack risk. Your heart attack risk may drop if levels of high-density lipoprotein (HDL) cholesterol — the "good" cholesterol — are in the standard range.
- Obesity. Obesity is linked with high blood pressure, diabetes, high levels of triglycerides and bad cholesterol, and low levels of good cholesterol.
- Diabetes. Blood sugar rises when the body doesn't make a hormone called insulin or can't use it correctly. High blood sugar increases the risk of a heart attack.
- Metabolic syndrome. This is a combination of at least three of the following things: enlarged waist (central obesity), high blood pressure, low good cholesterol, high triglycerides and high blood sugar. Having metabolic syndrome makes you twice as likely to develop heart disease than if you don't have it.
- Family history of heart attacks. If a brother, sister, parent or grandparent had an early heart attack (by age 55 for males and by age 65 for females), you might be at increased risk.
- Not enough exercise. A lack of physical activity (sedentary lifestyle) is linked to a higher risk of heart attacks. Regular exercise improves heart health.
- Unhealthy diet. A diet high in sugars, animal fats, processed foods, trans fats and salt increases the risk of heart attacks. Eat plenty of fruits, vegetables, fiber and healthy oils.
- Stress. Emotional stress, such as extreme anger, may increase the risk of a heart attack.
- Illegal drug use. Cocaine and amphetamines are stimulants. They can trigger a coronary artery spasm that can cause a heart attack.
- A history of preeclampsia. This condition causes high blood pressure during pregnancy. It increases the lifetime risk of heart disease.
- An autoimmune condition. Having a condition such as rheumatoid arthritis or lupus can increase the risk of a heart attack.

Why is prediction important? An improved ability to predict risk of heart attack can reveal who will benefit most from preventive strategies, such as increased exercise, a healthier diet, and quitting smoking

How do we currently identify heart attacks?

Currently we wait for it to occur. This is why the big step from that to my model is huge.

- Clinical Assessment and Symptoms Recognition:
    - Healthcare professionals typically evaluate a patient's medical history and symptoms. Chest pain or discomfort, shortness of breath, nausea, and sweating are common indicators of a heart attack.
    - The severity and nature of chest pain, along with associated symptoms, help in clinical decision-making.
- Electrocardiogram (ECG or EKG):
    - An electrocardiogram is a standard diagnostic test used to assess the electrical activity of the heart. Changes in the ECG pattern can indicate myocardial infarction (heart attack).
    - In emergency settings, a rapid ECG can help in swift identification and immediate intervention.
- Blood Tests:
    - Cardiac biomarkers, such as troponin and creatine kinase-MB (CK-MB), are measured through blood tests. Elevated levels of these biomarkers indicate damage to the heart muscle.
    - Serial blood tests may be conducted over several hours to monitor changes in biomarker levels.
- Imaging Techniques:
    - Imaging studies like coronary angiography, cardiac MRI, or CT angiography may be employed to visualize the coronary arteries and assess blood flow to the heart.
    - Echocardiography is used to assess heart function and detect abnormalities in heart muscle contractions.

  
    </p>
    """, unsafe_allow_html=True)
    st.markdown(
    """<p style="font-size:22px;">
            How about Cardiac events as a whole? What would switching the scope of study of the project do? Could we now talk about CVDs, Heart Failure, AFib, POTS and more? Not only focusing on the scope of an MI -> Myocardial Infarction/ Heart Attack
        </p>
    """, unsafe_allow_html=True)