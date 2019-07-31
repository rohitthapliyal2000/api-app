import os
import csv
from .models import Bank
from api.settings import BASE_DIR

file_path = os.path.join(BASE_DIR, 'app/bank_branches.csv')

with open(file_path) as f:
	reader = csv.reader(f)
	counter = 0

	for read in reader:
		if counter == 0:
			counter = 1
			continue
		if counter == 1000:
			break

		Bank.objects.create(
			ifsc=read[0], 
			bank_id=read[1], 
			branch=read[2], 
			address=read[3], 
			city=read[4], 
			district=read[5], 
			state=read[6], 
			bank_name=read[7]
		)
		counter += 1
