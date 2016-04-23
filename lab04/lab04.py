import random # do szumow
import math # do sinusa
import subprocess #do plotowania
from scipy.optimize import curve_fit # do fitowania 
import matplotlib.pyplot as plt # do wykresu
from scipy import asarray as ar,exp # do obliczen
from scipy.stats import chisquare # chisquare test - poziom jakosci dofitowania
import scipy


class Data_generator:
	def __init__(self):
		self.x = []
		self.y = []
		self.noice_level = float(input("Podaj poziom szumow: "))
		
	def Generate(self):
		for i in range(0,90):
			self.x.append(i/30.)
			self.y.append(math.sin(i/30.)+random.uniform \
				(-self.noice_level,self.noice_level))
		self.x = ar(self.x)
		self.y = ar(self.y)
		
	def get_x(self):
		return self.x
	def get_y(self):
		return self.y
		
	
class Fitter:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.popt = []
		self.pcov = []
	def Fit(self):
		n = len(self.x)    
		mean = sum(self.x * self.y)/n            
		sigma = sum(self.y*(self.x-mean)**2)/n   

		def gaus(x,a,x0,sigma):
  			return a*exp(-(x-x0)**2/(2*sigma**2))

		self.popt, self.pcov = curve_fit(gaus,self.x,self.y,p0=[1,mean,sigma])
		
	def get_x(self):
		return self.x
	def get_y(self):
		return self.y
	def get_popt(self):
		return self.popt
	def get_pcov(self):
		return self.pcov
	def get_gaus(self):
		return self.gaus

	
class Plotter:
	def __init__(self, x, y, popt, pcov):
		self.x = x
		self.y = y
		self.popt = popt
		self.pcov = pcov
	
	def gaus(self, x,a,x0,sigma):
  			return a*exp(-(x-x0)**2/(2*sigma**2))
  			
	def Plot(self):
		plt.plot(self.x,self.y,'ro',label='punkty')
		plt.plot(self.x,self.gaus(self.x,*(self.popt)),label='fit')
		plt.legend()
		plt.title('Punkty oraz dofitowany do nich wykres')
		plt.xlabel('oś x')
		plt.ylabel('oś y')
		#plt.show()
		plt.savefig("chart.png")
		print("Wykres gotowy!")	
		
		
class StatAnalyser:
	def __init__(self, x, y, popt):
		self.x = x
		self.y = y
		self.popt = popt
		self.n = len(self.x)
		self.mean = sum(self.x * self.y)/self.n
		self.sigma = sum(self.y*(self.x-self.mean)**2)/self.n 
	
	def gaus(self, x,a,x0,sigma):
  		return a*exp(-(x-x0)**2/(2*sigma**2))
  		
	def Analyse(self):
		list4chi = []
		for i in self.x:
			list4chi.append(self.gaus(i, *(self.popt)))
		res = chisquare(list4chi)
		print("Parametry testu Chi-Square:")
		print("\t" + str(res[0]) + ", " + str(res[1]))
  		
  		
  		
  		
d = Data_generator()
d.Generate()

f = Fitter(d.get_x(), d.get_y())
f.Fit()

p = Plotter(f.get_x(), f.get_y(), f.get_popt(), f.get_pcov)
p.Plot()

s = StatAnalyser(f.get_x(), f.get_y(), f.get_popt())
s.Analyse()









