# check_model.py

from tensorflow.keras.models import load_model

# Load the model
model = load_model('ECG-heartbeat-classification/notebooks/ecg_cnn_model.keras')

# Print the model summary
model.summary()
