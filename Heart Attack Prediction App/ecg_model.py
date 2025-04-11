# import pandas as pd
# import numpy as np
# import joblib
# from tensorflow.keras.models import load_model
# from sklearn.preprocessing import LabelEncoder

# class ECGModel:
#     def __init__(self):
#         # Load pre-trained models
#         self.cnn_model = load_model('models/ecg_cnn.h5')
#         self.label_encoder = joblib.load('models/label_encoder.pkl')
#         self.scaler = joblib.load('models/ecg_scaler.pkl')
        
#     def preprocess(self, raw_signal):
#         """Preprocess ECG signal matching training pipeline"""
#         # Apply your preprocessing steps
#         signal = self._apply_filters(raw_signal)
#         signal = self._normalize(signal)
#         return signal.reshape(1, -1, 1)  # Reshape for CNN input
    
#     def predict(self, ecg_signal):
#         """Make prediction with confidence scores"""
#         processed = self.preprocess(ecg_signal)
#         pred_proba = self.cnn_model.predict(processed)[0]
#         pred_class = np.argmax(pred_proba)
        
#         return {
#             'class': self.label_encoder.inverse_transform([pred_class])[0],
#             'confidence': float(np.max(pred_proba)),
#             'probabilities': {
#                 cls: float(prob) for cls, prob in 
#                 zip(self.label_encoder.classes_, pred_proba)
#             }
#         }
    
# import numpy as np
# import joblib
# from tensorflow.keras.models import load_model
# from sklearn.preprocessing import LabelEncoder
# import os
# from tensorflow.keras.layers import Reshape

# class ECGModel:
#     def __init__(self):
#         """Initialize model with proper shape handling"""
#         try:
#             self.model = load_model('ECG-heartbeat-classification/notebooks/ecg_cnn_model.keras')
#             self.label_encoder = LabelEncoder()
#             self.label_encoder.classes_ = np.load(
#                 'ECG-heartbeat-classification/notebooks/label_encoder_classes.npy',
#                 allow_pickle=True
#             )
            
#             # Add reshape layer if needed
#             self.requires_reshape = len(self.model.input_shape) == 3  # Check if expects 3D input
            
#             self.class_descriptions = {
#                 0: "Normal Sinus Rhythm",
#                 1: "Atrial Fibrillation (AFib)",
#                 2: "Ventricular Tachycardia (VT)",
#                 3: "Other Arrhythmia"
#             }
            
#         except Exception as e:
#             raise RuntimeError(f"Model initialization failed: {str(e)}")

#     def preprocess(self, raw_signal):
#         """Standardize input to 187 timesteps"""
#         signal = np.array(raw_signal).flatten()
        
#         # Trim or pad to 187 samples
#         if len(signal) > 187:
#             signal = signal[:187]
#         elif len(signal) < 187:
#             signal = np.pad(signal, (0, 187 - len(signal)))
            
#         # Normalize
#         signal = (signal - np.mean(signal)) / np.std(signal)
#         return signal

#     def predict(self, ecg_signal):
#         """Handle shape conversion automatically"""
#         try:
#             processed = self.preprocess(ecg_signal)
            
#             # Convert to 3D if model expects it
#             if self.requires_reshape:
#                 processed = processed.reshape(1, 187, 1)
                
#             proba = self.model.predict(processed, verbose=0)[0]
#             pred_class = np.argmax(proba)
            
#             return {
#                 'class': int(pred_class),
#                 'diagnosis': self.class_descriptions[pred_class],
#                 'confidence': float(np.max(proba)),
#                 'probabilities': {
#                     self.class_descriptions[i]: float(p) 
#                     for i, p in enumerate(proba)
#                 }
#             }
#         except Exception as e:
#             raise RuntimeError(f"Prediction failed: {str(e)}")

import numpy as np
import joblib
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import os
from scipy.signal import butter, filtfilt

class ECGModel:
    def __init__(self):
        """Initialize model with robust preprocessing"""
        try:
            self.model = load_model('ECG-heartbeat-classification/notebooks/ecg_cnn_model.keras')
            self.label_encoder = LabelEncoder()
            self.label_encoder.classes_ = np.load(
                'ECG-heartbeat-classification/notebooks/label_encoder_classes.npy',
                allow_pickle=True
            )
            
            self.class_descriptions = {
                0: "Normal Sinus Rhythm",
                1: "Atrial Fibrillation (AFib)",
                2: "Ventricular Tachycardia (VT)",
                3: "Other Arrhythmia"
            }
            
            # Fixed parameters matching your training
            self.target_length = 187  # Must match model input shape
            self.sample_rate = 360    # MIT-BIH sample rate
            
        except Exception as e:
            raise RuntimeError(f"Model initialization failed: {str(e)}")

    def _butter_bandpass(self, signal):
        """Bandpass filter (0.5-30Hz) for noise removal"""
        nyquist = 0.5 * self.sample_rate
        low = 0.5 / nyquist
        high = 30 / nyquist
        b, a = butter(4, [low, high], btype='band')
        return filtfilt(b, a, signal)

    def _segment_beats(self, signal):
        """Convert long ECG into 187-sample beats"""
        num_beats = len(signal) // self.target_length
        if num_beats == 0:
            return [np.pad(signal, (0, self.target_length - len(signal)))]
        return np.array_split(signal[:num_beats*self.target_length], num_beats)

    def preprocess(self, ecg_signal):
        """Full preprocessing pipeline"""
        signal = np.array(ecg_signal).flatten()
        signal = self._butter_bandpass(signal)
        signal = (signal - np.mean(signal)) / np.std(signal)
        return self._segment_beats(signal)

    def predict(self, ecg_signal):
        """Handle any ECG length (single beat or long recording)"""
        try:
            beats = self.preprocess(ecg_signal)
            probas = []
            
            for beat in beats:
                # Ensure correct shape (1, 187, 1)
                beat_ready = beat.reshape(1, self.target_length, 1)
                probas.append(self.model.predict(beat_ready, verbose=0)[0])
            
            avg_proba = np.mean(probas, axis=0)
            pred_class = np.argmax(avg_proba)
            
            return {
                'class': int(pred_class),
                'diagnosis': self.class_descriptions[pred_class],
                'confidence': float(np.max(avg_proba)),
                'probabilities': {
                    self.class_descriptions[i]: float(p) 
                    for i, p in enumerate(avg_proba)
                },
                'num_beats': len(beats)
            }
            
        except Exception as e:
            raise RuntimeError(f"Prediction failed: {str(e)}")