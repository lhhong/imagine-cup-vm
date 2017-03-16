from RMPE.testing.python.config_reader import config_reader
from RMPE.testing.python.demo import getposture
from Classification.getfeatures import predict
import urllib
from Face import bytesfaceapi
import base64


param, model = config_reader()


def generatewardrobe(image_list, personId, personGroupId):
	### image_list is a list of urls
	image_dir = 'userpics'

	for i in range(len(image_list)):
		coords = bytesfaceapi.check_photo(image_list[i], personId, personGroupId)
		if coords is not None:
			image_path = image_dir+'/'+str(i)+'.jpg'
			print image_list[i]

			with open(image_path, "wb") as img:
				img.write(image_list[i])

			face_x = coords[1]+coords[2]/2
			face_y = coords[0]+coords[3]/2
			getposture(image_path, param, model, face_x, face_y)

	predict(image_dir)

if __name__ == '__main__':
	arr = []
	with open("photo.jpg", "rb") as imageFile:
		f = imageFile.read()
		b = bytearray(f)
		print (len(b))
		arr.append(b)

	generatewardrobe(arr, 'b00c6a39-7807-4cf2-9a04-6b41f2efcf18', 'putin')
