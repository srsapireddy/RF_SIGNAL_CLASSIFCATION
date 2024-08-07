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

## Outout
![image](https://github.com/user-attachments/assets/fa63fd64-de94-4fce-a8f5-e6119c25222a)

