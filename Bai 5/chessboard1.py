import numpy as np
import matplotlib.pyplot as plt


def chessboard():
    M = np.zeros((8, 8))

    for i in np.arange(0, 8):
        for j in np.arange(0, 8):
            M[i, j] = (i + j) % 2
    return M


M = chessboard()
plt.imshow(M, cmap='binary')
plt.show()