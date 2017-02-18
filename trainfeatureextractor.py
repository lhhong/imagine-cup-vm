import tensorflow as tf
from sklearn.model_selection import train_test_split
from tqdm import tqdm

# Read 2048 vectors

data_inputs = 
data_labels = 

# Splitting into train, val, and test
train_inputs, train_labels, valtest_inputs, valtest_labels = train_test_split(data_inputs, data_labels, test_size=0.3, random_state=42)
val_inputs, val_labels, test_inputs, test_labels = train_test_split(valtest_inputs, valtest_labels, test_size=0.4, random_state=43)

# Setting hyperparameters
learning_rate = 0.01
batch_size = 128
epochs = 10
log_batch_step = 50

# useful info
n_features = len(train_features)
n_labels = len(train_labels)

# Placeholders for input features and labels
inputs = tf.placeholder(tf.float32, (None, n_features))
labels = tf.placeholder(tf.float32, (None, n_labels))

# Setting up weights and bias
weights = tf.Variable(tf.truncated_normal((n_features, n_labels), stddev=0.1))
bias = tf.Variable(tf.zeros(n_labels))

# Setting up operation in fully connected layer
logits = tf.add(tf.matmul(inputs, weights), bias)
final = tf.sigmoid(logits)
prediction = tf.round(final)

# Defining loss of network
difference = tf.nn.sigmoid_cross_entropy_with_logits(labels=labels, logits=logits)
loss = tf.reduce_sum(difference)

# Setting optimiser
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)

#Define accuracy
is_correct_prediction = tf.equal(prediction, labels)
accuracy = tf.reduce_mean(tf.cast(is_correct_prediction, tf.float32))


# Run tensorflow session
with tf.Session() as sess:
	#ADD TENSORBOARD STUFF
	init = tf.global_variables_initializer()
	sess.run(init)

	batch_count = int(math.ceil(len(train_features)/batch_size))

	for epoch_i in range(epochs):
		batches_pbar = tqdm(range(batch_count), desc='Epoch {:>2}/{}'.format(epoch_i+1, epochs), unit='batches')
		# The training cycle
		for batch_i in batches_pbar:
			# Get a batch of training features and labels
			batch_start = batch_i*batch_size
			batch_inputs = train_inputs[batch_start:batch_start + batch_size]
			batch_labels = train_labels[batch_start:batch_start + batch_size]
			# Run optimizer and get loss
			_ = sess.run(optimizer, feed_dict={inputs: batch_inputs, labels: batch_labels})
		

		# Check accuracy against Validation data
		val_accuracy, val_loss = session.run([accuracy, loss], feed_dict={inputs: val_inputs, labels: val_labels})
		print("After epoch {}, Loss: {}, Accuracy: ".format(epoch_i+1, val_loss, val_accuracy))