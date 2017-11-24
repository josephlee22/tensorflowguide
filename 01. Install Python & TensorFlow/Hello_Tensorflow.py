import tensorflow as tf # It'll Call Tensorflow as tf
sess = tf.Session()
hello = tf.constant("Hello Tensorflow")
print(sess.run(hello))
