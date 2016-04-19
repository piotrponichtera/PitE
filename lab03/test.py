
import csv
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA


fp = open("epkk-epwa.csv" , "rt")
try:
	reader = csv.reader(fp)
	for row in reader:
		print(row)
finally:
	fp.close()
	
"""
fp =  open("epkk-epwa.csv" , "rt")
l = fp.readline()
print(l.split(','))
"""
categories_guard=True
fp = open("epkk-epwa.csv" , "rt")
reader = csv.reader(fp)
for row in reader:
	if(categories_guard):
		categories = row
		categories_guard=False
	else:
		for i in range(len(categories)):
			print(str(categories[i]) + " : " + str(row[i]))			
			
fp.close()

for i in categories:
	print(i)
