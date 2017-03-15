import tensorflow as tf
import sys
import math
import os
import numpy as np
import json
import argparse

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from tqdm import tqdm
from tensorflow.python.platform import gfile
from progress.bar import Bar

parser = argparse.ArgumentParser()
parser.add_argument(
  '--type',
  type=str,
  default='tops',
  help='Specify if image is top/bottom/shoe'
)
FLAGS, unparsed = parser.parse_known_args()

"""
Reference for classes:
Tops: 
	0 - Short sleeve T-shirt
	1 - Long sleeve T-shirt
	2 - Short sleeve shirt
	3 - Long sleeve shirt
	4 - Singlet
	5 - Polo

Bottoms:
	0 - Jeans
	1 - Pants
	2 - Shorts

Shoes:
	0 - Sport Shoes
	1 - Sneakers
	2 - Boots
	3 - Dress shoes
	
"""

keys = {
		# 'blue': [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		# 'darkblue': [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		# 'lightblue': [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		# 'white': [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
		# 'black': [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
		# 'grey': [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
		# 'brown': [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
		# 'khaki': [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
		# 'purple': [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
		# 'pink': [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
		# 'red': [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
		# 'maroon': [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
		# 'orange': [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
		# 'yellow': [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
		# 'green': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
		# 'olive': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
		# 'camo': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],

		'blue': [1,0,0,0,0,0,0,0,0,0],
		'darkblue': [0,1,0,0,0,0,0,0,0,0],
		'lightblue': [1,0,0,0,0,0,0,0,0,0],
		'white': [0,0,1,0,0,0,0,0,0,0],
		'black': [0,0,0,1,0,0,0,0,0,0],
		'grey': [0,0,0,0,1,0,0,0,0,0],
		'brown': [0,0,0,0,0,1,0,0,0,0],
		'khaki': [0,0,0,0,0,1,0,0,0,0],
		'purple': [0,0,0,0,0,0,1,0,0,0],
		'pink': [0,0,0,0,0,0,0,1,0,0],
		'red': [0,0,0,0,0,0,0,1,0,0],
		'maroon': [0,0,0,0,0,0,0,1,0,0],
		'orange': [0,0,0,0,0,0,0,1,0,0],
		'yellow': [0,0,0,0,0,0,0,0,1,0],
		'green': [0,0,0,0,0,0,0,0,0,1],
		'olive': [0,0,0,0,0,0,0,0,0,1],
		'camo': [0,0,0,0,0,0,0,0,0,1],

		### USING THESE TEN COLOURS ###
		# 'blue':
		# 'darkblue':
		# 'white':
		# 'black':
		# 'grey':
		# 'brown':
		# 'purple':
		# 'red':
		# 'yellow':
		# 'green':

		}

jsontops = [
				'Scraped Json/checkshirts.json',
				'Scraped Json/denimshirts.json',
				'Scraped Json/dressshirts.json',
				'Scraped Json/plainshirts.json',
				'Scraped Json/printedshirts.json',
				'Scraped Json/shortsleeveshirts.json',
				'Scraped Json/graphics.json',
				'Scraped Json/longsleeve.json',
				'Scraped Json/solids.json',
				'Scraped Json/striped.json',
				'Scraped Json/singlets.json',
				'Scraped Json/polos.json',
			]

jsonbottoms = [
				'Scraped Json/jeans.json',
				'Scraped Json/pants.json',
				'Scraped Json/shorts.json',
				]

jsonshoes = [
				'Scraped Json/boatshoes.json',
				'Scraped Json/brogueshoes.json',
				'Scraped Json/casualshoes.json',
				'Scraped Json/chelseaboots.json',
				'Scraped Json/desertboots.json',
				'Scraped Json/espadrilles.json',
				'Scraped Json/flipflops.json',
				'Scraped Json/formalshoes.json',
				'Scraped Json/laceupboots.json',
				'Scraped Json/loafersanddrivers.json',
				'Scraped Json/plimsolls.json',
				'Scraped Json/sandals.json',
				'Scraped Json/slippers.json',
				'Scraped Json/trainers.json',
				]


### TODO: LOAD DATA FROM BOTTLENECKS
data_inputs = []
data_labels = []


savename = 'Colours'


### POPULATING DATA TO FEED INTO NEURAL NET
for jsonfile in jsontops:
	labels = open('../'+jsonfile)
	labels = json.load(labels)
	for item in labels:
		bottleneck_path = '../bottlenecks/'+item['dir']+'.txt'
		bottleneck_file = open(bottleneck_path, 'r')
		bottleneck_string = bottleneck_file.read()
		bottleneck_values = [float(x) for x in bottleneck_string.split(',')]
		
		data_inputs.append(bottleneck_values)
		data_labels.append(keys[item['colour']])

