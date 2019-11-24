import scipy.misc as misc
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft2, ifft2

def scale(X, lowest, highest):
    original_range = highest - lowest
    norm_fourier = (X-X.min(axis=0))*original_range
    denorm_fourier = X.max(axis=0) - X.min(axis=0)
    denorm_fourier[denorm_fourier==0] = 1
    return lowest + norm_fourier/denorm_fourier


inputImg = plt.imread('test.png')
fftImg = fft2(inputImg);

# Get Real Fourier image and export to 'real_img.png'
realImg = fftImg.real
rf_min = np.min(realImg)
for x in range(4):
    try:
        realImg[:,:,x] = scale(realImg[:,:,x], 0, 255)
    except:
        print("Image dont have alpha channel")

realImg = realImg.astype('uint8')
misc.imsave('real_img.png', realImg)

# Get Imaginary Fourier image and export to 'imaginary_img.png'
imaginaryImg = fftImg.imag
for x in range(4):
    try:
        imaginaryImg[:,:,x] = scale(imaginaryImg[:,:,x], 0, 255)
    except:
        print("Image dont have alpha channel")

imaginaryImg = imaginaryImg.astype('uint8')

misc.imsave('imaginary_img.png', imaginaryImg)
