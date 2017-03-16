from Classification.demotypeclassify import demotypeclassify
from Classification.democlassify import democlassify
from Classification.democolour import democolour
from Classification.demotshirtfeatures import demotshirt
from Classification.demoshirtfeatures import demoshirt
from Classification.getbottleneck import get_bottleneck

import numpy as np
import json
import os
from tensorflow.python.platform import gfile


'''
	Function to return the type of a piece of clothing (top, bottom or shoe) and its feature vector
'''
def query(image_data):
	image_path = 'query.jpg'
	### convert binary image data to saved jpg file
	with open(image_path, 'wb') as image_file:
		image_file.write(image_data)
	
	image_input = get_bottleneck(image_path)
	image_input = [np.asarray(image_input)]
	print np.array(image_input).shape

	clothing_type = demotypeclassify(image_input)
	#print clothing_type
	specific_type = democlassify(image_input, clothing_type)
	#print specific_type
	colour = democolour(image_input)
	#print colour
	if 'T-shirt' in specific_type:
		tshirt_features = demotshirt(image_input)
		#print tshirt_features
	elif 'shirt' in specific_type:
		shirt_features = demoshirt(image_input)
		#print shirt_features

	feature_vector = []
	return feature_vector



if __name__ == '__main__':
	with open("pics/pants.jpg", "rb") as imageFile:
		f = imageFile.read()
		b = bytearray(f)
	query(b)