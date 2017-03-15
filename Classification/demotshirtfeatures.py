from getbottleneck import get_bottleneck
import tensorflow as tf
import sys
import os
import numpy as np
import json
import argparse
from tensorflow.python.platform import gfile

def demotshirt(image_dir):
	keys = {
			0: 'Graphic',
			1: 'Solid',
			2: 'Striped',
			3: 'With pocket',
	}



	parser = argparse.ArgumentParser()
	parser.add_argument(
	  '--image_dir',
	  type=str,
	  default='',
	  help='Specify where to find the image you wanna test'
	)
	FLAGS, unparsed = parser.parse_known_args()

	savename = 'T-shirt_features'


	image_input = get_bottleneck(FLAGS.image_dir)
	image_input = [np.asarray(image_input)]
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


	print ('Graphic: {}'.format(prediction[0][0]))
	print ('Solid: {}'.format(prediction[0][1]))
	print ('Striped: {}'.format(prediction[0][2]))
	print ('With pocket: {}'.format(prediction[0][3]))
	print ('----------------------------------')
	pred = np.round(prediction)[0]

	features = []
	for i in range(len(pred)):
		if pred[i] == 1:
			features.append(keys[i])
	print (features)
	print ('----------------------------------')
	return features