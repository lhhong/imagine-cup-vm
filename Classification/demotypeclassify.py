from getbottleneck import get_bottleneck
import tensorflow as tf
import sys
import os
import numpy as np
import json
import argparse
from tensorflow.python.platform import gfile



def demotypeclassify(image_input):
	savename = 'Clothing_types'
	
	tf.reset_default_graph()

	with tf.Session() as sess:
		
		new_saver = tf.train.import_meta_graph(savename+'/'+savename+'.meta')
		new_saver.restore(sess, tf.train.latest_checkpoint(savename)) # <- this returns None, but still works, why?
		inputs = sess.graph.get_tensor_by_name('inputs:0')
		indices = sess.graph.get_tensor_by_name('indices:0')
		prediction = sess.graph.get_tensor_by_name('prediction:0')
		indices, prediction = sess.run([indices, prediction], feed_dict={inputs: image_input})

		print prediction
		
	if indices[0] == 0:
		return 'tops'
	elif indices[0] == 1:
		return 'bottoms'
	elif indices[0] == 2:
		return 'shoes'
