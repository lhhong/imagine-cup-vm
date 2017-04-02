import csv

# with open('test.csv', 'a', newline='') as csvfile:
# # dataWriter = csv.DictWriter(csvfile, fieldnames=retrieveFieldNames(clothing_type), restval=0, lineterminator='\n')
# # if not file_exists:
# # 	dataWriter.writeheader()  # file doesn't exist yet, write a header
# # dataWriter.writerow(data)

# 	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 	writer.writerow([1,0,1])
import numpy as np
x = np.array([1,0,1])
y = [1,1]
print (x+y)
print (x.shape)