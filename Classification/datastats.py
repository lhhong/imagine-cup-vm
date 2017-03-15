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


keys = {
		'Short sleeve T-shirt': 0,
		'Long sleeve T-shirt': 0,
		'Short sleeve shirt': 0,
		'Long sleeve shirt': 0,
		'Singlet': 0,
		'Polo': 0,
		'Jeans': 0,
		'Pants': 0,
		'Shorts': 0,
		'boatshoes': 0,
		'brogueshoes': 0,
		'casualshoes': 0,
		'chelseaboots': 0,
		'desertboots': 0,
		'espadrilles': 0,
		'flipflops': 0,
		'formalshoes': 0,
		'laceupboots': 0,
		'loafersanddrivers': 0,
		'plimsolls': 0,
		'sandals': 0,
		'slippers': 0,
		'trainers' : 0,
		}

total = 0


print ('----------------------TOPS:----------------------')
for jsonfile in jsontops:
	labels = open('../'+jsonfile)
	labels = json.load(labels)
	for item in labels:
		print item['colour']
		keys[item['type']] += 1
for pair in keys:
	if keys[pair]:
		print (pair+': '+str(keys[pair]))
	total += keys[pair]
	keys[pair] = 0

print ('----------------------BOTTOMS:----------------------')
for jsonfile in jsonbottoms:
	labels = open('../'+jsonfile)
	labels = json.load(labels)
	for item in labels:
		keys[item['type']] += 1
for pair in keys:
	if keys[pair]:
		print (pair+': '+str(keys[pair]))
	total += keys[pair]
	keys[pair] = 0


print ('----------------------SHOES:----------------------')
for jsonfile in jsonshoes:
	labels = open('../'+jsonfile)
	labels = json.load(labels)
	for item in labels:
		keys[item['type']] += 1
for pair in keys:
	if keys[pair]: 
		print (pair+': '+str(keys[pair]))
	total += keys[pair]
	keys[pair] = 0


print ('Total count: '+str(total))



################################

for jsonfile in jsonshoes:
	labels = open('../'+jsonfile)
	labels = json.load(labels)
	for item in labels:
		tmp = item['colour']
		if tmp == 'Black' or tmp=='White' or tmp=='Grey' or tmp=='Khaki' or tmp=='Red' or tmp=='Blue' or tmp=='Green' or tmp=='Pink' or tmp=='Yellow':
			continue
		print item['colour']