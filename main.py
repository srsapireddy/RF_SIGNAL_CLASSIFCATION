# main.py
import os

# Run FSK signal generation
os.system('python fsk_signal.py')

# Run OFDM signal generation
os.system('python ofdm_signal.py')

# Run classification
os.system('python classify_signal.py')
