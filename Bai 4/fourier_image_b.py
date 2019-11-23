import cv2
import numpy as np
from matplotlib import pyplot as plt
import scipy.misc as misc
img = cv2.imread('outfile.jpg',0)
#f = np.fft.fft2(img)

#fshift = np.fft.fftshift(f)
#magnitude_spectrum = 20*np.log(np.abs(fshift))

f_ishift = np.fft.ifftshift(img)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

misc.imsave('outfile_back_2.jpg', img_back)
plt.title('Reconstructed image'),plt.xticks([]), plt.yticks([])
plt.show()
