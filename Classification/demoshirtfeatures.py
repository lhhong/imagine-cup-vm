import tensorflow as tf
import sys
import os
import numpy as np
import json
from tensorflow.python.platform import gfile

def demoshirt(image_input):
	keys = {
			0: 'Check',
			1: 'Denim',
			2: 'Plain',
			3: 'Printed',
			4: 'Dress'
	}


	savename = 'Shirt_features'

	tf.reset_default_graph()

	with tf.Session() as sess:
		#tf.initialize_all_variables().run()
		#sess.run(global_variables_initializer())
		
		new_saver = tf.train.import_meta_graph(savename+'/'+savename+'.meta')
		new_saver.restore(sess, tf.train.latest_checkpoint(savename)) # <- this returns None, but still works, why?
		prediction = sess.graph.get_tensor_by_name('prediction:0')
		inputs = sess.graph.get_tensor_by_name('inputs:0')
		
		prediction = sess.run(prediction, feed_dict={inputs: image_input})


	print ('Check: {}'.format(prediction[0][0]))
	print ('Denim: {}'.format(prediction[0][1]))
	print ('Plain: {}'.format(prediction[0][2]))
	print ('Printed: {}'.format(prediction[0][3]))
	print ('Dress: {}'.format(prediction[0][4]))
	print ('----------------------------------')
	pred = np.round(prediction)[0]

	features = []

	for i in range(len(pred)):
		if pred[i] == 1:
			features.append(keys[i])
	print (str(features))
	print ('----------------------------------')
	return features