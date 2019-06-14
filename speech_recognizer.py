import os
import argparse 

import numpy as np
from scipy.io import wavfile 
from hmmlearn import hmm
from python_speech_features import mfcc

# function to parse input arguments
def build_arg_parser():
    parser = argparse.ArgumentParser(description='Trains the HMM classifier')
    parser.add_argument("--input-folder", dest="input_folder", required=True,
            help="Input folder containing the audio files in subfolders")
    return parser


"""
class to handle HMM training and prediction
"""

class HMMTrainer(object):
    # initialze the class and use Gaussian HMMs to model our data
    #   n_components: number of hidden states
    #   cov_type: type of covariance in our transition matrix
    #   n_iter: number of iterations before it stops training
    def __init__(self, model_name='GaussianHMM', n_components=4, cov_type='diag', n_iter=1000):
        # initialize the variables
        self.model_name = model_name
        self.n_components = n_components
        self.cov_type = cov_type
        self.n_iter = n_iter
        self.models = []

        # define the model
        if self.model_name == 'GaussianHMM':
            self.model = hmm.GaussianHMM(n_components=self.n_components, 
                    covariance_type=self.cov_type, n_iter=self.n_iter)
        else:
            raise TypeError('Invalid model type')

    # X is a 2D numpy array, where each element is a vector 
    # consisting of k dimensions
    def train(self, X):
        np.seterr(all='ignore')
        self.models.append(self.model.fit(X))

    # extract the score based on the model
    def get_score(self, input_data):
        return self.model.score(input_data)

# define the main function
if __name__=='__main__':
    # parse the input args
    args = build_arg_parser().parse_args()
    input_folder = args.input_folder

    # initialize the variable that will hold all the HMM models
    hmm_models = []

    # parse the input directory which contains all the database's audio files
    for dirname in os.listdir(input_folder):
        # grab the name of the subfolder 
        subfolder = os.path.join(input_folder, dirname)

        if not os.path.isdir(subfolder): 
            continue

        # since the name of the folder is the label of this class, 
        # then we extract it
        label = subfolder[subfolder.rfind('/') + 1:]

        # initialize variables for training
        X = np.array([])
        y_words = []

        # iterate through the list of audio files in each subfolder
        # (leaving 1 file for testing in each class)
        for filename in [x for x in os.listdir(subfolder) if x.endswith('.wav')][:-1]:
            # read the input file
            filepath = os.path.join(subfolder, filename)
            sampling_freq, audio = wavfile.read(filepath)
            
            # extract MFCC features
            mfcc_features = mfcc(audio, sampling_freq)

            # keep appending this to the variable X
            if len(X) == 0:
                X = mfcc_features
            else:
                X = np.append(X, mfcc_features, axis=0)
            
            # append the corresponding label
            y_words.append(label)

        print("[INFO] X.shape = ", X.shape)

        # train and save the HMM model
        hmm_trainer = HMMTrainer()
        hmm_trainer.train(X)
        hmm_models.append((hmm_trainer, label))
        hmm_trainer = None

    # get a list of test files that were not used for training
    # for testing purpose
    input_files = [
            input_folder + '/pineapple/pineapple15.wav',
            input_folder + '/orange/orange15.wav',
            input_folder + '/apple/apple15.wav',
            input_folder + '/kiwi/kiwi15.wav'
            ]

    # parse the input files
    for input_file in input_files:
        # read each input file
        sampling_freq, audio = wavfile.read(input_file)

        # extract MFCC features
        mfcc_features = mfcc(audio, sampling_freq)

        # define variables to store the maximum score and the output label
        max_score = float("-inf")
        output_label = None

        # iterate through all HMM models and 
        # run the input file for each of them
        for item in hmm_models:
            hmm_model, label = item

            # extract the scofe and store the max score
            score = hmm_model.get_score(mfcc_features)
            if score > max_score:
                max_score = score
                output_label = label

        # print the true and predicted labels
        print("-" * 30)
        print("[INFO] true: ", input_file[input_file.find('/')+1:input_file.rfind('/')])
        print("[INFO] predicted: ", output_label) 

