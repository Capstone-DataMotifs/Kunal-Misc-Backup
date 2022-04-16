import tensorflow as tf
import numpy as np

a = np.float32(np.random.rand(2,2))
b = np.float32(np.random.rand(2,2))

res = tf.linalg.matmul(a,b)