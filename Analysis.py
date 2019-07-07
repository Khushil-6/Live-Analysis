import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

def animate(i):
	data = pd.read_csv(r"C:\\Users\\khush\\PycharmProjects\\Data Generator\\data.csv")
	x = data['xvalue']
	y1 = data['newValue_1']
	y2 = data['newValue_2']

	plt.cla()

	plt.plot(x, y1, label = 'Data 1')
	plt.plot(x, y2, label = 'Data 2')
	plt.legend(loc = 'upper left')
	plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.show()
