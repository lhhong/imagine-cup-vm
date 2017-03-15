import tensorflow as tf
import sys
import math
import os
import numpy as np
import json
import argparse

from sklearn.model_selection import train_test_split
from tqdm import tqdm
from tensorflow.python.platform import gfile
from progress.bar import Bar


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
		'check': 0,
		'denim': 1,
		'plain': 2,
		'printed': 3,
		'dress': 4
		}

jsonshirts = [
				'Scraped Json/checkshirts.json',
				'Scraped Json/denimshirts.json',
				'Scraped Json/dressshirts.json',
				'Scraped Json/plainshirts.json',
				'Scraped Json/printedshirts.json',
				'Scraped Json/shortsleeveshirts.json',
			]

### TODO: LOAD DATA FROM BOTTLENECKS
data_inputs = []
data_labels = []

savename = 'Shirt_features'


### POPULATING DATA TO FEED INTO NEURAL NET
for jsonfile in jsonshirts:
	labels = open('../'+jsonfile)
	labels = json.load(labels)
	for item in labels:
		bottleneck_path = '../bottlenecks/'+item['dir']+'.txt'
		bottleneck_file = open(bottleneck_path, 'r')
		bottleneck_string = bottleneck_file.read()
		bottleneck_values = [float(x) for x in bottleneck_string.split(',')]
		
		data_inputs.append(bottleneck_values)

		label = [0,0,0,0,0]
		if item['check'] == 'Yes':
			label[0] = 1
		if item['denim'] == 'Yes':
			label[1] = 1
		if item['plain'] == 'Yes':
			label[2] = 1
		if item['printed'] == 'Yes':
			label[3] = 1
		if item['dress'] == 'Yes':
			label[4] = 1
		data_labels.append(label)



# Splitting into train, val, and test
train_inputs, valtest_inputs, train_labels, valtest_labels = train_test_split(data_inputs, data_labels, test_size=0.3, random_state=42)
val_inputs, test_inputs, val_labels, test_labels = train_test_split(valtest_inputs, valtest_labels, test_size=0.4, random_state=43)

# Setting hyperparameters
learning_rate = 0.01
batch_size = 64
epochs = 10
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
prediction = tf.sigmoid(logits, name='prediction')
pred = tf.round(prediction)


# Defining loss of network
difference = tf.nn.sigmoid_cross_entropy_with_logits(labels=labels, logits=logits)
loss = tf.reduce_sum(difference)
tf.summary.scalar('loss', loss)

# Setting optimiser
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)

# Define accuracy
is_correct_prediction = tf.equal(pred, labels)
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


	test_accuracy, test_loss = sess.run([accuracy, loss], feed_dict={inputs: test_inputs, labels: test_labels})
	print ("TEST LOSS: {}, TEST ACCURACY: {}".format(test_loss, test_accuracy))

	g = tf.get_default_graph()
	saver.save(sess, savename+'/'+savename)

	print (prediction.name)