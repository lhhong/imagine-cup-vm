from democolour import democolour
from demotshirtfeatures import demotshirt
from demoshirtfeatures import demoshirt
from democlassify import democlassify
import json
import os
from tensorflow.python.platform import gfile

def predict(image_dir):
	#image_dir = '../'+image_dir
	tops_list = []
	file_glob = os.path.join(image_dir, '*top.jpg')
	tops_list.extend(gfile.Glob(file_glob))

	bottoms_list = []
	file_glob = os.path.join(image_dir, '*bottom.jpg')
	bottoms_list.extend(gfile.Glob(file_glob))

	shoes_list = []
	file_glob = os.path.join(image_dir, '*shoe.jpg')
	shoes_list.extend(gfile.Glob(file_glob))


	for top_dir in tops_list:
		top_info = []
		top_type = democlassify(top_dir, 'tops')
		top_info.append({'Type': top_type})
		top_colour = democolour(top_dir)
		if 'T-' in top_type:
			tshirt_features = demotshirt(top_dir)
			top_info.append({'Features': tshirt_features, 'Colour': top_colour})
		elif 'shirt' in top_type:
			shirt_features = demoshirt(top_dir)
			top_info.append({'Features': shirt_features, 'Colour': top_colour})
		else:
			top_info.append({'Colour': top_colour})

		top_name = top_dir.split('.')[0]
		with open(top_name+'.json', 'w') as jsonfile:
			jsonfile.write(json.dumps(top_info))

	for bottom_dir in bottoms_list:
		bottom_info = []
		bottom_type = democlassify(bottom_dir, 'bottoms')
		bottom_colour = democolour(bottom_dir)
		bottom_info.append({'Type': bottom_type})
		bottom_info.append({'Colour': bottom_colour})

		bottom_name = bottom_dir.split('.')[0]
		with open(bottom_name+'.json', 'w') as jsonfile:
			jsonfile.write(json.dumps(bottom_info))

	for shoe_dir in shoes_list:
		shoe_info = []
		shoe_type = democlassify(shoe_dir, 'shoes')
		shoe_colour = democolour(shoe_dir)
		shoe_info.append({'Type': shoe_type})
		shoe_info.append({'Colour': shoe_colour})

		shoe_name = shoe_dir.split('.')[0]
		with open(shoe_name+'.json', 'w') as jsonfile:
			jsonfile.write(json.dumps(shoe_info))

	return True

if __name__ == '__main__':
	predict('userpics')