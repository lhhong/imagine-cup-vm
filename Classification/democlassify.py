import tensorflow as tf
import sys
import os
import numpy as np
import json
import argparse
from tensorflow.python.platform import gfile




def democlassify(image_input, clothing_type):

	keys = {
		(1,0,0,0,0,0): 'Short sleeve T-shirt',
		(0,1,0,0,0,0): 'Long sleeve T-shirt',
		(0,0,1,0,0,0): 'Short sleeve shirt',
		(0,0,0,1,0,0): 'Long sleeve shirt',
		(0,0,0,0,1,0): 'Singlet',
		(0,0,0,0,0,1): 'Polo',
		(1,0,0): 'Jeans',
		(0,1,0): 'Pants',
		(0,0,1): 'Shorts',
		(1,0,0,0,0,0,0,0,0,0,0,0,0,0): 'boatshoes',
		(0,1,0,0,0,0,0,0,0,0,0,0,0,0): 'brogueshoes',
		(0,0,1,0,0,0,0,0,0,0,0,0,0,0): 'casualshoes',
		(0,0,0,1,0,0,0,0,0,0,0,0,0,0): 'chelseaboots',
		(0,0,0,0,1,0,0,0,0,0,0,0,0,0): 'desertboots',
		(0,0,0,0,0,1,0,0,0,0,0,0,0,0): 'espadrilles',
		(0,0,0,0,0,0,1,0,0,0,0,0,0,0): 'flipflops',
		(0,0,0,0,0,0,0,1,0,0,0,0,0,0): 'formalshoes',
		(0,0,0,0,0,0,0,0,1,0,0,0,0,0): 'laceupboots',
		(0,0,0,0,0,0,0,0,0,1,0,0,0,0): 'loafersanddrivers',
		(0,0,0,0,0,0,0,0,0,0,1,0,0,0): 'plimsolls',
		(0,0,0,0,0,0,0,0,0,0,0,1,0,0): 'sandals',
		(0,0,0,0,0,0,0,0,0,0,0,0,1,0): 'slippers',
		(0,0,0,0,0,0,0,0,0,0,0,0,0,1): 'trainers',
	}


	if clothing_type == 'tops':
		savename = 'Types_of_tops'
	elif clothing_type == 'bottoms':
		savename = 'Types_of_bottoms'
	elif clothing_type == 'shoes':
		savename = 'Types_of_shoes'
	else:
		print ('choose if you wanna test on tops or bottoms or shoes')

	tf.reset_default_graph()

	with tf.Session() as sess:
		
		new_saver = tf.train.import_meta_graph(savename+'/'+savename+'.meta')
		new_saver.restore(sess, tf.train.latest_checkpoint(savename)) # <- this returns None, but still works, why?
		prediction = sess.graph.get_tensor_by_name('prediction:0')
		inputs = sess.graph.get_tensor_by_name('inputs:0')
		
		prediction = sess.run(prediction, feed_dict={inputs: image_input})


	if clothing_type == 'tops':
		print ('Short sleeve T-shirt: {}'.format(prediction[0][0]))
		print ('Long sleeve T-shirt: {}'.format(prediction[0][1]))
		print ('Short sleeve shirt: {}'.format(prediction[0][2]))
		print ('Long sleeve shirt: {}'.format(prediction[0][3]))
		print ('Singlet: {}'.format(prediction[0][4]))
		print ('Polo: {}'.format(prediction[0][5]))
		print ('----------------------------------')
		index = np.argmax(prediction, axis=1)
		pred = np.zeros(len(prediction[0]))
		pred[index] = 1
		predicted = keys[tuple(pred)]
		print ('Predicted type: {}'.format(predicted))
		print ('----------------------------------')
		return predicted

	elif clothing_type == 'bottoms':
		print ('Jeans: {}'.format(prediction[0][0]))
		print ('Pants: {}'.format(prediction[0][1]))
		print ('Shorts: {}'.format(prediction[0][2]))
		print ('----------------------------------')
		index = np.argmax(prediction, axis=1)
		pred = np.zeros(len(prediction[0]))
		pred[index] = 1
		predicted = keys[tuple(pred)]
		print ('Predicted type: {}'.format(predicted))
		print ('----------------------------------')
		return predicted

	elif clothing_type == 'shoes':
		print ('Boat Shoes: {}'.format(prediction[0][0]))
		print ('Brogue Shoes: {}'.format(prediction[0][1]))
		print ('Casual Shoes: {}'.format(prediction[0][2]))
		print ('Chelsea Boots: {}'.format(prediction[0][3]))
		print ('Desert Boots: {}'.format(prediction[0][4]))
		print ('Espadrilles: {}'.format(prediction[0][5]))
		print ('Flip Flops: {}'.format(prediction[0][6]))
		print ('Formal Shoes: {}'.format(prediction[0][7]))
		print ('Lace Up Boots: {}'.format(prediction[0][8]))
		print ('Loafers and Drivers: {}'.format(prediction[0][9]))
		print ('Plimsolls: {}'.format(prediction[0][10]))
		print ('Sandals: {}'.format(prediction[0][11]))
		print ('Slippers: {}'.format(prediction[0][12]))
		print ('Trainers: {}'.format(prediction[0][13]))

		print ('----------------------------------')
		index = np.argmax(prediction, axis=1)
		pred = np.zeros(len(prediction[0]))
		pred[index] = 1
		predicted = keys[tuple(pred)]
		print ('Predicted type: {}'.format(predicted))
		print ('----------------------------------')
		return predicted



def set_up_graph():
	pass
