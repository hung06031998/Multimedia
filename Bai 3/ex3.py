from PIL import Image
import numpy as np

img = Image.open('rgba.png')

rgba2grey = img.convert('LA')
rgba2grey.save('rgba2grey.png')


data = img.getdata()
r = [(d[0], 0, 0) for d in data]
g = [(0, d[1], 0) for d in data]
b = [(0, 0, d[2]) for d in data]
img_r = img.copy()
img_r.putdata(r)
img_r.save('rgba2red.png')

img_g = img.copy()
img_g.putdata(g)
img_g.save('rgba2green.png')

img_b = img.copy()
img_b.putdata(b)
img_b.save('rgba2blue.png')

if img.mode == 'RGB':
	img = img.convert('RGBA')

img.putalpha(128)
img.save('rgba2alpha.png')

R = Image.open('rgba2red.png').split()[0]
G = Image.open('rgba2green.png').split()[1]
B = Image.open('rgba2blue.png').split()[2]
A = Image.open('rgba2alpha.png').split()[3]
RGBA = Image.merge("RGBA",(R,G,B,A))
RGBA.save('rgba_merged.png')
