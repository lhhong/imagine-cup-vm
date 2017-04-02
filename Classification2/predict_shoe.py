from getbottleneck import get_bottleneck
import tensorflow as tf
from keys import KEYS
import numpy as np

model_dir = 'Saved_models/'

# def predict_shoe_primary_colour(bottleneck_values):

# 	return shoe_primary_colour


# def predict_shoe_secondary_colour(bottleneck_values):

# 	return shoe_secondary_colour


# def predict_shoe_type(bottleneck_values):

# 	return shoe_type


# def predict_shoe_feature(bottleneck_values):

# 	return shoe_feature


# def predict_shoe_material(bottleneck_values):

# 	return shoe_material

def predict_shoe_x(attributes, bottleneck_values):
	tf.reset_default_graph()
	with tf.Session() as sess:
		saver = tf.train.import_meta_graph(model_dir+attributes+'/'+attributes+'.meta')
		saver.restore(sess, tf.train.latest_checkpoint(model_dir+attributes))
		prediction = sess.graph.get_tensor_by_name('prediction:0')
		inputs = sess.graph.get_tensor_by_name('inputs:0')
		pred = sess.run(prediction, feed_dict={inputs: bottleneck_values})
	index = np.argmax(pred)
	return KEYS[attributes][index]


def predict_shoe(bottleneck_values):
	summary = {}
	summary['Clothing type'] = 'Shoe'
	summary['Shoe primary colour'] = predict_shoe_x('Shoe_primary_colours', bottleneck_values)
	summary['Shoe secondary colour'] = predict_shoe_x('Shoe_secondary_colours', bottleneck_values)
	summary['Shoe type'] = predict_shoe_x('Shoe_types', bottleneck_values)
	summary['Shoe feature'] = predict_shoe_x('Shoe_features', bottleneck_values)
	summary['Shoe material'] = predict_shoe_x('Shoe_materials', bottleneck_values)
	return summary

if __name__ == '__main__':
	bottleneck_values = get_bottleneck('pics/group-photo-02.jpg-shoe.jpg')
	summary = predict_shoe(bottleneck_values)
	print (summary)