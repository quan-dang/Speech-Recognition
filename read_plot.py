import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# read the input file
sampling_freq, audio = wavfile.read('input_read.wav')

# print out the params of this signal
print("Shape: {}".format(audio.shape))
print("Datatype: {}".format(audio.dtype))
print("Duration: {}s".format(round(audio.shape[0] / float(sampling_freq), 3)))

# normalize the values since the audio signal is stored as 16-bit integer data
audio = audio / (2.**15)

# extract the first 30 values for plotting
audio = audio[:30]

# build the time axis (the x axis) and scale it using the sampling frequency factor
x_values = np.arange(0, len(audio), 1) / float(sampling_freq)

# convert to seconds
x_values *= 1000

# plotting the chopped audio signal
plt.plot(x_values, audio, color='black')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.title('Audio signal')
plt.show()

