import json

jsonfile = open('trainers.json')
items = json.load(jsonfile)

print (len(items))

for item in items:
	if item['price'] is None:
		print (item['url'])