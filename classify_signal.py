# classify_signal.py
import pandas as pd
from utils import classify_signal

# Load the features DataFrame for FSK and OFDM
stft_features_df_fsk = pd.read_csv('stft_features_fsk.csv')
stft_features_df_ofdm = pd.read_csv('stft_features_ofdm.csv')

# Combine the DataFrames
stft_features_df = pd.concat([stft_features_df_fsk, stft_features_df_ofdm])

# Parameters for classification
fsk_params = [(50, 150), (100, 200), (150, 250)]
ofdm_params = [(5, 20), (10, 30), (15, 40)]

# Classify the signals
stft_features_df['Predicted Label'] = classify_signal(stft_features_df, fsk_params, ofdm_params)

# Save the classified DataFrame to a new CSV file
stft_features_df.to_csv('classified_signals.csv', index=False)

# Print classification results
print(stft_features_df[['Time', 'Spectral Centroid', 'Spectral Bandwidth', 'Spectral Flatness', 'Dominant Frequency', 'Predicted Label']])
