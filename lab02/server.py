import socket
import subprocess

def Main():
	host = "127.0.0.1"
	port = 5017
	
	soc = socket.socket()
	soc.bind((host,port))
	
	#sluchamy 1 polaczenie
	soc.listen(1)
	mainloop=True
	counter=0
	
	fp = open("chart.gp","w")
	print("Welcome!")
	print("Plane Controller v123.42f")
	
	
	while(mainloop):
		connection , address = soc.accept()
		print("Instrument connected correcylt! " + str(address))
		welcome_message = "Report your Altitude!"
		connection.send(welcome_message.encode('utf-8'))
		while(True):
	
			# buffor 1024 bajty
			data_in = connection.recv(1024).decode('utf-8')
			if not data_in:
				break
			else:
				if(str(data_in) == "quit"):
					mainloop = False
					print("Plane has landed!")
					break
				data_out = "Roger! Your altitude " + str(data_in) + "ft. Report further measurements!"
				
				print("Your altitude: " + str(data_in) +"ft")
				fp.write(str(counter) + " " + str(data_in) + "\n")
				counter+=1
				connection.send(data_out.encode('utf-8'))
	
	
	connection.close()
	soc.close()
	fp.close()
	fp2 = open("plot.gp", "w")
	fp2.write("set term png\n")
	fp2.write("set output \"chart.png\" \n")
	fp2.write("plot \"chart.gp\" with lines\n")
	fp2.close()	
	subprocess.Popen("gnuplot plot.gp", shell=True)
	print("Chart completed!")
	print("Instrument disconnected!")
	

if __name__ == "__main__":
	Main()
	
