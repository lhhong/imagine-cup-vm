import json

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

# filename = 'Scraped Json/boatshoes.json'

for filename in jsonshoes:
	print (filename)
	jsonfile = open(filename)
	items = json.load(jsonfile)

	for item in items:
		tmp = item['dir']
		array = tmp.split('/')
		tmp = array[0]+'/'+array[1]+'/shoes'+array[-1]
		print (tmp)
	# 	item['dir']=tmp

	# with open(filename, 'w') as jsonfile:
	# 	jsonfile.write(json.dumps(items))


#############################################
# for bottomjson in jsonbottoms:
# 	jsonfile = open(bottomjson)
# 	items = json.load(jsonfile)

# 	for item in items:
# 		temp = item['colour']

# 		if temp == 'blue' or temp == 'green' or temp == 'khaki' or temp == 'brown' or temp =='black' or temp=='grey' or temp=='lightblue' or temp=='darkblue' or temp == 'maroon' or temp == 'pink' or temp =='red' or temp=='orange' or temp=='white' or temp=='yellow' or temp=='olive' or temp=='camo':
# 			continue

	# with open(bottomjson, 'w') as jsonfile:
	# 	jsonfile.write(json.dumps(items))

	# print (str(bottomjson)+' changed')


# for shoejson in jsonshoes:
# 	shoetype = shoejson.split('.')[0].split('/')[1]
# 	print (shoetype)

# 	jsonfile = open(shoejson)
# 	items = json.load(jsonfile)
# 	for item in items:
# 		item['type'] = shoetype

# 	with open(shoejson, 'w') as jsonfile:
# 	    jsonfile.write(json.dumps(items))


#### ---------------------------------------------------- #######
# filename = 'Scraped Json/solids.json'

# labels = open(filename)
# labels = json.load(labels)


# for i in range(len(labels)):
# 	if 'Sleeveless' in str(labels[i]['description']):
# 		labels[i]['type'] = 'Singlet'
# 	elif 'Long sleeve' in str(labels[i]['description']):
# 		labels[i]['type'] = 'Long sleeve T-shirt'
# 	else:
# 		labels[i]['type'] = 'Short sleeve T-shirt'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))

# print ('done')
# ###########################################
# filename = 'Scraped Json/graphics.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	if 'Sleeveless' in str(labels[i]['description']):
# 		labels[i]['type'] = 'Singlet'
# 	elif 'Long sleeve' in str(labels[i]['description']):
# 		labels[i]['type'] = 'Long sleeve T-shirt'
# 	else:
# 		labels[i]['type'] = 'Short sleeve T-shirt'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/longsleeve.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	labels[i]['type'] = 'Long sleeve T-shirt'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/striped.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	if 'Sleeveless' in str(labels[i]['description']):
# 		labels[i]['type'] = 'Singlet'
# 	elif 'Long sleeve' in str(labels[i]['description']):
# 		labels[i]['type'] = 'Long sleeve T-shirt'
# 	else:
# 		labels[i]['type'] = 'Short sleeve T-shirt'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/singlets.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	labels[i]['type'] = 'Singlet'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/checkshirts.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	if 'Short sleeve' in str(labels[i]['description']) or 'Short sleeve' in str(labels[i]['title']):
# 		labels[i]['type'] = 'Short sleeve shirt'
# 	else:
# 		labels[i]['type'] = 'Long sleeve shirt'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/denimshirts.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	if 'Short sleeve' in str(labels[i]['description']) or 'Short sleeve' in str(labels[i]['title']):
# 		labels[i]['type'] = 'Short sleeve shirt'
# 	else:
# 		labels[i]['type'] = 'Long sleeve shirt'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/dressshirts.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	labels[i]['type'] = 'Long sleeve shirt'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/plainshirts.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	if 'Short sleeve' in str(labels[i]['description']) or 'Short sleeve' in str(labels[i]['title']):
# 		labels[i]['type'] = 'Short sleeve shirt'
# 	else:
# 		labels[i]['type'] = 'Long sleeve shirt'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/printedshirts.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	if 'Short sleeve' in str(labels[i]['description']) or 'Short sleeve' in str(labels[i]['title']):
# 		labels[i]['type'] = 'Short sleeve shirt'
# 	else:
# 		labels[i]['type'] = 'Long sleeve shirt'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/shortsleeveshirts.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	labels[i]['type'] = 'Short sleeve shirt'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/polos.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	labels[i]['type'] = 'Polo'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/jeans.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	labels[i]['type'] = 'Jeans'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/pants.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	labels[i]['type'] = 'Pants'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################
# filename = 'Scraped Json/shorts.json'

# labels = open(filename)
# labels = json.load(labels)

# for i in range(len(labels)):
# 	labels[i]['type'] = 'Shorts'

# with open(filename, 'w') as jsonfile:
#     jsonfile.write(json.dumps(labels))
# print ('done')
# ###########################################