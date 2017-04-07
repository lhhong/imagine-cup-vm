import pandas as pd
import numpy as np
import keys
import csv
import glob

''' getting vector string '''
'''
csv_path = 'predictedshoes.csv'
csvfile = open('string_predictedshoes.csv', 'w', newline='')
writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
with open(csv_path, 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		path = row[-1]
		bot = row[1]
		string_vector = (', '.join(row[2:-1]))
		print (path)
		print (string_vector)
		entry = [bot]+[string_vector]+[path]
		print (entry)
		writer.writerow(entry)
		print ('one row entered')
'''



'''removing duplicate pictures'''
'''
count = 0
total = 0
fileglob = glob.glob('Clothes/Shoes/*.jpg')

out = open('clean_predictedshoes.csv', 'w')
writer = csv.writer(out, delimiter=',', quoting=csv.QUOTE_MINIMAL)

with open('predictedshoes.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		if row[-1] in fileglob:
			count += 1
			writer.writerow(row)
		total += 1
print ('{} out of {}'.format(count, total))
'''

'''changing predictions to 0 for non applicable columns'''
# top_types = [
#     "top-type-short-sleeve-t-shirt",
#     "top-type-long-sleeve-t-shirt",
#     "top-type-short-sleeve-shirt",
#     "top-type-long-sleeve-shirt",
#     "top-type-singlet",
#     "top-type-polo",
# ]
# t_shirt_fits = [
#     "t-shirt-fit-slim-fit",
#     "t-shirt-fit-longline",
#     "t-shirt-fit-baggy",
#     "t-shirt-fit-regular"
# ]

# shirt_fits = [
#     "shirt-fit-slim-fit",
#     "shirt-fit-regular-fit"
# ]

# shirt_styles = [
#     "shirt-style-oxford",
#     "shirt-style-dress",
#     "shirt-style-graphic",
#     "shirt-style-pocket",
#     "shirt-style-granddad-collar",
# ]

# t_shirt_styles = [
#     "t-shirt-style-graphic-text",
#     "t-shirt-style-graphic-image",
#     "t-shirt-style-round-neck",
#     "t-shirt-style-henley",
#     "t-shirt-style-pocket",
# ]

# df = pd.read_csv('unlabelled_predictedtops.csv')
# count = 0
# for i in range(len(df)):
# 	x = (df.loc[i, top_types])
# 	index = np.argmax(x)
# 	# print (x)
# 	print (index)
# 	if 't-shirt' in index or 'polo' in index or 'singlet' in index:
# 		df.ix[i, shirt_styles] = 0
# 		df.ix[i, shirt_fits] = 0
# 	else:
# 		df.ix[i, t_shirt_styles] = 0
# 		df.ix[i, t_shirt_fits] = 0
# df.to_csv('unlabelled_predictedtops.csv')

# bottom_materials = [
#     "bottom-material-denim/jeans",
#     "bottom-material-cotton",
#     "bottom-material-dry-fit"
# ]

# denim_styles = [
#     "denim-style-ripped",
#     "denim-style-acid-wash",
#     "denim-style-washed"
# ]
# df = pd.read_csv('unlabelled_predictedbottoms.csv')
# count = 0
# for i in range(len(df)):
# 	x = (df.loc[i, bottom_materials])
# 	index = np.argmax(x)
# 	print (x)
# 	print (index)
# 	if 'denim' not in index:
# 		df.ix[i, denim_styles] = 0
# df.to_csv('unlabelled_predictedbottoms.csv')



'''adding dir from bottleneck_dir'''
# data = pd.read_csv('unlabelled_predictedshoes.csv')

# data['dir'] = data.index
# for i in range(len(data)):
# 	tmp = data['bottleneck_dir'][i]
# 	new = tmp[12:-4]

# 	data['dir'][i] = new
# 	print (data['dir'][i])

# print (data.to_csv('unlabelled_predictedshoes.csv'))


# top_types = [
#     "top-type-short-sleeve-t-shirt",
#     "top-type-long-sleeve-t-shirt",
#     "top-type-short-sleeve-shirt",
#     "top-type-long-sleeve-shirt",
#     "top-type-singlet",
#     "top-type-polo",
# ]
# csv_data = pd.read_csv('new_clean_predictedtops.csv')
# count = 0
# for i in range(len(csv_data)):
# 	x = csv_data.loc[i, top_styles]
# 	if (x.max()) < 1:
# 		csv_data['bottom-style-none'][i] = 1
# 		count += 1
# 	# 	print (csv_data['bottleneck_dir'][i])
# 	# print (csv_data['bottom-style-none'][i])
# print (count)
# csv_data.to_csv('bottoms.csv')



