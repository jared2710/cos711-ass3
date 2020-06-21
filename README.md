# cos711-ass3
This is the GitHub repo for my COS 711 Assignment 3 project. This code has the capability to process and manipulate the air quality prediction dataset to get it ready for training, and then can also train both a CNN and an LSTM on this data. 

## Installation
If you wish to install this project, use the following git command to clone the repo to your computer:

```bash
git clone https://github.com/jared2710/cos711-ass3.git
cd cos711-ass3
```
You will need to add a 'data' folder in this repo, and add the sensor information file (airqo_metadata.csv) as well as the sensor time series file with targets (Train.csv). I cannot upload them as they go over GitHub's file size limit.

## Usage
You can run the code using python:
```bash
python main.py
```
There are 3 options for the code's execution which you can easily change by editing the code. The first is on line 14 and 15 of main.py, where you can uncomment the way you want to load the dataset: either by constructing it by processing the csv files, or by using the preprocessed dataset which was saved after constructing it.
```bash
14: method = "construct"
15: #method = "preprocessed"
```
The second comes on line 30 and 31, where you can specify (by uncommenting again) whether to train the CNN model on the dataset and get optimal weights that way, or read in the saved weights from a previous training and use those for further prediction.
```bash
30: #method = "train"
31: method = "read"
```
The third and final one comes on line 43 and 44, where you can specify the same thing as above (train weights or read them in), but for the LSTM.

```bash
43: method = "train"
44: #method = "read"
```
One more thing: to see the missing data analysis code, take a look at nan_analysis.py!

## Contribution
Thanks to the [Tensorflow framework](https://www.tensorflow.org/) and [Keras API](https://keras.io/) for making deep learning model construction a breeze, allowing students like me to experiment with these amazing mathematical wonders without having to implement it all myself.

Besides the use of this library, everything else was coded by Jared O'Reilly (me), an Honours student in [Computer Science at the University of Pretoria](https://cs.up.ac.za/) in South Africa.
