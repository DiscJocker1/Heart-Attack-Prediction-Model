# import os
# import streamlit as st
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import plotly.graph_objects as go
# from ecg_model import ECGModel

# # Initialize model (cached)
# @st.cache_resource
# def load_ecg_model():
#     return ECGModel()

# # def generate_sample_ecg(ecg_type="Normal"):
# #     """Generate synthetic ECG signals for demo"""
# #     t = np.linspace(0, 1, 1000)
# #     if ecg_type == "Normal":
# #         return np.sin(2 * np.pi * 5 * t)
# #     elif ecg_type == "AFib":
# #         return 0.5 * np.sin(2 * np.pi * 7 * t) + 0.2 * np.random.randn(1000)
# #     elif ecg_type == "VT":
# #         return 1.5 * np.sin(2 * np.pi * 3 * t)
    
# def generate_sample_ecg(ecg_type="Normal"):
#     """Generate 187-sample ECGs matching model expectations"""
#     t = np.linspace(0, 1, 187)  # 187 samples
    
#     if ecg_type == "Normal":
#         signal = np.sin(2 * np.pi * 5 * t)  # Normal sinus rhythm
#     elif ecg_type == "AFib":
#         signal = 0.5*np.sin(2*np.pi*7*t) + 0.2*np.random.randn(187)  # Irregular
#     elif ecg_type == "VT":
#         signal = 1.5*np.sin(2*np.pi*3*t)  # Wide, fast waves
    
#     return signal

# # def plot_ecg(signal, title):
# #     """Interactive ECG plot"""
# #     fig = go.Figure()
# #     fig.add_trace(go.Scatter(y=signal, line=dict(color='#FF4B4B')))
# #     fig.update_layout(title=title, xaxis_title="Time (ms)", yaxis_title="Amplitude (mV)")
# #     st.plotly_chart(fig, use_container_width=True)

# # In your plotting function:
# def plot_ecg(signal, title):
#     """Plot first 187 samples"""
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(y=signal[:187], line=dict(color='#FF4B4B')))
#     fig.update_layout(title=title + " (First 187 samples)")
#     st.plotly_chart(fig)

# def app():
#     st.title("🫀 ECG Arrhythmia Classifier")
    
#     # Initialize model
#     model = load_ecg_model()
#     # print("Model input shape:", self.model.input_shape)
#     # File upload section
#     uploaded_file = st.file_uploader("Upload ECG (CSV/TXT)", type=["csv", "txt"])
    
#     # Sample ECG section
#     with st.expander("Or try sample ECGs"):
#         sample_type = st.radio("Sample Type", ["Normal", "AFib", "VT"])
#         if st.button("Load Sample"):
#             sample_signal = generate_sample_ecg(sample_type)
#             st.session_state.ecg_signal = sample_signal
#             st.success(f"Loaded {sample_type} sample ECG")

#     # Process ECG and show results
#     if 'ecg_signal' in st.session_state or uploaded_file:
#         try:
#             # Get the ECG data
#             ecg_signal = (st.session_state.ecg_signal if 'ecg_signal' in st.session_state 
#                           else pd.read_csv(uploaded_file, header=None).values.flatten())
            
#             # Display ECG plot
#             plot_ecg(ecg_signal[:1000], "ECG Signal")
            
#             # Make prediction
#             with st.spinner("Analyzing heart rhythm..."):
#                 result = model.predict(ecg_signal)
            
#             # Show diagnosis
#             st.subheader("Diagnosis")
#             color = "#2ecc71" if result['class'] == 0 else "#e74c3c"
#             st.markdown(f"""
#             <div style='border-left: 5px solid {color}; padding: 1rem;'>
#                 <h3 style='color:{color};'>{result['diagnosis']}</h3>
#                 <p>Confidence: <b>{result['confidence']:.1%}</b></p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Show probabilities
#             with st.expander("Detailed probabilities"):
#                 for condition, prob in result['probabilities'].items():
#                     st.progress(prob, text=f"{condition}: {prob:.1%}")
            
#             # Clinical notes
#             st.subheader("Clinical Notes")
#             if result['class'] == 0:
#                 st.success("Normal sinus rhythm detected")
#             elif result['class'] == 1:
#                 st.error("**Atrial Fibrillation Detected**\n\n- Refer to cardiologist")
#             elif result['class'] == 2:
#                 st.error("**Ventricular Tachycardia Detected**\n\n- EMERGENCY: Immediate intervention needed")
            
