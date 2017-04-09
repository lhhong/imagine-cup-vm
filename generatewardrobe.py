from RMPE.testing.python.config_reader import config_reader
from RMPE.testing.python.demo import getposture
from predict import feed_dir
import urllib
from Face import faceapi
from Face import bytesfaceapi
import os
import ast
from PIL import Image


param, model = config_reader()


def generatewardrobe(image_list, personId, personGroupId, time):
	### image_list must be a list of urls
	image_list = ast.literal_eval(str(image_list))
	image_dir = 'USERS/'+personId+' wardrobe'
	if not os.path.isdir('bottlenecks/'+image_dir):
		os.mkdir('bottlenecks/'+image_dir)
	if not os.path.isdir(image_dir):
		os.mkdir(image_dir)

	image_dir = image_dir+'/'+time
	if not os.path.isdir(image_dir):
		os.mkdir(image_dir)

	path = 'wardrobe_candidate.jpg'
	for i in range(len(image_list)):
		urllib.urlretrieve(image_list[i], path)
		pic = Image.open(path)
		pic.save(path,quality=50,optimize=True)
		with open(path, 'rb') as imageFile:
			f = imageFile.read()
			b = bytearray(f)

		coords = bytesfaceapi.check_photo(b, personId, personGroupId)
		#coords = faceapi.check_photo(image_list[i], personId, personGroupId)
		coords = ast.literal_eval(str(coords))
		print (coords)
		if coords is not None:
			image_path = os.path.join(image_dir, str(i)+'.jpg')
			#image_dir+'/'+str(i)+'.jpg'
			urllib.urlretrieve(image_list[i], image_path) # saves image to user's folder, to be returned later in feed_dir
			# pic = Image.open(image_path)
			# pic.save(image_path,quality=40,optimize=True)
			face_x = coords[1]+coords[2]/2
			face_y = coords[0]+coords[3]/2
			getposture(image_path, param, model, face_x, face_y)

	x = feed_dir(image_dir)
	# print (x)
	return x

if __name__ == '__main__':
	a = generatewardrobe(['https://jafrianews.files.wordpress.com/2012/05/russian-president-putin-with-vladimir-putin-may-7-2012.jpg', 
					'http://america.aljazeera.com/content/ajam/opinions/2014/3/vladimir-putin-ukrainerussiacrimeainternationallaw/jcr:content/mainpar/adaptiveimage/src.adapt.960.high.putin_ukraine_doctrine-1a.1394060261398.jpg'], 
					'b00c6a39-7807-4cf2-9a04-6b41f2efcf18', 
					'putin', '2017-04-08 20:26')

	# a = generatewardrobe(["http://static.guim.co.uk/sys-images/Guardian/Pix/pictures/2015/10/3/1443892812592/Vladimir-Putin--009.jpg"], 
	# 				'cd09435a-c73b-4df2-888a-31af70a8a2f1', 
	# 				'jiarui', '2017-04-08 20:26')

	a = str(a)
	print (a)

	# generatewardrobe(["http://www.thewrap.com/wp-content/uploads/2015/11/Donald-Trump.jpg"], 
	# 				'b00c6a39-7807-4cf2-9a04-6b41f2efcf18', 
	# 				'putin')
