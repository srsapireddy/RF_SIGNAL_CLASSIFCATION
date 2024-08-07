# utils.py
import numpy as np
import pandas as pd
from scipy.signal import stft

def generate_fsk_signal(t, f0, f1, data, fs):
    signal = np.zeros_like(t)
    bit_duration = len(t) // len(data)
    for i, bit in enumerate(data):
        if bit == 0:
            signal[i * bit_duration: (i + 1) * bit_duration] = np.cos(2 * np.pi * f0 * t[i * bit_duration: (i + 1) * bit_duration])
        else:
            signal[i * bit_duration: (i + 1) * bit_duration] = np.cos(2 * np.pi * f1 * t[i * bit_duration: (i + 1) * bit_duration])
    return signal

def generate_ofdm_signal(num_subcarriers, data, subcarrier_spacing, fs, t):
    signal = np.zeros_like(t, dtype=complex)
    bit_duration = len(t) // len(data)
    for i, bit in enumerate(data):
        for k in range(num_subcarriers):
            freq = k * subcarrier_spacing
            signal[i * bit_duration: (i + 1) * bit_duration] += bit * np.exp(2j * np.pi * freq * t[i * bit_duration: (i + 1) * bit_duration])
    return signal.real

def spectral_flatness(magnitude):
    geometric_mean = np.exp(np.mean(np.log(magnitude + 1e-10)))
    arithmetic_mean = np.mean(magnitude)
    return geometric_mean / (arithmetic_mean + 1e-10)

def extract_stft_features(f, t_stft, Zxx):
    features = []
    for j in range(len(t_stft)):
        magnitude = np.abs(Zxx[:, j])
        power = magnitude ** 2
        spectral_centroid = np.sum(f * magnitude) / np.sum(magnitude)
        spectral_bandwidth = np.sqrt(np.sum((f - spectral_centroid) ** 2 * magnitude) / np.sum(magnitude))
        spectral_flatness_value = spectral_flatness(magnitude)
        dominant_freq = f[np.argmax(magnitude)]
        features.append([t_stft[j], spectral_centroid, spectral_bandwidth, spectral_flatness_value, dominant_freq])
    return np.array(features)

def classify_signal(stft_features_df, fsk_params, ofdm_params):
    results = []
    for _, row in stft_features_df.iterrows():
        is_fsk = False
        is_ofdm = False
        
        # Check for FSK signature
        for f0, f1 in fsk_params:
            if np.abs(row['Dominant Frequency'] - f0) < 10 or np.abs(row['Dominant Frequency'] - f1) < 10:
                is_fsk = True
        
        # Check for OFDM signature
        for num_subcarriers, subcarrier_spacing in ofdm_params:
            expected_frequencies = [k * subcarrier_spacing for k in range(num_subcarriers)]
            if any(np.abs(row['Dominant Frequency'] - freq) < 10 for freq in expected_frequencies):
                is_ofdm = True
        
        if is_fsk:
            results.append("FSK")
        elif is_ofdm:
            results.append("OFDM")
        else:
            results.append("Unknown")
    
    return results
