import numpy as np

x_n = [1,2,3]
h_n = [1,1]
start = 0
end = 0
print
print "Linear Convolution use Numpy's Function: y_n =",np.convolve(x_n, h_n)

N = len(x_n) + len(h_n) - 1
w = len(x_n)
matrix = np.zeros((N,w)) # create matrix all value by zero with N row and w column
matrix[0][0] = h_n[0]

i = 1 
while i <= len(np.arange(1,N)): # create array with value from 1 -> N
        start = i
        if i >= len(h_n):
            if i <= len(x_n)-1:
                end = i - len(h_n)+1
            else:
                start = len(x_n)-1
                end = i-len(h_n)+1

        for j in np.arange(start, end-1, -1):
            if w > i:
                matrix[i][j] = h_n[start-j]
            else:
                matrix[i][j] = h_n[start-j+1+i-w]
                
	i+=1    
print
print "Linear Convolution caculate manual: z_n =",np.matmul(matrix,x_n) # multiply matrix with vector
print