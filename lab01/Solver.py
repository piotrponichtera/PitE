import subprocess
from time import gmtime, strftime
import numpy
		
"""
	klasa odpowiedzialna za rozwiązanie układu, rysowanie wykresu oraz zapis historii użytkowania programu
	zawiera funkcje, która rozwiązuje układ równań, tworzy wykres za pomocą Gnuplot'a oraz zapisuje datę użycia, wczytane równania i ich rozwiązanie do pliku
	
"""
class Solver:
	#funkcja w której rozwiązywany jest układ równań
	def solve(self,eq1,eq2):
		#left = numpy.array(list(map(lambda x,y:[x,y],eq1[:len(eq1)-1],eq2[:len(eq2)-1])))
		#left = numpy.array(list(zip(eq1[:len(eq1)-1],eq2[:len(eq2)-1])))
		left = numpy.array([eq1[:len(eq1)-1],eq2[:len(eq2)-1]])
		right = numpy.array([eq1[len(eq1)-1:],eq2[len(eq2)-1:]])
		
		#print(left)
		#print(right)
		try:
			result = numpy.linalg.solve(left,right)
			return result
		except numpy.linalg.linalg.LinAlgError:
			return -1

	#funkcje w której tworzony jest plik potrzebny do generacji wykresu oraz sam wykres (wykres tworzony w gnuplocie)
	def plot_chart(self,eq1,eq2):
		fp = open("chart.gp", "w+")
		fp.write("set term png\n")
		fp.write("set output \"chart.png\" \n")
		fp.write("plot " + str(-eq1[0]/eq1[1]) + "*x +" + str(eq1[2]/eq1[1]) + ", "
		+ str(-eq2[0]/eq2[1]) + "*x +" + str(eq2[2]/eq2[1]))
		fp.close()
		subprocess.Popen("gnuplot chart.gp", shell=True)
		print("Wykres gotowy!")
		
	#funkcja dodająca do pliku z historią użytkowania kolejeny wpis
	# zapisuje: datę, równania oraz rozwiązanie
	#jest używana tylko w przypadku, gdy układ ma rozwiązanie
	def save_data(self,eq1,eq2,result):
		fp = open("history.txt", "a+")
		fp.write(strftime("%a, %d %b %Y %X\n", gmtime()))
		fp.write((str(eq1[0]) + "x + " + str(eq1[1]) + "y = " + str(eq1[2]))+"\n")
		fp.write((str(eq2[0]) + "x + " + str(eq2[1]) + "y = " + str(eq2[2])) +"\n")
		fp.write("x = " + str(result[0][0]) + "\ny = " + str(result[1][0]) + "\n\n")
		fp.close()
		
