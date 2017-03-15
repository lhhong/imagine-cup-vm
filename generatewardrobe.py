from RMPE.testing.python.config_reader import config_reader
from RMPE.testing.python.demo import getposture
from Classification.getfeatures import predict
import urllib
from Face import faceapi


param, model = config_reader()


def main(image_list, personId, personGroupId):
	### image_list is a list of urls
	image_dir = 'userpics'
	images = []
	for i in range(len(image_list)):
		coords = faceapi.check_photo(image_list[i], personId, personGroupId)
		if coords is not None:
			image_path = image_dir+'/'+str(i)+'.jpg'
			urllib.urlretrieve(image_list[i], image_path)
			face_x = coords[1]+coords[2]/2
			face_y = coords[0]+coords[3]/2
			getposture(image_path, param, model, face_x, face_y)

	predict(image_dir)

if __name__ == '__main__':
	main(['https://jafrianews.files.wordpress.com/2012/05/russian-president-putin-with-vladimir-putin-may-7-2012.jpg', 'http://america.aljazeera.com/content/ajam/opinions/2014/3/vladimir-putin-ukrainerussiacrimeainternationallaw/jcr:content/mainpar/adaptiveimage/src.adapt.960.high.putin_ukraine_doctrine-1a.1394060261398.jpg'], 'b00c6a39-7807-4cf2-9a04-6b41f2efcf18', 'putin')