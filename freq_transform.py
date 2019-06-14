import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# read the input file
sampling_freq, audio = wavfile.read('input_freq.wav')

# normalize the signal
audio = audio / (2.**15)

# since audio signal is just a numpy array, extract its length
len_audio = len(audio)

# apply Fourier transform
transformed_signal = np.fft.fft(audio)
half_length = np.ceil((len_audio + 1) / 2.0).astype(int)
print(half_length)
transformed_signal = abs(transformed_signal[0:half_length])
transformed_signal /= float(len_audio)
transformed_signal **= 2

# extract length of transformed signal
len_ts = len(transformed_signal)

# double the signal according to its length
if len_audio % 2:
    transformed_signal[1:len_ts] *= 2
else:
    transformed_signal[1:len_ts-1] *= 2

# extract power in dB
power = 10 * np.log10(transformed_signal)

# build the time axis (x axis) and scale it according to the sampling frequency
# and convert into seconds 
x_values = np.arange(0, half_length, 1) * (sampling_freq / len_audio) / 1000.0

# plot the signal
plt.figure()
plt.plot(x_values, power, color='black')
plt.xlabel('Freq (in kHz)')
plt.ylabel('Power (in dB)')
plt.show()

