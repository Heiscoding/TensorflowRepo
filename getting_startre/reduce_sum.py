import tensorflow as tf
y = tf.placeholder(tf.float32)
x = tf.placeholder(tf.float32)
squared_deltas = tf.square(x - y)#squared_deltas is conputed element-wisely.
loss = tf.reduce_sum(squared_deltas)#all elements of squared_deltas are summed up.
sess = tf.Session()
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))
