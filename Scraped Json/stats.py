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

count = 0


polo = open('polos.json')
polo = json.load(polo)


# for x in polo:
# 	#print x['striped']
# 	des = str(x['description'])
# 	print des
# 	if 'mandarin' in des or 'Mandarin' in des or 'granddad' in des or 'Granddad' in des:
# 		count += 1
# 		x['striped'] = 'Yes'
# 	else:
# 		x['striped'] = 'No'
# print (count)
# with open('polos.json', 'w') as polos:
# 	polos.write(json.dumps(polo))





# shortsleeve = open('printedshirts.json')
# x = json.load(shortsleeve)


# for i in range(len(x)):
# 	print x[i]['dress']


# y = open('dressshirts.json')
# y = json.load(y)

# indices = []

# for b in y:
# 	for i in range(len(x)):
# 		if b['image'] == x[i]['image']:
# 			indices.append(i)
# 			continue

# print (indices)
# 	# with open('longsleeve.json', 'w') as longsleeve:
# 	# 	longsleeve.write(json.dumps(x))

# for i in x:
# 	i['dress'] = 'No'


# for i in indices:
# 	x[i]['dress'] = 'Yes'

# with open('printedshirts.json', 'w') as shortsleeve:
# 	shortsleeve.write(json.dumps(x))



jsonshirts = [
				#'Scraped Json/checkshirts.json',
				#'Scraped Json/denimshirts.json',
				#'Scraped Json/dressshirts.json',
				#'Scraped Json/plainshirts.json',
				'Scraped Json/printedshirts.json',
				#'Scraped Json/shortsleeveshirts.json',
			]
for jsonfile in jsonshirts:
	x = open('../'+jsonfile)
	x = json.load(x)

	for i in x:
		print (i['dress'])