for jsonfile in jsonbottoms:
	labels = open('../'+jsonfile)
	labels = json.load(labels)
	for item in labels:
		bottleneck_path = '../bottlenecks/'+item['dir']+'.txt'
		bottleneck_file = open(bottleneck_path, 'r')
		bottleneck_string = bottleneck_file.read()
		bottleneck_values = [float(x) for x in bottleneck_string.split(',')]
		
		data_inputs.append(bottleneck_values)
		data_labels.append(keys[item['colour']])

for jsonfile in jsonshoes:
	labels = open('../'+jsonfile)
	labels = json.load(labels)
	for item in labels:
		bottleneck_path = '../bottlenecks/'+item['dir']+'.txt'
		bottleneck_file = open(bottleneck_path, 'r')
		bottleneck_string = bottleneck_file.read()
		bottleneck_values = [float(x) for x in bottleneck_string.split(',')]
		
		data_inputs.append(bottleneck_values)
		data_labels.append(keys[item['colour']])



# Splitting into train, val, and test
train_inputs, valtest_inputs, train_labels, valtest_labels = train_test_split(data_inputs, data_labels, test_size=0.3, random_state=42)
val_inputs, test_inputs, val_labels, test_labels = train_test_split(valtest_inputs, valtest_labels, test_size=0.4, random_state=43)

# Setting hyperparameters
learning_rate = 0.005
batch_size = 64
epochs = 8
log_batch_step = 50

# useful info
n_features = np.size(train_inputs, 1)
n_labels = np.size(train_labels, 1)

tf.reset_default_graph()
graph = tf.get_default_graph()

# Placeholders for input features and labels
inputs = tf.placeholder(tf.float32, (None, n_features), name='inputs')
labels = tf.placeholder(tf.float32, (None, n_labels), name='labels')

# Setting up weights and bias
weights = tf.Variable(tf.truncated_normal((n_features, n_labels), stddev=0.1), name='weights')
bias = tf.Variable(tf.zeros(n_labels), name='bias')
tf.summary.histogram('weightshist', weights)
tf.summary.histogram('biashist', bias)

# Setting up operation in fully connected layer
logits = tf.add(tf.matmul(inputs, weights), bias)
prediction = tf.nn.softmax(logits, name='prediction')
indices = tf.argmax(prediction, 1)


# Defining loss of network
difference = tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=logits)
loss = tf.reduce_sum(difference)
tf.summary.scalar('loss', loss)

# Setting optimiser
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)

# Define accuracy
is_correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct_prediction, tf.float32))
tf.summary.scalar('accuracy', accuracy)

# For saving checkpoint after training
saver = tf.train.Saver()

merged = tf.summary.merge_all()

# tensorboard --logdir=path/to/log  --> to view tensorboard

# Run tensorflow session
with tf.Session() as sess:
	init = tf.global_variables_initializer()
	sess.run(init)
	train_writer = tf.summary.FileWriter(savename, sess.graph)
	# tf.train.write_graph(sess.graph_def, '', savename+'.pbtxt', as_text=False)

	# Running the training in batches 
	batch_count = int(math.ceil(len(train_inputs)/batch_size))

	for epoch_i in range(epochs):
		batches_pbar = tqdm(range(batch_count), desc='Epoch {:>2}/{}'.format(epoch_i+1, epochs), unit='batches')
		# The training cycle
		for batch_i in batches_pbar:
			# Get a batch of training features and labels
			batch_start = batch_i*batch_size
			batch_inputs = train_inputs[batch_start:batch_start + batch_size]
			batch_labels = train_labels[batch_start:batch_start + batch_size]
			# Run optimizer
			_, summary = sess.run([optimizer, merged], feed_dict={inputs: batch_inputs, labels: batch_labels})
			train_writer.add_summary(summary, batch_i)

		# Check accuracy against validation data
		val_accuracy, val_loss = sess.run([accuracy, loss], feed_dict={inputs: val_inputs, labels: val_labels})
		print("After epoch {}, Loss: {}, Accuracy: {}".format(epoch_i+1, val_loss, val_accuracy))


	test_accuracy, test_loss, indices = sess.run([accuracy, loss, indices], feed_dict={inputs: test_inputs, labels: test_labels})
	print ("TEST LOSS: {}, TEST ACCURACY: {}".format(test_loss, test_accuracy))

	# prediction = np.zeros((np.array(test_labels).shape))
	# print (prediction)
	# print (indices)
	# for i in range(len(test_labels)):
	# 	prediction[i][indices[i]] = 1
	# print (prediction)

	true = np.argmax(test_labels, axis=1)

	# x-axis: predicted, y-axis: truth
	confusion_matrix = confusion_matrix(true, indices)
	print (confusion_matrix)

	g = tf.get_default_graph()
	result = saver.save(sess, savename+'/'+savename)


	print (prediction.name)
	print (result)