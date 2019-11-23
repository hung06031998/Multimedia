import cv2
import numpy as np
from matplotlib import pyplot as plt
import scipy.misc as misc

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image',
    help="get image path")
args = parser.parse_args()
img = cv2.imread(args.image, 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
misc.imsave('outfile.jpg', magnitude_spectrum)
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.subplot(133), plt.imshow(img_back, cmap = 'gray')
misc.imsave('outfile_back.jpg', img_back)
plt.title('Reconstructed image'),plt.xticks([]), plt.yticks([])
plt.show()
