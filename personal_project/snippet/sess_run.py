def s_run(value):
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        return tf.constant(value).eval()

print(s_run(1)) 
