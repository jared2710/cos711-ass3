#from models.CNN import CNN
#from models.LSTM import LSTM

#print("importing tensorflow")
#import tensorflow as tf
#print("done importing tensorflow")
#from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import pandas as pd

column_names = [    'ID','location','loc_altitude','km2','aspect','dist_motorway','dist_trunk','dist_primary',
                    'dist_secondary','dist_tertiary','dist_unclassified','dist_residential','popn','hh',
                    'hh_cook_charcoal','hh_cook_firewood','hh_burn_waste']
raw_dataset = pd.read_csv("data/airqo_metadata.csv", names=column_names,
                      na_values = "?", comment='\t',
                      sep=",", skiprows=1)
sensors = raw_dataset.copy()
print(sensors)

column_names = [    'ID','location','temp','precip','rel_humidity',
                    'wind_dir','wind_spd','atmos_press','target']
raw_dataset = pd.read_csv("data/Train.csv", names=column_names,
                      na_values = "?", comment='\t',
                      sep=",", skiprows=1)
dataset = raw_dataset.copy()
print(dataset.head())
print(dataset['rel_humidity'].head())


#lstm = LSTM()
#lstm.print()

#(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
#train_images, test_images = train_images / 255.0, test_images / 255.0

#cnn = CNN()
#cnn.data(train_images, train_labels, test_images, test_labels)
#cnn.createModel()
#cnn.trainModel()
#cnn.testModel()


                    
                    