# '''change bottleneck_dir to dir'''
# path = 'predictedshoes.csv'
# data = pd.read_csv(path)
# data['dir'] = 0
# for i in range(len(data)):
# 	bot = data['bottleneck_dir'][i]
# 	new = bot[12:-4]
# 	print(new)
# 	data['dir'][i] = new
# data.to_csv('predictedshoes.csv')


'''adding bottleneck dir'''
'''
data = pd.read_csv('shirts.csv')

data['bottleneck_dir'] = data.index
for i in range(len(data)):
	tmp = data['image_name'][i]
	new = tmp.split('/')[1:]
	new = '/'.join(new)

	new = 'bottlenecks/'+new+'.txt'

	data['bottleneck_dir'][i] = new
	print (data['bottleneck_dir'][i])

print (data.to_csv('shirts.csv'))
'''




#SET SECONDARY-COLOR-NONE
### TODO: Add none column for sec color, add primary color for three items missing color
# csv_data = pd.read_csv('shoes.csv')
# csv_data['shoes-secondary-color-none'] = 0
# count = 0
# for i in range(len(csv_data)):
# 	x = csv_data.loc[i, keys.shoe_secondary_colours]
# 	if (x.max()) < 1:
# 		csv_data['shoes-secondary-color-none'][i] = 1
# 		count += 1
# 	print (csv_data['shoes-secondary-color-none'][i])
# print (count)
# csv_data.to_csv('shoes.csv')


# csv_data = pd.read_csv('shirts.csv')
# csv_data['top-secondary-color-none'] = 0
# count = 0
# for i in range(len(csv_data)):
# 	x = csv_data.loc[i, keys.top_secondary_colours]
# 	if (x.max()) < 1:
# 		csv_data['top-secondary-color-none'][i] = 1
# 		count += 1
# 	print (csv_data['top-secondary-color-none'][i])
# print (count)
# csv_data.to_csv('shirts.csv')

# csv_data = pd.read_csv('bottoms.csv')
# csv_data['bottom-secondary-color-none'] = 0
# count = 0
# for i in range(len(csv_data)):
# 	x = csv_data.loc[i, keys.bottom_secondary_colours]
# 	if (x.max()) < 1:
# 		csv_data['bottom-secondary-color-none'][i] = 1
# 		count += 1
	# print (csv_data['bottom-secondary-color-none'][i])
# print (count)
# csv_data.to_csv('bottoms.csv')


### creating denim csv
# csv_data = pd.read_csv('bottoms.csv')
# new_data = csv_data
# new_data = new_data[new_data['bottom-material-denim/jeans'] == 1]
# print (len(csv_data))
# print (len(new_data))
# print (csv_data[csv_data['bottom-material-denim/jeans'] == 1])
# new_data.to_csv('denims.csv')

# csv = pd.read_csv('tops.csv')
# new = csv[csv['top-type-long-sleeve-shirt'] == 1]
# print (len(new))
# new2 = csv[csv['top-type-short-sleeve-shirt'] == 1]
# new = new.append(new2)
# print (len(new))
# new.to_csv('newshirts.csv')


# new3 = csv[csv['top-type-long-sleeve-t-shirt'] == 1]
# new4 = csv[csv['top-type-short-sleeve-t-shirt'] == 1]
# new5 = csv[csv['top-type-singlet'] == 1]
# new6 = csv[csv['top-type-polo'] == 1]

# tshirts = new3.append(new4.append(new5.append(new6)))
# print (len(tshirts))
# tshirts.to_csv('t-shirts.csv')


# t_shirt_fits = [
#     "t-shirt-fit-slim-fit",
#     "t-shirt-fit-longline",
#     "t-shirt-fit-baggy",
#     "t-shirt-fit-regular"
# ]

# csv_data = pd.read_csv('t-shirts.csv')
# csv_data['t-shirt-fit-regular'] = 0
# count = 0
# for i in range(len(csv_data)):
# 	x = csv_data.loc[i, t_shirt_fits]
# 	if (x.max()) < 1:
# 		csv_data['t-shirt-fit-regular'][i] = 1
# 		count += 1
# 	print (csv_data['t-shirt-fit-regular'][i])
# print (count)
# csv_data.to_csv('t-shirts.csv')


# bottom_styles = [
#     "bottom-style-cargo",
#     "bottom-style-dress",
#     "bottom-style-chinos",
#     "bottom-style-sweatpants",
#     "bottom-style-none"
# ]

# csv_data = pd.read_csv('bottoms.csv')
# csv_data['bottom-style-none'] = 0
# count = 0
# for i in range(len(csv_data)):
# 	x = csv_data.loc[i, bottom_styles]
# 	if (x.max()) < 1:
# 		csv_data['bottom-style-none'][i] = 1
# 		count += 1
# 	# 	print (csv_data['bottleneck_dir'][i])
# 	# print (csv_data['bottom-style-none'][i])
# print (count)
# csv_data.to_csv('bottoms.csv')