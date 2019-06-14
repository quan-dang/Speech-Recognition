# Speech Recognition
* Experiments with speech 
* Create a speech recognition system with HMM
* Build a TTS (text-to-speech) system with pyttsx 

## Project structure

* __read_plot.py:__ read and plot the input signal
* __freq_transform.py:__ transform audio signals into the frequency domain
* __generate.py:__ generate audio signals with custom parameters
* __synthesize_music.py:__ synthesize music
* __tone_freq_map.json:__ JSON file contains some notes along with their frequencies
* __extract_freq_features.py:__ extract frequency domain features
* __speech_recognizer.py:__ script to run speech recognizer
* __hmm-speech-recognition-0.1/:__ our dataset
    - __audio/__
    - ..
* __TTS.py:__ script to run TTS

## Dataset

1. Sample dataset for experiments
    * __input_freq.wav__
    * __input_read.wav__

2. Dataset for our speech recognizer

We will use the [database](https://code.google.com/archive/p/hmm-speech-recognition/downloads) from Google, which 
contains 7 different words, where each word has 15 audio files associated with it. Please download and extract it
to the root path of our project before moving on.

We are going to recognize 7 different words from the given dataset.

## How to run

* __Step 1:__ visualize the input signal and retrieve some important properties on the terminal

```
python read_plot.py
```

* __Step 2:__ transform audio signals into the frequency domain 

```
python freq_transform.py
```

* __Step 3:__ generate audio signals

```
python generate.py
```

* __Step 4:__ synthesize music

```
python synthesize_music.py
```

* __Step 5:__ extract frequency domain features

```
python extract_freq_features.py
```

* __Step 6:__ run speech recognizer

```
python speech_recognizer.py --input-folder hmm-speech-recognition-0.1/audio
```

* __Step 6__ run TTS, plug your earphone and enjoy Eminem music

```
python TTS.py
```



