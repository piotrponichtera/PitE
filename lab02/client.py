import socket
import random
import time


def Main():
	
	max_alt = 39000
	actual_alt = 0
	max_alt_period = 100
	mainloop = True
	approach = False
	
	
	host = "127.0.0.1"
	port = 5017
	
	soc = socket.socket()
	
	
	#krotka (host,port)
	soc.connect((host,port))
	data = soc.recv(1024).decode('utf-8')
	print(data)
	#message = input("ALT: ")
	
	while(mainloop):
		#if(message == "quit"):
		#	soc.send(message.encode('utf-8'))
		#	break;
		if(actual_alt < max_alt and approach == False):
			actual_alt = random.randint(actual_alt,actual_alt+100)
		elif(actual_alt >= max_alt and max_alt_period > 0 and approach == False):
			actual_alt = max_alt
			max_alt_period-=1
		elif(max_alt_period == 0 and approach == False):
			approach=True
		elif(approach and actual_alt > 100):
			actual_alt = random.randint(actual_alt-100,actual_alt)
		else:
			actual_alt =0
			mainloop = False
			

			
			
		

		#time.sleep(2)
		message =  str(actual_alt)
		print("--> Sending altitude: " + str(actual_alt) + "ft")
		soc.send(message.encode('utf-8'))
		data = soc.recv(1024).decode('utf-8')
		print("Recived from controller: " + str(data))

	message = "quit"
	soc.send(message.encode('utf-8'))
	soc.close()
	
if __name__ == "__main__":
	Main()
		
	
