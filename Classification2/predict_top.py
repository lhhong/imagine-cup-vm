from getbottleneck import get_bottleneck
import tensorflow as tf
from keys import KEYS
import numpy as np

model_dir = 'Saved_models/'

# def predict_top_primary_colour(bottleneck_values):

# 	return top_primary_colour


# def predict_top_secondary_colour(bottleneck_values):

# 	return top_secondary_colour


# def predict_top_type(bottleneck_values):
# 	tf.reset_default_graph()
# 	with tf.Session() as sess:
# 		saver = tf.train.import_meta_graph(model_dir+'Types_of_tops/Types_of_tops.meta')
# 		saver.restore(sess, tf.train.latest_checkpoint(model_dir+'Types_of_tops'))
# 		prediction = sess.graph.get_tensor_by_name('prediction:0')
# 		inputs = sess.graph.get_tensor_by_name('inputs:0')
# 		pred = sess.run(prediction, feed_dict={inputs: bottleneck_values})
# 	index = np.argmax(pred)
# 	return KEYS[index]


# def predict_t_shirt_style(bottleneck_values):

# 	return t_shirt_style


# def predict_shirt_style(bottleneck_values):

# 	return shirt_style


# def predict_t_shirt_fit(bottleneck_values):

# 	return t_shirt_fit


# def predict_shirt_fit(bottleneck_values):

# 	return shirt_fit


# def predict_top_pattern(bottleneck_values):

# 	return top_pattern


# def predict_top_material(bottleneck_values):

# 	return top_material


def predict_top_x(attributes, bottleneck_values):
	tf.reset_default_graph()
	with tf.Session() as sess:
		saver = tf.train.import_meta_graph(model_dir+attributes+'/'+attributes+'.meta')
		saver.restore(sess, tf.train.latest_checkpoint(model_dir+attributes))
		prediction = sess.graph.get_tensor_by_name('prediction:0')
		inputs = sess.graph.get_tensor_by_name('inputs:0')
		pred = sess.run(prediction, feed_dict={inputs: bottleneck_values})
	index = np.argmax(pred)
	return KEYS[attributes][index]


def predict_top(bottleneck_values):
	summary = {}
	summary['Clothing type'] = 'Top'
	summary['Top primary colour'] = predict_top_x('Top_primary_colours', bottleneck_values)
	summary['Top secondary colour'] = predict_top_x('Top_secondary_colours', bottleneck_values)
	summary['Top type'] = predict_top_x('Top_types', bottleneck_values)
	
	if 'T-' in top_type or 'singlet' in top_type or 'polo' in top_type:
		summary['T-shirt style'] = predict_top_x('T-shirt_styles', bottleneck_values)
		summary['T-shirt fit'] = predict_top_x('T-shirt_fits', bottleneck_values)
	elif top_typee is 'shirt':
		summary['Shirt style'] = predict_top_x('Shirt_styles', bottleneck_values)
		summary['Shirt fit'] = predict_top_x('Shirt_fits', bottleneck_values)

	summary['Top pattern'] = predict_top_x('Top_patterns', bottleneck_values)
	summary['Top material'] = predict_top_x('Top_materials', bottleneck_values)

	return summary



### TESTING ###
if __name__ == '__main__':
	image = 'pics/tshirt.jpg'
	bottleneck_values = get_bottleneck(image)
	prediction = predict_top(bottleneck_values)
	print (prediction)