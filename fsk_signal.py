# fsk_signal.py
import numpy as np
import pandas as pd
from scipy.signal import stft
from utils import generate_fsk_signal, extract_stft_features

# Parameters
fs = 1000  # Sampling frequency
T = 5  # Duration in seconds
t = np.linspace(0, T, int(fs * T), endpoint=False)  # Time array

# Generate multiple FSK signals
fsk_signals = []
fsk_params = [(50, 150), (100, 200), (150, 250)]
for f0, f1 in fsk_params:
    data_fsk = np.random.randint(0, 2, size=10)
    signal_fsk = generate_fsk_signal(t, f0, f1, data_fsk, fs)
    fsk_signals.append((signal_fsk, f0, f1))

# Extract and classify FSK signals
stft_features_combined = []
labels = []

for signal_fsk, f0, f1 in fsk_signals:
    f, t_stft, Zxx = stft(signal_fsk, fs=fs, nperseg=256)
    features = extract_stft_features(f, t_stft, Zxx)
    stft_features_combined.append(features)
    labels.extend(['FSK'] * len(features))

# Combine all features and labels into a DataFrame
stft_features_combined = np.vstack(stft_features_combined)
columns = ['Time', 'Spectral Centroid', 'Spectral Bandwidth', 'Spectral Flatness', 'Dominant Frequency']
stft_features_df = pd.DataFrame(stft_features_combined, columns=columns)
stft_features_df['Label'] = labels

# Save DataFrame to a CSV file
stft_features_df.to_csv('stft_features_fsk.csv', index=False)
