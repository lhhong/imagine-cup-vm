import sys
from RMPE.testing.python.config_reader import config_reader
from RMPE.testing.python.demo import getposture
import os
from tensorflow.python.platform import gfile
from progress.bar import Bar
# reading config file to set up posture detector
param, model = config_reader()


# Call this function on all photos with user's face. It will save the cropped clothes into somewhere.


# file_list = []
# file_glob = os.path.join(image_dir, '*.jpg')
# file_list.extend(gfile.Glob(file_glob))
# length = len(file_list)
# bar = Bar('cropping...', max=length)
# for image in file_list:
# 	getposture(image, param, model)
# 	bar.next()
# bar.finish()

image_dir = 'DEMO/groupphoto.jpg'

#image_dir = 'pics/1.jpg'
getposture(image_dir, param, model, 300, 400)
