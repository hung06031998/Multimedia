from PIL import Image
import numpy as np

img = Image.open('img.png')
print img.mode

rgba2grey = img.convert('LA')
rgba2grey.save('greyscale.png')


data = img.getdata()
r = [(d[0], 0, 0) for d in data]
g = [(0, d[1], 0) for d in data]
b = [(0, 0, d[2]) for d in data]
img_r = img.copy()
img_r.putdata(r)
img_r.save('redscale.png')

img_g = img.copy()
img_g.putdata(g)
img_g.save('greenscale.png')

img_b = img.copy()
img_b.putdata(b)
img_b.save('bluescale.png')

if img.mode == 'RGBA':
	img_a = img.copy()
	img_a.putalpha(128)
	img_a.save('alphascale.png')

R = Image.open('redscale.png').split()[0]
G = Image.open('greenscale.png').split()[1]
B = Image.open('bluescale.png').split()[2]

if img.mode == 'RGB':
	RGB = Image.merge("RGB",(R,G,B))
	RGB.save('merged.png')
else:
	A = Image.open('alphascale.png').split()[3]
	RGBA = Image.merge("RGBA",(R,G,B,A))
	RGBA.save('merged.png')
