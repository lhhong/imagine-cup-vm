import json
import urllib.request

# name of json file to get scrape info from
filename = 'Scrapy/Scraped Json/test.json'

labels = open(filename)
labels = json.load(labels)
# print data[0]['image']
# print data[0]['colour']
# print len(data)

for i in range(len(labels)):
	imgurl = labels[i]['image']
	# change directory here as appropriate
	urllib.request.urlretrieve(imgurl, 'T shirts/'+str(i)+'.jpg')
	labels[i]['imagename'] = str(i) + '.jpg'

# to write the name of the saved image into the json file, for reference/training
with open(filename, 'w') as jsonfile:
    jsonfile.write(json.dumps(labels))
