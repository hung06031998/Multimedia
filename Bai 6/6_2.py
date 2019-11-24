import numpy as np

x_n = [1,2,3]
h_n = [1,1]

print
print "Cyclic Convolution use Numpy's Function: Not support"

w = len(x_n)
matrix = np.zeros((w,w)) #create matrix all value by zero with w row and w column

for i in np.arange(0, w):
        if i < len(h_n)-1:
            for j in np.arange(i, -1, -1):
                matrix[i][j] = h_n[i-j]
            for j in np.arange(w+i-len(h_n)+1, w):
                matrix[i][j] = h_n[w-j+i]
                
        else:
            for j in np.arange(i, i-len(h_n), -1):
                matrix[i][j] = h_n[i-j]
print
print "Cyclic Convolution caculate manual: z_n =", np.matmul(matrix,x_n)# multiply matrix with vector
print