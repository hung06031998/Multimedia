import scipy.misc as misc
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft2, ifft2


def scale(X, lowest, highest):
    original_range = highest - lowest
    # normalize the Fourier image data ("stretch" the contrast)
    norm_fourier = (X-X.min(axis=0))*original_range
    denorm_fourier = X.max(axis=0) - X.min(axis=0)
    denorm_fourier[denorm_fourier==0] = 1
    return lowest + norm_fourier/denorm_fourier

print("Recovering image")
recoverImage = plt.imread('real_img.png').astype('complex128')
recoverImage.imag = plt.imread('imaginary_img.png')
recoverImage = ifft2(recoverImage).real
for x in range(4):
    try:
        recoverImage[:,:,x] = scale(recoverImage[:,:,x], 0, 255)
    except:
        print("Image dont have alpha channel")

recoverImage = recoverImage.astype('uint8')
misc.imsave('recover.png', recoverImage)
print("Recovered image and saved to 'rercover.png'")
