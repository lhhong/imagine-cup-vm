from getbottleneck import get_bottleneck
import tensorflow as tf
import sys
import os
import numpy as np
import json
import argparse
from tensorflow.python.platform import gfile


keys = {
		0: 'Check',
		1: 'Denim',
		2: 'Plain',
		3: 'Printed',
		4: 'Dress'
}



parser = argparse.ArgumentParser()
parser.add_argument(
  '--image_dir',
  type=str,
  default='',
  help='Specify where to find the image you wanna test'
)
FLAGS, unparsed = parser.parse_known_args()

savename = 'Shirt_features'


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