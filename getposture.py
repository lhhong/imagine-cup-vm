import sys
from RMPE.testing.python.config_reader import config_reader
from RMPE.testing.python.demo import getposture

param, model = config_reader()


# Call this function on all photos with user's face. It will save the cropped clothes into somewhere.
getposture('pics/group-photo-04.jpg', param, model)
