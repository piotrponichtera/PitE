		
"""
	klasa odpowiedzialna za walidacje danych
	zawiera funkcje walidujące wybór opcji w menu i wczytane równania oraz wypisujące równania i wynik

"""
class InputValidator:	
	def check_menu(self,option):
		if(option == str(1) or option == 'q'):
			return option
		else:
			return 0
	
	def check_eq_load(self,option):
		if(option == str(1)):
			return option
		else:
			return 0
			
	def print_equation(self,eq1):
		print(str(eq1[0]) + "x + " + str(eq1[1]) + "y = " + str(eq1[2]))
		
	def print_result(self,result):
		print("Rozwiązaniem układu jest:\n"
						"x = " + str(result[0][0]) + "\ny = " + str(result[1][0]))
