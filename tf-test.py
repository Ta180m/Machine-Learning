# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

# print(tf.__version__)

# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

with tf.device("/GPU:0"):
    a = tf.random.normal([1, 2])


