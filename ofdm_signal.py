# ofdm_signal.py
import numpy as np
import pandas as pd
from scipy.signal import stft
from utils import generate_ofdm_signal, extract_stft_features

# Parameters
fs = 1000  # Sampling frequency
T = 5  # Duration in seconds
t = np.linspace(0, T, int(fs * T), endpoint=False)  # Time array

# Generate multiple OFDM signals
ofdm_signals = []
ofdm_params = [(5, 20), (10, 30), (15, 40)]
for num_subcarriers, subcarrier_spacing in ofdm_params:
    data_ofdm = np.random.randint(0, 2, size=10)
    signal_ofdm = generate_ofdm_signal(num_subcarriers, data_ofdm, subcarrier_spacing, fs, t)
    ofdm_signals.append((signal_ofdm, num_subcarriers, subcarrier_spacing))

# Extract and classify OFDM signals
stft_features_combined = []
labels = []

for signal_ofdm, num_subcarriers, subcarrier_spacing in ofdm_signals:
    f, t_stft, Zxx = stft(signal_ofdm, fs=fs, nperseg=256)
    features = extract_stft_features(f, t_stft, Zxx)
    stft_features_combined.append(features)
    labels.extend(['OFDM'] * len(features))

# Combine all features and labels into a DataFrame
stft_features_combined = np.vstack(stft_features_combined)
columns = ['Time', 'Spectral Centroid', 'Spectral Bandwidth', 'Spectral Flatness', 'Dominant Frequency']
stft_features_df = pd.DataFrame(stft_features_combined, columns=columns)
stft_features_df['Label'] = labels

# Save DataFrame to a CSV file
stft_features_df.to_csv('stft_features_ofdm.csv', index=False)
