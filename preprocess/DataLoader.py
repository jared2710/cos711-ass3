import pandas as pd
import numpy as np
from preprocess.PreProcessor import PreProcessor

class DataLoader():
    def __init__(self, method):
        self.method = method
        
    
    def print(self):
        print("DataLoader")
        
    def load(self):
        if(self.method == "preprocessed"):
            return self.loadFromPreprocessed()
        elif(self.method == "construct"):
            return self.loadFromRawFiles()
        else:
            return "Invalid method"
        
    def loadFromRawFiles(self):
        pre = PreProcessor()
        pre.fetchFromFiles()
        pre.convertCSVReadToNumpy()
        pre.normalizeNumpyArray()
        pre.saveToFile()
        return (pre.dataset_array, pre.target_array)
        
        
    def loadFromPreprocessed(self):
        dataset_array = np.load('data/dataset_array.npy')
        target_array = np.load('data/target_array.npy')
        return (dataset_array, target_array)