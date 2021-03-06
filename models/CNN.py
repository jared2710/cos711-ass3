print("importing tensorflow")
import tensorflow as tf
print("done importing tensorflow")
from tensorflow.keras import datasets, layers, models, callbacks
from tensorflow.keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt

class CNN():
    def __init__(self):
        print("CNN created")
    
    def print(self):
        print("CNN")
        
    def data(self, train_inputs, train_labels, test_inputs, test_labels):
        print("inputting data")
        self.train_inputs = train_inputs
        self.train_labels = train_labels
        self.test_inputs = test_inputs
        self.test_labels = test_labels
        
        self.num_data_elements = len(self.train_inputs)
        self.num_hourly_per_element = len(self.train_inputs[0])
        self.num_values_per_hour = len(self.train_inputs[0][0])
        
        print(self.num_data_elements)
        print(self.num_hourly_per_element)
        print(self.num_values_per_hour)
        
        print("done inputting data")
        
        
    def createModel(self):
        print("creating model")
        self.model = models.Sequential()
        
        
        self.model.add(
            layers.Conv1D(8, (3), activation='relu', input_shape=(self.num_hourly_per_element, self.num_values_per_hour))
        )
        self.model.add(
            layers.MaxPooling1D((2))
        )
        self.model.add(
            layers.Conv1D(16, (3), activation='relu')
        )
        self.model.add(
            layers.MaxPooling1D((2))
        )
        self.model.add(
            layers.Conv1D(16, (3), activation='relu')
        )
        
        
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(16, activation='relu'))
        self.model.add(layers.Dense(8, activation='relu'))
        self.model.add(layers.Dense(1))
        
        print(self.model.layers[0].input_shape)
        self.model.summary()
        
        print("done creating model")
        
    def findBestWeights(self, method):
        print("finding best weights")
        
        if(method == "read"):
            self.model.load_weights("cnn.best.hdf5")
        
        optimizer = tf.keras.optimizers.Adam(0.001)
        self.model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
        
        if(method == "train"):
            weights_file="cnn.best.hdf5"
            checkpoint = ModelCheckpoint(weights_file, monitor='val_mae', verbose=1, save_best_only=True, mode='min')
            callbacks_list = [checkpoint]

            history = self.model.fit(self.train_inputs, self.train_labels,
            epochs=100, 
            #validation_split=0.33,
            validation_data=(self.test_inputs, self.test_labels),
            callbacks=callbacks_list)
                    
            plt.plot(history.history['mae'], label='mae')
            #plt.plot(history.history['mse'][1:], label='mse')
            plt.plot(history.history['val_mae'], label = 'val_mae')
            #plt.plot(history.history['val_mse'][1:], label = 'val_mse')
            plt.xlabel('Epoch')
            plt.ylabel('Accuracy')
            plt.legend(loc='upper right')
            plt.show()
        print("done finding best weights")

    def testModel(self):
        print("testing model")
        test_loss, test_mae, test_mse = self.model.evaluate(self.test_inputs, self.test_labels, verbose=2)
        print(test_loss, test_mae, test_mse)
        print("done testing model")










                