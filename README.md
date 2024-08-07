# RF_SIGNAL_CLASSIFCATION

## Explination
### Signal Classification Project
This project aims to classify Frequency Shift Keying (FSK) and Orthogonal Frequency Division Multiplexing (OFDM) signals. The project is organized into several Python scripts for modularity and ease of understanding.

### File Structure
* utils.py: Contains utility functions for signal generation, feature extraction, and signal classification.
* fsk_signal.py: Generates FSK signals and extracts their features.
* ofdm_signal.py: Generates OFDM signals and extracts their features.
* classify_signal.py: Classifies the signals based on extracted features.
* main.py: Main script to run the entire process.

# Explanation
## utils.py
* generate_fsk_signal(t, f0, f1, data, fs): Generates an FSK signal based on input parameters.
* generate_ofdm_signal(num_subcarriers, data, subcarrier_spacing, fs, t): Generates an OFDM signal based on input parameters.
* spectral_flatness(magnitude): Calculates the spectral flatness of a given signal.
* extract_stft_features(f, t_stft, Zxx): Extracts features like spectral centroid, bandwidth, flatness, and dominant frequency from the STFT of the signal.
* classify_signal(stft_features_df, fsk_params, ofdm_params): Classifies the signals based on extracted features.

## fsk_signal.py
* Generates multiple FSK signals with different parameters.
* Extracts features from the generated signals.
* Saves the extracted features to stft_features_fsk.csv.
* ofdm_signal.py
* Generates multiple OFDM signals with different parameters.
* Extracts features from the generated signals.
* Saves the extracted features to stft_features_ofdm.csv.

## classify_signal.py
* Loads the extracted features from stft_features_fsk.csv and stft_features_ofdm.csv.
* Classifies the signals based on their features.
* Saves the classification results to classified_signals.csv.

## main.py
* Runs the entire process by calling fsk_signal.py, ofdm_signal.py, and classify_signal.py.

## How to run 
```
python2 main.py
```

## Output
![image](https://github.com/user-attachments/assets/fa63fd64-de94-4fce-a8f5-e6119c25222a)

# Basis of Signal Classification
The signals in this project are classified based on features extracted from their Short-Time Fourier Transform (STFT). The following features are used to classify the signals:

1. Spectral Centroid: This represents the "center of mass" of the spectrum. It indicates where the bulk of the signal's energy is located in the frequency spectrum.

2. Spectral Bandwidth: This measures the width of the spectrum. It shows the range of frequencies that contain a significant portion of the signal's energy.

3. Spectral Flatness: This quantifies how flat the spectrum is. A high spectral flatness value indicates that the power spectrum is similar across all frequencies (noise-like signal), while a low value indicates that the power is concentrated in a narrow band of frequencies (tonal signal).

4. Dominant Frequency: This is the frequency with the highest amplitude in the spectrum. It represents the most prominent frequency component of the signal.

# Classification Process
The classification process involves comparing the extracted features of the signals to predefined parameters characteristic of FSK and OFDM signals.

## FSK (Frequency Shift Keying)
FSK signals switch between two distinct frequencies (f0 and f1) based on the binary data being transmitted. The classification checks if the dominant frequencies in the signal match either f0 or f1.

## OFDM (Orthogonal Frequency Division Multiplexing)
OFDM signals consist of multiple subcarriers that are spaced apart by a specific frequency interval (subcarrier_spacing). The classification checks if the dominant frequencies in the signal match the expected frequencies of the subcarriers.

# Detailed Classification Steps
## FSK Classification:
* For each segment of the signal, extract the dominant frequency.
* Check if the dominant frequency matches either f0 or f1 for the given FSK parameters.

## OFDM Classification:
* For each segment of the signal, extract the dominant frequency.
* Check if the dominant frequency matches any of the expected subcarrier frequencies, which are multiples of the subcarrier_spacing for the given OFDM parameters.

# Example of Classification Logic
* FSK Signature Check: Compares the dominant frequency to f0 and f1 within a tolerance of 10 Hz.
* OFDM Signature Check: Compares the dominant frequency to the expected subcarrier frequencies within a tolerance of 10 Hz.

# Summary
The classification relies on identifying the key frequency components of the signal and matching them to the expected patterns of FSK and OFDM modulations. By extracting spectral features and analyzing the dominant frequencies, the system can distinguish between these two types of modulations effectively.
