from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as misc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image',
    help="get image path")
args = parser.parse_args()

# open an image
img = Image.open(args.image).convert('L')
# load the image data into a numpy array
img_data = np.asarray(img)
# perform the 2-D fast Fourier transform on the image data
fourier = np.fft.fft2(img_data)

fshift = np.fft.fftshift(fourier)
# compute the magnitudes (absolute values) of the complex numbers
fourier = np.abs(fshift)
# compute the common logarithm of each value to reduce the dynamic range
fourier = 2*np.log10(fourier)
# convert the data into an image
magnitude_spectrum = Image.fromarray(fourier)

# get the image back
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(221),plt.imshow(Image.open(args.image).convert('RGBA'))
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.imshow(img, cmap = 'gray')
plt.title('Gray scale'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(magnitude_spectrum, cmap = 'gray')
misc.imsave('magnitude_spectrum.jpg', magnitude_spectrum)
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.subplot(224), plt.imshow(img_back, cmap = 'gray')
misc.imsave('reconstructed.jpg', img_back)
plt.title('Reconstructed image'),plt.xticks([]), plt.yticks([])
plt.show()
