#!/usr/bin/python3


# importowane moduły
from Solver import *
from InputValidator import *
from InputReader import *
import numpy
import subprocess
from time import gmtime, strftime


"""
	główna klasa
	zawiera funkcje odpowiedzialną za działanie całego programu oraz funkcje wypisującą historię użytkowania programu
"""
class ApplicationMgr:
	#konstruktor
	def __init__(self):
		self.inputvaludator = InputValidator()
		self.inputreader = InputReader()
		self.solver = Solver()
		print("Witaj w programie!")
		self.run()
		
	def history(self):
		try:
			fp = open("history.txt", "r")
			lines = fp.readlines()
			for line in lines:
				print(line,end="")
			fp.close()
		except FileNotFoundError:
			print("Brak historii")
			return
		
		
	def run(self):
		menuinput=""
		option=1
		equations_list = []
		#główna pętla programu
		while( True ):
		
			#zmienne odpowiedzialne za działanie pętli w których wczytywane są równania
			eq1_loop, eq2_loop = True,True
			#listy zawierające współczynniki równania
			eq1,eq2=[],[]
			print("Wybierz --1-- aby rozwiązać równanie")
			print("Wybierz --2-- aby wyswietlic historie rozwiazan")
			print("Wybierz --q-- aby wyjść")
			#wczytywanie opcji wybranej przez yżytkownika
			menuinput = self.inputreader.menu_loader()
			#print(menuinput)
			
			#wybór działania w zależności od wyboru użytkownika
			if(menuinput == 'q'):
				break
			elif(menuinput == str(2)):
				self.history()
			elif( menuinput != str(1)):
				print("Nie ma takiej opcji!")
				
			else:
				#pętla w której użytkownik podaje pierwsze równanie
				while(eq1_loop):
					print("Pierwsze równanie:")
					#wczytywanie współczynników rownania
					eq1 = self.inputreader.equation_loader()
					print("Wczytano równanie: " + str(eq1[0]) + 
						"x + " + str(eq1[1]) + "y = " + str(eq1[2]))
					print("Zatwierdź równanie lub podaj je jeszcze raz")
					#wczytywanie działania podanego przez użytkownika
					option = self.inputreader.eq_option_loader()
					#print(option)
					if(option == str(1)):
						eq1_loop=False
				#pętla w ktorej użytkownik podaje drugie równanie
				while(eq2_loop):
					print("Drugie równanie:")
					eq2 = self.inputreader.equation_loader()
					print("Wczytano równanie: " + str(eq2[0]) + 
						"x + " + str(eq2[1]) + "y = " + str(eq2[2]))
					print("Zatwierdź równanie lub podaj je jeszcze raz")
					option = self.inputreader.eq_option_loader()
					#print(option)
					if(option == str(1)):
						eq2_loop=False
				print("Wczytane równania")
				#wypis wczytanych równań
				self.inputvaludator.print_equation(eq1)
				self.inputvaludator.print_equation(eq2)
	
				#zapis rozwiązania 
				result = self.solver.solve(eq1,eq2)
				#wychwycenie gdy podany układ ma nieskończenie wiele rozwiązań lub jest sprzeczny
				if(result is -1):
					print("Układ ma nieskończenie wiele rozwiązań lub jest sprzeczny")
				else:
					#wypis rozwiązania układu
					self.inputvaludator.print_result(result)
					#generowanie wykresu
					self.solver.plot_chart(eq1,eq2)
					#zapis do historii działania programu
					self.solver.save_data(eq1,eq2,result)
					
					
					
					
		#komunikat na zakończenie programu
		print("Żegnaj!")
		




#stworzenie obiektu klasy jest równoznaczne z odpaleniem funkcji run(), która odpowiada za działanie całej aplikacji
a = ApplicationMgr()

