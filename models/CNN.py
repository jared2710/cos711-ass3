print("importing tensorflow")
import tensorflow as tf
print("done importing tensorflow")
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

class CNN():
    def __init__(self):
        print("CNN created")
    
    def print(self):
        print("CNN")
        
    def data(self, train_inputs, train_labels, test_inputs, test_labels):
        self.train_inputs = train_inputs
        self.train_labels = train_labels
        self.test_inputs = test_inputs
        self.test_labels = test_labels
        
    def createModel(self):
        self.model = models.Sequential()
        self.model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(64, activation='relu'))
        self.model.add(layers.Dense(10))
        self.model.summary()
        
    def trainModel(self):
        self.model.compile(optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'])

        history = self.model.fit(self.train_inputs, self.train_labels,
        epochs=10, 
        validation_data=(self.test_inputs, self.test_labels))
                
        plt.plot(history.history['accuracy'], label='accuracy')
        plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.ylim([0.5, 1])
        plt.legend(loc='lower right')
        plt.show()

    def testModel(self):
        test_loss, test_acc = self.model.evaluate(self.test_inputs, self.test_labels, verbose=2)
        print(test_loss, test_acc)










                