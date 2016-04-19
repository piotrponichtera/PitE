import socket
import subprocess


class FlightRecorderServer:
	def __init__(self):
		self.host = "127.0.0.1"
		self.port = 5033
		self.protocol = socket.getprotobyname('tcp')
		self.counter=0
		self.mainloop=True
		self.connect()
		self.welcome_msg()
		self.main()
		self.make_chart()
		self.disconnect()
		
		
	def connect(self):
		self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM,self.protocol)
		self.soc.bind((self.host,self.port))
		self.soc.listen(1)
	
	def welcome_msg(self):
		print("Welcome!")
		print("Plane Controller v123.42f")
		print("Waiting for connection...")

	def main(self):
		self.fp = open("chart.gp","w")
		while(self.mainloop):
			self.connection , self.address = self.soc.accept()
			print("Instruments connected correctly! " + str(self.address))
			self.welcome_message = "Report your flight parameters!"
			self.connection.send(self.welcome_message.encode('utf-8'))
			self.data_in = self.connection.recv(1024).decode('utf-8')
			print(str(self.data_in))
			while(True):
	
				# buffor 1024 bajty
				self.data_in = self.connection.recv(1024).decode('utf-8')
				if not self.data_in:
					break
				else:
					if(str(self.data_in) == "landed"):
						self.mainloop = False
						print("The plane has landed!")
						break
				
					self.data_out = "<-- Roger! Report further measurements!\n"
					print("--> Confirmation! \n"+ str(self.data_in))
				
					self.fp.write(str(self.counter) + " " + str(self.data_in).split()[27] + " " + str(self.data_in).split()[31] + " " + str(self.data_in).split()[35]  +  "\n")
					self.counter+=1
					self.connection.send(self.data_out.encode('utf-8'))
	
	
		self.connection.close()
		self.soc.close()
		self.fp.close()
		
		
	def make_chart(self):
		subprocess.Popen("gnuplot plot.gp", shell=True)
		print("Chart completed!")

	def disconnect(self):
		self.soc.close()
		print("Instrument disconnected!")
	

	

	

if __name__ == "__main__":
	FlightRecorderServer()
	
