import numpy as np
#length of x_n > length of h_n
x_n = [1,2,3]
h_n = [1,1]

if len(h_n) > len(x_n):
	print "Length of x_n must > length h_n"
else:
	h = np.zeros(len(x_n)) #padding h with zeros up to len(x_n), create vector h with length = length of x_n
	for i in np.arange(0, len(x_n)): #np.arange(): create array with value from 0 ->  length of x_n - 1
	    if i < len(h_n):
	        h[i] = h_n[i]
	hh = np.array(h) #copy h and assign for hh
	hh = np.tile(hh,2) # duplicate hh
	z_n = np.convolve(x_n,hh)#Linear convolve x_n with hh
	z_n = z_n[len(x_n): (len(z_n) - (len(x_n) - 1))] # Get z by cut array from len(x_n) to len(z_n) - (len(x_n) -1)
	print
	print "Cyclic Convolution from Linear Convolution: z_n = ",z_n
	print