import streamlit as st
import time

def stream_text(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

def app():
    """This function create the background page"""
    
    # Add title to the home page
    st.title("Cardiac events")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:24px;">
            In background, there was talk about Myocardial Infarctions, but not necessarily on the holistic view of Cardiac Events
        </p>
    """, unsafe_allow_html=True)

    # Set Page Configuration
    # st.set_page_config(page_title="POTS - Cardiac Event App", layout="wide")

    st.title("🩺 Postural Orthostatic Tachycardia Syndrome (POTS)")
    st.image("POTS-Postural-Orthostatic-Tachycardia-Syndrome.png")

    st.markdown("""**What is POTS?**
    Postural Orthostatic Tachycardia Syndrome (POTS) is a **dysautonomic disorder** affecting the autonomic nervous system (ANS), which controls involuntary functions like **heart rate, blood pressure, and circulation**.  
    The defining feature of POTS is an **abnormal heart rate increase of ≥30 bpm upon standing (or ≥40 bpm in teens)** without a significant blood pressure drop.

    While POTS is not a heart disease, it can **mimic cardiac conditions** like heart attacks, making accurate diagnosis essential. Postural Orthostatic Tachycardia Syndrome (POTS) is not a form of cardiovascular disease (CVD), but rather a disorder of the autonomic nervous system that can cause heart rate to increase excessively upon standing. 
""")
    st.markdown("Diagnosis -> POTS is diagnosed based on symptoms, including an excessive increase in heart rate upon standing, and a careful evaluation to rule out other conditions that could cause similar symptoms.")
    if st.markdown("Management -> There's no cure for POTS, but symptoms can be managed through lifestyle changes, such as increasing fluid and salt intake, regular exercise, and sometimes medication. Additionally, there is no prescribed medication for POTS patients that will change their life and stop POTS from affecting them , however there are 2 main medications used for management."):
        st.markdown(" Propranolol (a beta-blocker) and Ivabradine are used to manage symptoms of POTS, particularly to control heart rate. ")
        st.markdown("Propranolol is a beta-blocker (a class of medications that can slow down the heart rate). It's often used as a first-line treatment for POTS to help control the rapid heart rate that can occur when standing. However, beta-blockers like propranolol can also cause fatigue and potentially worsen pre-syncope, which can complicate management. ")
        st.markdown("Ivabradine is a newer medication that works by slowing the heart rate without affecting blood pressure.  It's a selective **If channel blocker** - it specifically targets the heart's pacemaker, reducing heart rate. Many studies have shown that ivabradine can be a good option for controlling orthostatic tachycardia and reducing syncope episodes in POTS patients. Ivabradine can be considered as a second-line treatment in patients with POTS, especially if beta-blockers are not tolerated or ineffective. ")

    if st.markdown("### **⚠️ Common Symptoms of POTS**"):
        st.markdown("""
        ✅ **Sudden rapid heartbeat** (tachycardia) upon standing  
        ✅ **Dizziness or lightheadedness**  
        ✅ **Brain fog & difficulty concentrating**  
        ✅ **Fatigue & exercise intolerance**  
        ✅ **Nausea & digestive issues**  
        ✅ **Cold hands and feet due to blood pooling**  
        ✅ **Excessive sweating or inability to sweat**  
        """)

    st.markdown("### **🩺 Types of POTS**")
    if st.checkbox("🔬 Show Detailed Types of POTS"):
        st.markdown("""
        **1️⃣ Neuropathic POTS (Small Fiber Neuropathy)**  
        - Damage to **small autonomic nerve fibers** responsible for blood vessel constriction.  
        - Leads to **poor circulation & blood pooling in the legs**.  
        - Common in **diabetes, autoimmune diseases, and post-viral syndromes**.  

        **2️⃣ Hyperadrenergic POTS (Excess Sympathetic Activity)**  
        - Overactivation of the **sympathetic nervous system**, leading to excessive norepinephrine release.  
        - Symptoms: **high blood pressure, tremors, palpitations, migraines, sweating**.  
        - Patients may experience **fluctuating blood pressure and adrenaline surges**.  

        **3️⃣ Hypovolemic POTS (Low Blood Volume)**  
        - Results from **reduced blood volume**, leading to circulation issues.  
        - Common in individuals with **low renin and aldosterone levels**.  
        - Symptoms: **cold extremities, low blood pressure, and fatigue**.  
        """)

    st.markdown("### **🧠 The Role of the Autonomic Nervous System**")
    st.markdown("""
    POTS involves an imbalance between the two branches of the **autonomic nervous system (ANS)**:

    **Parasympathetic Nervous System ("Rest & Digest")**  
    - Normally **lowers heart rate & relaxes blood vessels** when standing.  
    - In POTS, it **fails to counteract heart rate spikes**, leading to **excessive tachycardia**.  

    **Sympathetic Nervous System ("Fight or Flight")**  
    - Normally **increases blood pressure & heart rate when needed**.  
    - In **Hyperadrenergic POTS**, it is **overactive**, causing excessive **norepinephrine release, tremors, and high BP**.  
    """)

    st.image("Autonomic NS Summary.jpg")

    
    st.markdown("### **📋 How is POTS Diagnosed?**")
    if st.checkbox("🩺 Show Diagnostic Tests"):
        st.markdown("""
        **1️⃣ Active Stand Test**  
        - Patient lies down for **10 minutes**, then stands.  
        - POTS is diagnosed if the **heart rate increases by ≥30 bpm (≥40 bpm in teens) within 10 minutes** of standing.  

        **2️⃣ Tilt Table Test**  
        - Patient is secured to a **tilt table**, slowly moved upright.  
        - **Heart rate and blood pressure** are monitored.  

        **3️⃣ Valsalva Maneuver**  
        - Patient exhales **forcefully against resistance** to test autonomic function.  

        **4️⃣ QSART Test (Sweat Test)**  
        - Measures **sweat gland function**, which is controlled by the ANS.  
        - Reduced sweating indicates **neuropathic POTS**.  

        **5️⃣ Blood Volume & Catecholamine Testing**  
        - **Blood volume tests** check for **hypovolemia (low blood volume)**.  
        - **Norepinephrine testing** diagnoses **Hyperadrenergic POTS**.  
        """)

    st.markdown("### **📊 Key Measurements in POTS**")
    with st.expander("📌 Click to View Key Measurements"):
        st.markdown("""
        - **Heart Rate (HR)** → Increases **≥30 bpm upon standing**.  
        - **Blood Pressure (BP)** → Often fluctuates but does **not** drop significantly.  
        - **Stroke Volume (SV)** → Reduced due to **poor venous return** from the legs.  
        - **Cardiac Output (CO)** → Can be normal or low.  
        - **Systemic Vascular Resistance (SVR)** → Abnormal in some forms of POTS.  
        - **QSART Test (Sweat Response)** → Reduced in **Neuropathic POTS**.  
        """)

    st.markdown("### **🔬 How POTS Relates to Cardiac Event Prediction & Repair**")
    st.markdown("**AI-Based Prediction** → Differentiating POTS from cardiac events like heart attacks. **Cardiac Monitoring** → Tracking heart rate, blood pressure, and autonomic function. **Regenerative Medicine Research** → Exploring whether **stem cell therapy or synthetic bio-neurons** can repair autonomic dysfunction. ")
    st.markdown("**ASK ME ABOUT THE LBNP CHAMBER**")
    
    # Set Page Configuration
    # st.set_page_config(page_title="Cardiovascular Diseases (CVDs)", layout="wide")

    st.title("🫀 Cardiovascular Diseases (CVDs)")

    st.markdown("""
    ## ** What Are Cardiovascular Diseases (CVDs)?**
    Cardiovascular diseases (CVDs) are a group of **disorders affecting the heart and blood vessels**.  
    CVDs are the **leading cause of death worldwide**, responsible for **over 17 million deaths annually**.  

    These conditions impact **heart function, blood flow, and oxygen delivery**, leading to **serious cardiac events like heart attacks and strokes**.
    """)

    st.markdown("### **⚠️ Causes & Risk Factors of CVDs**")
    if st.checkbox("🚨 Show Major Causes & Risk Factors"):
        st.markdown("""
        **Common Causes of CVDs:**  
        - **Atherosclerosis** → Narrowing of arteries due to **plaque buildup**.  
        - **Hypertension (High Blood Pressure)** → Increases heart workload.  
        - **Diabetes** → Damages blood vessels, increasing heart disease risk.  
        - **Arrhythmias** → Irregular heartbeats affecting blood circulation.  
        - **Congenital Heart Defects** → Structural abnormalities present from birth.  

        **⚠️ Key Risk Factors for CVDs:**  
        ✅ **High cholesterol**  
        ✅ **Obesity & physical inactivity**  
        ✅ **Smoking & alcohol use**  
        ✅ **Genetic predisposition**  
        ✅ **Stress & mental health**  
        """)

    st.markdown("### **🩺 Types of Cardiovascular Diseases**")
    with st.expander("📌 Click to View Major Types of CVDs"):
        st.markdown("""
        **1️⃣ Coronary Artery Disease (CAD)**  
        - Caused by **plaque buildup (atherosclerosis)** in coronary arteries.  
        - Reduces blood flow to the heart, increasing **heart attack risk**.  

        **2️⃣ Hypertensive Heart Disease**  
        - Result of **chronic high blood pressure**, leading to **heart failure**.  

        **3️⃣ Arrhythmias**  
        - **Irregular heartbeats** due to electrical signal issues in the heart.  
        - Includes **atrial fibrillation (AFib), bradycardia, tachycardia**.  

        **4️⃣ Heart Failure**  
        - **Weak heart muscle** leads to poor circulation and fluid buildup.  
        - Causes **shortness of breath, fatigue, and swelling**.  

        **5️⃣ Valvular Heart Disease**  
        - **Faulty heart valves** lead to improper blood flow, often requiring surgery.  

        **6️⃣ Stroke**  
        - Occurs when **blood flow to the brain is blocked** (ischemic stroke) or **a vessel bursts** (hemorrhagic stroke).  

        **7️⃣ Peripheral Artery Disease (PAD)**  
        - **Narrowed arteries reduce blood flow to limbs**, causing pain and circulation issues.  
        """)

    st.markdown("### **🧪 Diagnosis & Tests for CVDs**")
    if st.checkbox("🩺 Show Diagnostic Tests for CVDs"):
        st.markdown("""
        **1️⃣ Electrocardiogram (ECG/EKG)**  
        - Detects **abnormal heart rhythms, ischemia, and heart attacks**.  
        - Used in **AI-powered ECG prediction models**.  

        **2️⃣ Echocardiogram (Ultrasound of the Heart)**  
        - Assesses **heart structure, function, and valve abnormalities**.  

        **3️⃣ Cardiac MRI**  
        - Provides **detailed imaging of the heart muscle, valves, and blood flow**.  
        - Helps diagnose **myocarditis, congenital defects, and cardiomyopathies**.  

        **4️⃣ Coronary Angiography**  
        - Uses **contrast dye & X-rays** to detect **narrowed or blocked arteries**.  

        **5️⃣ Blood Tests**  
        - **Troponin levels** indicate **heart muscle damage (e.g., heart attack)**.  
        - **BNP levels** measure heart failure severity.  

        **6️⃣ Stress Testing**  
        - Assesses heart function under **physical exertion or medication-induced stress**.  

        **7️⃣ Holter Monitoring**  
        - 24-hour ECG monitoring to detect **intermittent arrhythmias**.  
        """)

    st.markdown("### **📊 Key Cardiovascular Measurements**")
    with st.expander("📌 Click to View Key Parameters"):
        st.markdown("""
        - **Heart Rate (HR)** → Normal: **60-100 bpm**.  
        - **Blood Pressure (BP)** → Normal: **120/80 mmHg**.  
        - **Ejection Fraction (EF)** → **Measures heart's pumping ability (Normal: 55-70%)**.  
        - **Cardiac Output (CO)** → **Blood pumped per minute (Normal: 4-8 L/min)**.  
        - **Troponin Levels** → **Indicates heart damage (High = heart attack risk)**.  
        """)

    st.markdown("### **How CVDs Relate to Cardiac Event Prediction & Repair**")
    st.markdown("""
    **AI-Based Prediction Models** → **Detects early CVD risk using ECG & biomarkers**.  
    **Real-Time Monitoring** → **Integrates wearable tech for continuous tracking**.  
    **Regenerative Medicine Research** → **Exploring stem cells & synthetic bio solutions**.  
    """)

    st.subheader("### Arrhythmias")
    if st.checkbox("🔍 Learn More About Arrhythmias"):
        st.markdown("### 1️⃣ Types of Arrhythmias")
        st.markdown("""
        Arrhythmias are abnormal heart rhythms that can lead to serious cardiac events. They are classified into:
        
        - **Supraventricular Arrhythmias**:
            - **Atrial Fibrillation (AFib)**: An **irregularly irregular** heartbeat that increases the risk of **stroke**, **heart failure**, and **clots**.
            - **Atrial Flutter**: Similar to AFib but more regular.
            - **SVT (Supraventricular Tachycardia)**: Rapid heart rate episodes that can cause palpitations and fainting.
        
        - **Ventricular Arrhythmias**:
            - **Ventricular Tachycardia (VT)**: Can progress to **ventricular fibrillation (VF)**, a life-threatening emergency.
            - **Ventricular Fibrillation (VF)**: Causes cardiac arrest, requiring **immediate defibrillation**.
        
        - **Bradyarrhythmias**:
            - **Sinus Bradycardia**: Slower-than-normal heartbeat, common in athletes but can indicate disease.
            - **Heart Block**: Electrical conduction delay, possibly leading to syncope.
        """)

        st.markdown("#### Atrial Fibrillation & Fibrosis")
        st.markdown("""
        - **Atrial Fibrosis & AFib**:
            - MRI with **Late Gadolinium Enhancement (LGE)** can detect fibrosis in atrial walls.
            - Fibrosis contributes to electrical instability, making **AFib more persistent and harder to treat**.
            - Early MRI screening for atrial fibrosis could help **prevent AFib progression** before symptoms appear.

        - **Stroke Risk & AFib**:
            - AFib patients have **5x higher stroke risk** due to blood pooling in the atria.
            - Anticoagulants are often prescribed, but MRI can help **personalize stroke prevention strategies**.
        """)

        st.markdown("### Diagnosis & Tests for Arrhythmias")
        st.markdown("""
        Arrhythmias can be diagnosed using:
        
        - **ECG/EKG** (Electrocardiogram) – Captures real-time electrical signals of the heart.
        - **Holter Monitor** – A 24-48 hour wearable ECG.
        - **Electrophysiology Study (EPS)** – Tests electrical conduction pathways in the heart.
        - **MRI for Fibrosis Detection** – Advanced imaging can reveal scar tissue linked to arrhythmias.
        """)

    st.markdown("### 🏥 Proposed Research: MRI, Fibrosis & Regenerative Medicine")
    if st.checkbox("Explore MRI & Fibrosis in Cardiac Event Prediction"):
        st.markdown("### Role of Cardiac MRI in Detecting & Preventing Cardiac Events")
        st.markdown("""
        **Why Cardiac MRI?**  
        - MRI is the **gold standard** for detecting **myocardial fibrosis**, **inflammation**, and **ischemia**.
        - AI-enhanced MRI is advancing, but **multi-modal prediction models** integrating MRI with biomarkers are still underdeveloped.

        **Key Research Areas:**
        - **Myocardial Fibrosis as a Predictor of Cardiac Events**:
            - MRI detects **Late Gadolinium Enhancement (LGE)**, a marker for **fibrosis and scarring**.
            - Fibrosis increases risk for **heart failure** and **arrhythmias** but is **underutilized** in current clinical risk models.

        - **MRI vs. Traditional Biomarkers in Heart Attack Prediction**:
            - **Biomarkers** like **troponin** and **CK-MB** detect active damage, but MRI can **detect pre-symptomatic structural changes**.
            - A study comparing **MRI-based vs. blood biomarker-based prediction** could reshape **early heart attack detection**.

        """)

        st.markdown("### 2️⃣ Synthetic Biology & Regenerative Medicine in Cardiac Repair")
        st.markdown("""
        **How Can We Repair MRI-Detected Heart Damage?**
        
        - **Fibrosis & Scar Tissue Repair**:
            - **Engineered stem cell-derived cardiomyocytes** could replace fibrotic tissue.
        
        - **Injectable Bioprinted Grafts**:
            - **3D-printed bio-scaffolds** could be used to **regrow damaged cardiac tissue** after a heart attack.

        - **Gene Therapy for Fibrosis Reversal**:
            - Targeting genes involved in **collagen deposition** could help **reverse myocardial fibrosis**.
            - CRISPR-based therapies are being researched for **modifying fibrosis-related pathways**.
        """)