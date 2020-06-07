from models.CNN import CNN
from models.LSTM import LSTM
from preprocess.DataLoader import DataLoader
import helpers as h

#print("importing tensorflow")
#import tensorflow as tf
#print("done importing tensorflow")
#from tensorflow.keras import datasets
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#method = "construct"
method = "preprocessed"

dataLoader = DataLoader(method)
(input_array, target_array) = dataLoader.load()
print(input_array)
print(target_array)



h.randomShuffleTogether(input_array, target_array)
train_data, train_labels, test_data, test_labels = h.splitToTrainAndTest(input_array, target_array, 0.66)



method = "train"
#method = "read"



cnn = CNN()
cnn.data(train_data, train_labels, test_data, test_labels)
cnn.createModel()
cnn.findBestWeights(method)
cnn.testModel()




lstm = LSTM()
lstm.data(train_data, train_labels, test_data, test_labels)
lstm.createModel()
lstm.findBestWeights(method)
lstm.testModel()

#(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
#print(train_images)
#print(train_labels)
#print(train_images.shape)
#print(train_images.head())

# Normalize pixel values to be between 0 and 1
#train_images, test_images = train_images / 255.0, test_images / 255.0


                    
                    




