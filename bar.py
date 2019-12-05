import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from arduinoiface import Reader
import random


color = "aqua"

def combin_to_temperature(com_bin):
	vsal = com_bin * (0.019607853)
	e2 = 5 - vsal
	deltaR = ((100000) - (20000*e2))/(10-e2)
	rsen = 10000-deltaR
	temperatura = (12000-rsen)/80
	return temperatura


def dynamicBar(t,performance,pause_time = 0.1):
	plt.ion()
	
	plt.clf()

	v = performance[0]
	if v > 24 and v < 50:
		color = "aqua"
	elif v > 50 and v <75:
		color = "yellow"
	elif v > 75 and v < 100:
		color = "orange"
	else:
		color = "red"
	plt.bar([" "], performance, align='center', color = color)

	#plt.xlim(0, 1)
	plt.ylim(0, 150)
	plt.ylabel('Temperatura °C')
	plt.title("VALOR: " + str(t) + "°C")
	plt.show()
	plt.pause(pause_time)

if __name__ == '__main__':
	#r = Reader("COM4")
	#print("START ARDUINO")
	valorAnterior = 0
	t = 0
	performance = [255]
	valorAnterior = 0
	r = Reader("COM3")
	print("START ARDUINO")
	while True:
		value = r.read()
		if value is None or value == -1:
		    	print("no c")
		    	performance[0] = t
		else:
			t = combin_to_temperature(value)
			print("VALUE: " + str(t))
			performance[0] = t
			t = performance[0]
		dynamicBar(t,performance)

		
		
		
