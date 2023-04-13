import numpy as np
import time

def matrix_multiplier(n):
    """Return a randomly populated matrix of size n x n."""
    return np.random.randint(-100, 100, size=(n, n))

def classical_multiplication(matrix_a, matrix_b):
    """Return the result of matrix_a * matrix_b, calculated using classical matrix multiplication."""
    n = len(matrix_a)
    result = [[0 for x in range(n)] for y in range(n)]
    for i in range(n): 
        for j in range(n): 
            for k in range(n): 
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

def split(matrix):   
    """Split a matrix into four quadrants."""
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:] 

def strassen_multiplication(matrix_a, matrix_b): 
    """Return the result of matrix_a * matrix_b, calculated using Strassen's algorithm."""
    n = len(matrix_a)
    if n == 1: 
        return matrix_a * matrix_b
    # Recursively split the matrices into quadrants until the base case is reached. 
    a, b, c, d = split(matrix_a)
    e, f, g, h = split(matrix_b) 
    # Seven recursive calls 
    p = strassen_multiplication(a, f - h)   
    q = strassen_multiplication(a + b, h)         
    r = strassen_multiplication(c + d, e)         
    s = strassen_multiplication(d, g - e)
    t = strassen_multiplication(a + d, e + h)         
    u = strassen_multiplication(b - d, g + h)   
    v = strassen_multiplication(a - c, e + f)   
    # Compute the four quadrants of the result matrix
    c11 = t + s - q + u   
    c12 = p + q            
    c21 = r + s             
    c22 = p + t - r - v   
    # Combine the four quadrants 
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))  
    return c

def divide_conquer_multiplication(a, b):
    """Return the result of a * b, calculated using the divide-and-conquer method."""
    n = len(a)
    if n == 1:
        return a * b
    a11 = a[:n//2, :n//2]
    a12 = a[:n//2, n//2:]
    a21 = a[n//2:, :n//2]
    a22 = a[n//2:, n//2:]
    b11 = b[:n//2, :n//2]
    b12 = b[:n//2, n//2:]
    b21 = b[n//2:, :n//2]
    b22 = b[n//2:, n//2:]
    c11 = divide_conquer_multiplication(a11, b11) + divide_conquer_multiplication(a12, b21)
    c12 = divide_conquer_multiplication(a11, b12) + divide_conquer_multiplication(a12, b22)
    c21 = divide_conquer_multiplication(a21, b11) + divide_conquer_multiplication(a22, b21)
    c22 = divide_conquer_multiplication(a21, b12) + divide_conquer_multiplication(a22, b22)
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return c

def main(): 
    # n is both dimensions of each 2D array 
    classicalTotalTime = 0
    
    strassenTotalTime = 0
    
    divideConquerTotalTime = 0
    n = 8    
    
    # Looping
    # doubling the size of the matrices each time
    # while n <= 64:
    for x in range(0, 200):
        # This generates two randomly populated matrices.
        MatrixA = matrix_multiplier(n)
        MatrixB = matrix_multiplier(n)
        for y in range(0, 10):
       
            # This generates two randomly populated matrices.
            # MatrixA = matrixMultiplier(n)
            # MatrixB = matrixMultiplier(n)
        
            # This multiplies the matrices and times the operation.
            startTime = time.perf_counter_ns()
            classical_multiplication(MatrixA, MatrixB) 
            finishTime = time.perf_counter_ns()
        
            # Calculates the elapsed time in seconds.
            classicalTotalTime += ((finishTime - startTime) * (10**-9)) 
            
            # This multiplies the matrices and times the operation.
            startTime = time.perf_counter_ns()
            strassen_multiplication(MatrixA, MatrixB) 
            finishTime = time.perf_counter_ns()
        
            # Calculates the elapsed time in seconds.
            strassenTotalTime += ((finishTime - startTime) * (10**-9)) 
            
            # This multiplies the matrices and times the operation.
            startTime = time.perf_counter_ns()
            divide_conquer_multiplication(MatrixA, MatrixB) 
            finishTime = time.perf_counter_ns()
            
            # Calculates the elapsed time in seconds.
            divideConquerTotalTime += ((finishTime - startTime) * (10**-9)) 
            
            # instance and the corresponding time it took to multiply them.
            #Does the 200 data sets 10 times
            y+=1
           
        if y == 10:
           
           y=0
        #Prints every data set done 
        x+=1
        
        print(x)
        
    print("Classical Average Execution Time (sec.): \nFor n = ", f'{n:1,}', "   t = {:0.10f}".format(classicalTotalTime/2000))#, f'{period:.3}')
    print("Strassen Average Execution Time (sec.): \nFor n = ", f'{n:1,}', "   t = {:0.10f}".format(strassenTotalTime/2000))#, f'{period:.3}')
    print("Divide and Conquer Average Execution Time (sec.): \nFor n = ", f'{n:1,}', "   t = {:0.10f}".format(divideConquerTotalTime/2000))#, f'{period:.3}')
if __name__ == '__main__':
   main() 
    