#         except Exception as e:
#             st.error(f"Analysis failed: {str(e)}")

# # Create sample data directory if missing
# os.makedirs("sample_data", exist_ok=True)

# import os
# import streamlit as st
# import numpy as np
# import pandas as pd
# import plotly.graph_objects as go
# import wfdb
# from ecg_model import ECGModel

# @st.cache_resource
# def load_model():
#     """Cache the model with error handling"""
#     try:
#         model = ECGModel()
        
#         # Test prediction with known-good input
#         test_signal = np.sin(np.linspace(0, 2*np.pi, 187))
#         test_result = model.predict(test_signal)
#         st.session_state.model_test_pass = True
        
#         return model
#     except Exception as e:
#         st.error(f"""Model failed to initialize. Verify:
#                 1. Model files exist in ECG-heartbeat-classification/notebooks/
#                 2. Input shape matches model expectations
#                 Error: {str(e)}""")
#         st.stop()

# def plot_ecg(signal, title, sample_rate=360):
#     """Interactive ECG plot with time in seconds"""
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(
#         y=signal,
#         x=np.arange(len(signal))/sample_rate,
#         line=dict(color='#FF4B4B', width=1),
#         name='ECG Signal'
#     ))
#     fig.update_layout(
#         title=f"{title} (Length: {len(signal)} samples)",
#         xaxis_title="Time (s)",
#         yaxis_title="Amplitude (mV)",
#         template="plotly_white"
#     )
#     st.plotly_chart(fig, use_container_width=True)

# def app():
#     st.title("🫀 ECG Arrhythmia Classifier")
    
#     # Initialize model
#     if 'ecg_model' not in st.session_state:
#         st.session_state.ecg_model = load_model()
#     model = st.session_state.ecg_model
    
#     # Processing tabs
#     tab1, tab2, tab3 = st.tabs(["Upload ECG", "PhysioNet Record", "Sample Data"])
    
#     with tab1:
#         uploaded_file = st.file_uploader(
#             "Upload CSV/TXT ECG", 
#             type=["csv", "txt"],
#             help="Single-column numeric data"
#         )
        
#         if uploaded_file:
#             try:
#                 ecg_signal = pd.read_csv(uploaded_file, header=None).values.flatten()
#                 plot_ecg(ecg_signal, "Uploaded ECG")
                
#                 with st.spinner("Analyzing..."):
#                     result = model.predict(ecg_signal)
                
#                 st.subheader("Diagnosis")
#                 color = "#2ecc71" if result['class'] == 0 else "#e74c3c"
#                 st.markdown(f"""
#                 <div style='border-left: 5px solid {color}; padding: 1rem;'>
#                     <h3 style='color:{color};'>{result['diagnosis']}</h3>
#                     <p>Confidence: <b>{result['confidence']:.1%}</b></p>
#                 </div>
#                 """, unsafe_allow_html=True)
                
#             except Exception as e:
#                 st.error(f"Analysis failed: {str(e)}")
    
#     with tab2:
#         st.markdown("### Analyze MIT-BIH Record")
#         record_id = st.text_input("Enter PhysioNet Record ID (e.g., 100):", "100")
        
#         if st.button("Load Record"):
#             try:
#                 record = wfdb.rdrecord(record_id, pn_dir='mitdb/')
#                 ecg_signal = record.p_signal[:, 0]  # Lead II
#                 plot_ecg(ecg_signal, f"Record {record_id}")
                
#                 with st.spinner("Analyzing..."):
#                     result = model.predict(ecg_signal)
                
#                 st.success(f"Result: {result['diagnosis']} (Confidence: {result['confidence']:.1%})")
                
#             except Exception as e:
#                 st.error(f"PhysioNet error: {str(e)}")
    
#     with tab3:
#         st.markdown("### Generate Sample ECG")
#         sample_type = st.selectbox("Type", ["Normal", "AFib", "VT"])
        
#         if st.button("Generate Sample"):
#             t = np.linspace(0, 1, 187)
#             if sample_type == "Normal":
#                 signal = np.sin(2 * np.pi * 5 * t)
#             elif sample_type == "AFib":
#                 signal = 0.5*np.sin(2*np.pi*7*t) + 0.2*np.random.randn(187)
#             else:  # VT
#                 signal = 1.5*np.sin(2*np.pi*3*t)
            
#             plot_ecg(signal, f"Generated {sample_type} ECG")
            
#             with st.spinner("Analyzing..."):
#                 result = model.predict(signal)
            
#             st.write(f"**Result:** {result['diagnosis']} (Confidence: {result['confidence']:.1%})")

# # Create required directories
# os.makedirs("ECG-heartbeat-classification/notebooks", exist_ok=True)

import os
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import wfdb
from ecg_model import ECGModel

@st.cache_resource
def load_model():
    """Cache the model to avoid reloading"""
    try:
        return ECGModel()
    except Exception as e:
        st.error(f"""Model failed to load. Ensure:
                1. ECG-heartbeat-classification/notebooks/ecg_cnn_model.keras exists
                2. ECG-heartbeat-classification/notebooks/label_encoder_classes.npy exists
                Error: {str(e)}""")
        st.stop()

def plot_ecg(signal, title, sample_rate=360):
    """Interactive ECG plot with time in seconds"""
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        y=signal,
        x=np.arange(len(signal))/sample_rate,
        line=dict(color='#FF4B4B', width=1),
        name='ECG Signal'
    ))
    fig.update_layout(
        title=title,
        xaxis_title="Time (s)",
        yaxis_title="Amplitude (mV)",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

def app():
    st.title("🫀 ECG Arrhythmia Classifier")
    
    # Initialize model
    model = load_model()
    
    # Processing tabs
    tab1, tab2, tab3 = st.tabs(["Upload ECG", "PhysioNet Record", "Sample Data"])
    
    with tab1:
        uploaded_file = st.file_uploader(
            "Upload CSV/TXT ECG", 
            type=["csv", "txt"],
            help="Single-column numeric data"
        )
        
        if uploaded_file:
            try:
                ecg_signal = pd.read_csv(uploaded_file, header=None).values.flatten()
                plot_ecg(ecg_signal, "Uploaded ECG Signal")
                
                with st.spinner("Analyzing..."):
                    result = model.predict(ecg_signal)
                
                st.subheader("Diagnosis")
                color = "#2ecc71" if result['class'] == 0 else "#e74c3c"
                st.markdown(f"""
                <div style='border-left: 5px solid {color}; padding: 1rem;'>
                    <h3 style='color:{color};'>{result['diagnosis']}</h3>
                    <p>Confidence: <b>{result['confidence']:.1%}</b> (from {result['num_beats']} beats)</p>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")
    
    with tab2:
        st.markdown("### Analyze MIT-BIH Records")
        record_id = st.text_input("Enter PhysioNet Record ID (e.g., 100):", "100")
        
        if st.button("Load Record"):
            try:
                record = wfdb.rdrecord(record_id, pn_dir='mitdb/')
                ecg_signal = record.p_signal[:, 0]  # Lead II
                plot_ecg(ecg_signal, f"Record {record_id} (Lead II)")
                
                with st.spinner("Analyzing..."):
                    result = model.predict(ecg_signal)
                
                st.success(f"Analyzed {result['num_beats']} beats from record {record_id}")
                st.write(f"**Diagnosis:** {result['diagnosis']} (Confidence: {result['confidence']:.1%})")
                
            except Exception as e:
                st.error(f"PhysioNet error: {str(e)}")
    
    with tab3:
        st.markdown("### Generate Sample ECG")
        sample_type = st.selectbox("Type", ["Normal", "AFib", "VT"])
        
        if st.button("Generate Sample"):
            t = np.linspace(0, 2, 374)  # 2-second sample
            if sample_type == "Normal":
                signal = np.sin(2 * np.pi * 1 * t)  # 1Hz heartbeat
            elif sample_type == "AFib":
                signal = 0.5*np.sin(2*np.pi*1.5*t) + 0.2*np.random.randn(374)
            else:  # VT
                signal = 1.5*np.sin(2*np.pi*0.8*t)
            
            plot_ecg(signal, f"Generated {sample_type} ECG")
            
            with st.spinner("Analyzing..."):
                result = model.predict(signal)
            
            st.write(f"**Result:** {result['diagnosis']} (Confidence: {result['confidence']:.1%})")

# Create required directories
os.makedirs("ECG-heartbeat-classification/notebooks", exist_ok=True)