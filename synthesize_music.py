import json
import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

# synthesize a tone
def synthesizer(freq, duration, amp=1.0, sampling_freq=44100):
    # build the time axis values
    # print("duration: ", duration)
    # print("sampling_freq: ", sampling_freq)
    # print("duration * sampling_freq: ", np.ceil(duration * sampling_freq).astype(int))
    t = np.linspace(0.0, duration, num=np.ceil(duration*sampling_freq).astype(int))

    # construct the audio signal using the input args 
    # such as amplitude and frequency
    audio = amp * np.sin(2 * np.pi * freq * t)

    return audio.astype(np.int16) 

if __name__=='__main__':
    # JSON file containing note to frequency mapping
    tone_map_file = 'tone_freq_map.json'
    
    # read the frequency map
    with open(tone_map_file, 'r') as f:
        tone_freq_map = json.loads(f.read())

    # assume that we want to generate a 'G' note 
    # for a duration of two seconds 
    input_tone = 'G'
    duration = 2.0     # seconds
    amplitude = 10000
    sampling_freq = 44100    # Hz

    # generate the note
    synthesized_tone = synthesizer(tone_freq_map[input_tone], duration, amplitude, sampling_freq)

    # write the generated signal to the output file
    write('output_tone.wav', sampling_freq, synthesized_tone)

    # generate some notes in sequence to give it a musical feel
    # define a note sequence along with their durations in seconds
    tone_seq = [('D', 0.3), ('G', 0.6), ('C', 0.5), ('A', 0.3), ('Asharp', 0.7)]

    # iterate through the list and call the synthesizer function for each of them
    output = np.array([])
    for item in tone_seq:
        input_tone = item[0]
        duration = item[1]
        synthesized_tone = synthesizer(tone_freq_map[input_tone], duration, amplitude, sampling_freq)
        output = np.append(output, synthesized_tone, axis=0)
    output = output.astype(np.int16)

    # write the signal to the output file
    write('output_tone_seq.wav', sampling_freq, output)

