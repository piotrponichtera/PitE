		
"""
	klasa odpowiedzialna za wczytywanie opcji menu i równań
	zawiera funkcje wczytującą opcje w menu oraz wczytującą równania
	
"""			
class InputReader:
	def menu_loader(self):
		option = input("Wybieram: ")
		return option
		
	def eq_option_loader(self):
		option = input("Naciśnij 1 aby potwierdzić poprawność równania\n"
			"Naciśnij dowolny klawisz aby wczytać rownanie jeszcze raz\n"
			"Wybieram : ")
		return option
		
	def equation_loader(self):
		value=0.
		equation = []
		
		while(True):
			try:
				value = input("Podaj współczynniki X równania : ")
				equation.append(float(value))
				break;
			except ValueError:
				print("Podaj wartość zmiennoprzecinkową!")
		while(True):
			try:
				value = input("Podaj współczynniki Y równania : ")
				equation.append(float(value))
				break;
			except ValueError:
				print("Podaj wartość zmiennoprzecinkową!")
		while(True):
			try:
				value = input("Podaj współczynniki Z równania : ")
				equation.append(float(value))
				break;
			except ValueError:
				print("Podaj wartość zmiennoprzecinkową!")
		
		return equation

