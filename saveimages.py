import json
import urllib.request
from progress.bar import Bar
from tensorflow.python.platform import gfile
import os

# name of json file to get scrape info from
# filename = 'Clothes/Shoes/pants.json'
# labels = open(filename)
# labels = json.load(labels)

image_dir = 'Clothes/Shoes'

file_list = []
file_glob = os.path.join(image_dir, '*.json')
file_list.extend(gfile.Glob(file_glob))

i = 0

for jsonfile in file_list:
	items = open(jsonfile)
	items = json.load(items)
	bar = Bar('Downloading from '+str(jsonfile), max=len(items))
	for item in items:
		imgurl = item['image']
		item_dir = image_dir+'/'+str(i)+'.jpg'
		urllib.request.urlretrieve(imgurl, item_dir)
		item['dir'] = item_dir
		i += 1
		bar.next()
	bar.finish()
	with open(jsonfile, 'w') as newfile:
		newfile.write(json.dumps(items))


# n_images = len(labels)
# imagedir = 'Clothes/Bottoms/Pants/'

# bar = Bar('Downloading and saving images:', max=n_images)
# for i in range(n_images):
# 	imgurl = labels[i]['image']
	
# 	urllib.request.urlretrieve(imgurl, imagedir+str(i)+'.jpg')
# 	labels[i]['dir'] = imagedir+str(i) + '.jpg'
# 	bar.next()
# bar.finish()

# to write the name of the saved image into the json file, for reference/training
# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
