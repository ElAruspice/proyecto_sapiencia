import numpy as np
from keras import layers, models
from keras.utils import to_categorical
from keras.datasets import mnist
import matplotlib.pyplot as plt
(train_data, train_labels), (test_data, test_labels) =mnist.load_data()
train_data
train_data.shape
train_data[0]
plt.imshow(train_data[0])
train_labels[0]
