import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# output file where the generated audio will be stored
output_file = 'output_generated.wav'

# specify audio parameters
duration = 3  # seconds
sampling_freq = 44100  # Hz
tone_freq = 587
min_val = -2 * np.pi
max_val = 2 * np.pi

# generate the time axis and the audio signal
t = np.linspace(min_val, max_val, duration * sampling_freq)
audio = np.sin(2 * np.pi * tone_freq * t)

# add some noise to the signal
noise = 0.4 * np.random.rand(duration * sampling_freq)
audio += noise

# scale it to 16-bit integer values to 16-bit integers before we store them
scaling_factor = pow(2,15) - 1
audio_normalized = audio / np.max(np.abs(audio))
audio_scaled = np.int16(audio_normalized * scaling_factor)

# write the signal to the output file
write(output_file, sampling_freq, audio_scaled)

# extract first 100 values for plotting
audio = audio[:100]

# generate the time axis and scale it
x_values = np.arange(0, len(audio), 1) / float(sampling_freq)

# convert the time axis to seconds
x_values *= 1000

# plotting the chopped audio signal
plt.plot(x_values, audio, color='black')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.title('Audio signal')
plt.show()
