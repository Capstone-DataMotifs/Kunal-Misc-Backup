import tensorflow as tf
import numpy as np
import time

a = np.float32(np.random.rand(2,2))
b = np.float32(np.random.rand(2,2))

res = tf.math.multiply(a,b)