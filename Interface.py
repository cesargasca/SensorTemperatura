from arduinoiface import Reader

import matplotlib.pyplot as plt
import numpy as np

# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')

azul = (.13,.7,.185)
azul_claro = (.14,.167,.255)
amarillo = (.232,.255,.14)


def live_plotter(x_vec,y1_data,line1,identifier='',pause_time=0.1):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)

        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)        
        #update plot label/title
        plt.xlim(0, 100)
        plt.ylim(0, 255)
        plt.ylabel('Temperatua')
        plt.title('Termometro: {}'.format(identifier))
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    # adjust limits if new data goes beyond bounds
    
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1


if __name__ == '__main__':
	r = Reader("COM3")
	'''while True:
		value = r.read()
		if value is None or value == -1:
			print("no c")
		else:
			print("VALUE: " + str(value))'''
	print("START ARDUINO")

	size = 100
	x_vec = np.linspace(0,100,size+1)[0:-1]
	y_vec = np.linspace(0,100,size+1)[0:-1]
	line1 = []
	valorAnterior = 0
	while True:
	    value = r.read()
	    if value is None or value == -1:
	    	print("no c")
	    	y_vec[-1] = valorAnterior
	    else:
	    	print("VALUE: " + str(value))
	    	y_vec[-1] = value
	    	valorAnterior = value
	    line1 = live_plotter(x_vec,y_vec,line1)
	    y_vec = np.append(y_vec[1:],0.0)