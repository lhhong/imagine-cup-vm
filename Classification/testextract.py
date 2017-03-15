from getbottleneck import get_bottleneck
import tensorflow as tf
import sys
import os
import numpy as np
import json
import argparse
from tensorflow.python.platform import gfile



parser = argparse.ArgumentParser()
parser.add_argument(
  '--type',
  type=str,
  default='tops',
  help='Specify if image is in category tops/bottoms/shoes'
)
parser.add_argument(
  '--image_dir',
  type=str,
  default='',
  help='Specify where to find the image you wanna test'
)
FLAGS, unparsed = parser.parse_known_args()


#savename = 'Types_of_tops'
if FLAGS.type == 'tops':
	savename = 'Types_of_tops'
elif FLAGS.type == 'bottoms':
	savename = 'Types_of_bottoms'
elif FLAGS.type == 'shoes':
	savename = 'Types_of_shoes'
else:
	print ('choose if you wanna test on tops or bottoms or shoes')


image_input = get_bottleneck(FLAGS.image_dir)
image_input = [np.asarray(image_input)]

with gfile.FastGFile(savename+'.pbtxt','rb') as f:
	graph_def = tf.GraphDef()
	graph_def.ParseFromString(f.read())
	tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
	prediction = sess.graph.get_tensor_by_name('Softmax:0')
	inputs = sess.graph.get_tensor_by_name('inputs:0')
	new_saver = tf.train.import_meta_graph(savename+'.meta')
	new_saver.restore(sess, tf.train.latest_checkpoint('./'))
	
	prediction = sess.run(prediction, feed_dict={inputs: image_input})


if str(FLAGS.type) == 'tops':
	print ('Short sleeve T-shirt: {}'.format(prediction[0][0]))
	print ('Long sleeve T-shirt: {}'.format(prediction[0][1]))
	print ('Short sleeve shirt: {}'.format(prediction[0][2]))
	print ('Long sleeve shirt: {}'.format(prediction[0][3]))
	print ('Singlet: {}'.format(prediction[0][4]))
	print ('Polo: {}'.format(prediction[0][5]))

elif FLAGS.type == 'bottoms':
	print ('Jeans: {}'.format(prediction[0][0]))
	print ('Pants: {}'.format(prediction[0][0]))
	print ('Shorts: {}'.format(prediction[0][0]))