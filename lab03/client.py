import socket
import random
import time
import csv

class FlightRecorderClient:
	def __init__(self):
		self.host = "127.0.0.1"
		self.port = 5033
		self.protocol = socket.getprotobyname('tcp')
		self.mainloop = True
		self.categories_guard = True
		self.categories = []
		self.connect()
		self.main()
		
		
		
	def connect(self):
		self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, self.protocol)
		#krotka (host,port)
		self.soc.connect((self.host,self.port))
		self.data = self.soc.recv(1024).decode('utf-8')
		print(self.data)
		
		
	def main(self):
		self.message = "The plane has just taken off!"
		self.soc.send(self.message.encode('utf-8'))
		self.fp = open("hamburg_istanbul.csv" , "rt")
		self.reader = csv.reader(self.fp)
		for row in self.reader:
			if(self.categories_guard):
				self.categories = row
				self.categories_guard = False
			else:
				self.message = "Actual flight parameters:\n"
				print("Reporting!")
				#time.sleep(1)
				for i in range(len(self.categories)):
					print("--> " + str(self.categories[i]) + " : " + str(row[i]))
					self.message += "<-- " + str(self.categories[i]) + " : " + str(row[i])+"\n"
				
				self.soc.send(self.message.encode('utf-8'))
				print()
				self.data = self.soc.recv(1024).decode('utf-8')
				print(self.data)
		self.fp.close()
		
		print("Final approach!")
		print("Landed safe and sound!")
		self.message = "landed"
		self.soc.send(self.message.encode('utf-8'))
		self.disconnect()
		
		
	def disconnect(self):
		self.soc.close()
		print("Disconnected!")
		

	
if __name__ == "__main__":
	FlightRecorderClient()
		
	
