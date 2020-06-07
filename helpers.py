import random

def splitToTrainAndTest(data, labels, perc):
    length = len(data)
    length = int(length * perc)
    
    train_data = data[:length]
    train_labels = labels[:length]
    test_data = data[length:]
    test_labels = labels[length:]
    
    return train_data, train_labels, test_data, test_labels
    
def randomShuffleTogether(arr1, arr2):
	for i in range(len(arr1)):
		rand = int(random.random()*len(arr1))
		arr1[i], arr1[rand] = arr1[rand].copy(), arr1[i].copy()
		arr2[i], arr2[rand] = arr2[rand].copy(), arr2[i].copy()