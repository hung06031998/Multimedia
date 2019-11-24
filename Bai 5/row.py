import matplotlib.pyplot as plt

from matplotlib import cm
from numpy import linspace

start = 0.0
stop = 1.0
number_of_lines= 5000
cm_subsection = linspace(start, stop, number_of_lines) 

colors = [ cm.gist_rainbow(x) for x in cm_subsection ]

for i, color in enumerate(colors):
    plt.axhline(i, color=color)

plt.ylabel('Line Number')
plt.show()
