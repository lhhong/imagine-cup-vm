import sys
from RMPE.testing.python.config_reader import config_reader

from RMPE.testing.python.demo import getposture

param, model = config_reader()


#modify this to loop through pictures, maybe
getposture('pics/jeans.jpg', param, model)