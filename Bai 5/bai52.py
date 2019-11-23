import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

fig, ax = plt.subplots(figsize=(6, 6))

for x in range(3001):
    if x < 501 :
        c1='red' #blue
        c2='orange' #green
        ax.axvline(x, color=colorFader(c1,c2,x/500), linewidth=0.5)
    if 500 < x < 1001:
        c1='orange' #blue
        c2='yellow' #green
        ax.axvline(x, color=colorFader(c1,c2,(x-500)/500), linewidth=0.5)
    if 1000 < x < 1501:
        c1='yellow' #blue
        c2='green' #green
        ax.axvline(x, color=colorFader(c1,c2,(x-1000)/500), linewidth=0.5)
    if 1500 < x < 2001:
        c1='green' #blue
        c2='blue' #green
        ax.axvline(x, color=colorFader(c1,c2,(x-1500)/500), linewidth=0.5)
    if 2000 < x < 2501:
        c1='blue' #blue
        c2='indigo' #green
        ax.axvline(x, color=colorFader(c1,c2,(x-2000)/500), linewidth=0.5)
    if 2500 < x < 3001:
        c1='indigo' #blue
        c2='violet' #green
        ax.axvline(x, color=colorFader(c1,c2,(x-2500)/500), linewidth=0.5)

fig, ax = plt.subplots(figsize=(6, 6))

for x in range(3001):
    if x < 501 :
        c1='red' #blue
        c2='orange' #green
        ax.axhline(x, color=colorFader(c1,c2,x/500), linewidth=0.5)
    if 500 < x < 1001:
        c1='orange' #blue
        c2='yellow' #green
        ax.axhline(x, color=colorFader(c1,c2,(x-500)/500), linewidth=0.5)
    if 1000 < x < 1501:
        c1='yellow' #blue
        c2='green' #green
        ax.axhline(x, color=colorFader(c1,c2,(x-1000)/500), linewidth=0.5)
    if 1500 < x < 2001:
        c1='green' #blue
        c2='blue' #green
        ax.axhline(x, color=colorFader(c1,c2,(x-1500)/500), linewidth=0.5)
    if 2000 < x < 2501:
        c1='blue' #blue
        c2='indigo' #green
        ax.axhline(x, color=colorFader(c1,c2,(x-2000)/500), linewidth=0.5)
    if 2500 < x < 3001:
        c1='indigo' #blue
        c2='violet' #green
        ax.axhline(x, color=colorFader(c1,c2,(x-2500)/500), linewidth=0.5)
plt.show()