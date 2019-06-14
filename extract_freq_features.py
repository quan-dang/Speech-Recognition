import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile 
from python_speech_features import mfcc, logfbank

# read the input sound file
sampling_freq, audio = wavfile.read("input_freq.wav")

# extract MFCC and filter bank features
mfcc_features = mfcc(audio, sampling_freq)
filterbank_features = logfbank(audio, sampling_freq)

# print parameters
print("-" * 30)
print("MFCC:")
print("[INFO] number of windows = ", mfcc_features.shape[0])
print("[INFO] length of each feature = ", mfcc_features.shape[1])
print("-" * 30)
print("Filter bank:")
print("[INFO] number of windows = ", filterbank_features.shape[0])
print("[INFO] length of each feature = ", filterbank_features.shape[1])

# visualize the MFCC features
mfcc_features = mfcc_features.T # transform the matrix so that the time domain is horizontal
plt.matshow(mfcc_features)
plt.title('MFCC')

# visualize the filter bank features
filterbank_features = filterbank_features.T
plt.matshow(filterbank_features)
plt.title('Filter bank')

plt.show()
