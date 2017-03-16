import tensorflow as tf
import sys
import os
import numpy as np
import json
import argparse
from tensorflow.python.platform import gfile

def democolour(image_input):
	keys = {
			(1,0,0,0,0,0,0,0,0,0): 'Blue',
			(0,1,0,0,0,0,0,0,0,0): 'Dark Blue',
			(0,0,1,0,0,0,0,0,0,0): 'White',
			(0,0,0,1,0,0,0,0,0,0): 'Black',
			(0,0,0,0,1,0,0,0,0,0): 'Grey',
			(0,0,0,0,0,1,0,0,0,0): 'Brown',
			(0,0,0,0,0,0,1,0,0,0): 'Purple',
			(0,0,0,0,0,0,0,1,0,0): 'Red',
			(0,0,0,0,0,0,0,0,1,0): 'Yellow',
			(0,0,0,0,0,0,0,0,0,1): 'Green',
	}


	savename = 'Colours'

	# print (image_input)

	# with gfile.FastGFile(savename+'.pbtxt','rb') as f:
	# 	graph_def = tf.GraphDef()
	# 	graph_def.ParseFromString(f.read())
	# 	tf.import_graph_def(graph_def, name='')

	tf.reset_default_graph()

	with tf.Session() as sess:
		#tf.initialize_all_variables().run()
		#sess.run(global_variables_initializer())
		
		new_saver = tf.train.import_meta_graph(savename+'/'+savename+'.meta')
		new_saver.restore(sess, tf.train.latest_checkpoint(savename)) # <- this returns None, but still works, why?
		prediction = sess.graph.get_tensor_by_name('prediction:0')
		inputs = sess.graph.get_tensor_by_name('inputs:0')
		
		prediction = sess.run(prediction, feed_dict={inputs: image_input})


	print ('Blue: {}'.format(prediction[0][0]))
	print ('Dark Blue: {}'.format(prediction[0][1]))
	print ('White: {}'.format(prediction[0][2]))
	print ('Black: {}'.format(prediction[0][3]))
	print ('Grey: {}'.format(prediction[0][4]))
	print ('Brown: {}'.format(prediction[0][5]))
	print ('Purple: {}'.format(prediction[0][6]))
	print ('Red: {}'.format(prediction[0][7]))
	print ('Yellow: {}'.format(prediction[0][8]))
	print ('Green: {}'.format(prediction[0][9]))
	print ('----------------------------------')

	index = np.argmax(prediction, axis=1)
	pred = np.zeros(len(prediction[0]))
	pred[index] = 1
	predicted = keys[tuple(pred)]
	print ('Predicted colour: {}'.format(predicted))
	print ('----------------------------------')
	return predicted