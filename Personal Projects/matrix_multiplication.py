import numpy as np
import time

def matrixMultiplier(n):
        return np.random.randint(-100,100, size=(n, n))

def classicalMultiplication(matrixA, matrixB):

    result = [[0 for x in range(len(matrixA))] for y in range(len(matrixB))]
        
    for i in range(len(matrixA)): 
        for j in range(len(matrixB[0])): 
            for k in range(len(matrixB)): 
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    return result

def split(matrix):   
    row, col = matrix.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], \
        matrix[row2:, :col2], matrix[row2:, col2:] 

# Compute the matrix using Strassen

def strassenMultiplication(matrixA, matrixB): 
   
    if len(matrixA) == 1: 
        return matrixA * matrixB
  
    # Recursively splits the matrices into quadrants 
    # until the base case is reached. 
    a, b, c, d = split(matrixA)
    e, f, g, h = split(matrixB) 
  
    # Seven recursive calls 
    P = strassenMultiplication(a, f - h)   
    Q = strassenMultiplication(a + b, h)         
    R = strassenMultiplication(c + d, e)         
    S = strassenMultiplication(d, g - e)
    T = strassenMultiplication(a + d, e + h)         
    U = strassenMultiplication(b - d, g + h)   
    V = strassenMultiplication(a - c, e + f)   
  
    # Matrix C
    c11 = T + S - Q + U   
    c12 = P + Q            
    c21 = R + S             
    c22 = P + T - R - V   
  
    # This combines the four quadrants 
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))  
  
    return c

def divideConquerMultiplication(a, b):
    n = len(a)
    if n == 1:
        return a * b
    else:
        a11 = a[:int(len(a) / 2), :int(len(a) / 2)]
        a12 = a[:int(len(a) / 2), int(len(a) / 2):]
        a21 = a[int(len(a) / 2):, :int(len(a) / 2)]
        a22 = a[int(len(a) / 2):, int(len(a) / 2):]

        b11 = b[:int(len(b) / 2), :int(len(b) / 2)]
        b12 = b[:int(len(b) / 2), int(len(b) / 2):]
        b21 = b[int(len(b) / 2):, :int(len(b) / 2)]
        b22 = b[int(len(b) / 2):, int(len(b) / 2):]

        c11 = divideConquerMultiplication(a11, b11) + divideConquerMultiplication(a12, b21)
        c12 = divideConquerMultiplication(a11, b12) + divideConquerMultiplication(a12, b22)
        c21 = divideConquerMultiplication(a21, b11) + divideConquerMultiplication(a22, b21)
        c22 = divideConquerMultiplication(a21, b12) + divideConquerMultiplication(a22, b22)

        result = np.zeros((n, n))
        result[:int(len(result) / 2), :int(len(result) / 2)] = c11
        result[:int(len(result) / 2), int(len(result) / 2):] = c12
        result[int(len(result) / 2):, :int(len(result) / 2)] = c21
        result[int(len(result) / 2):, int(len(result) / 2):] = c22
    return result

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
        MatrixA = matrixMultiplier(n)
        MatrixB = matrixMultiplier(n)
        for y in range(0, 10):
       
            # This generates two randomly populated matrices.
            # MatrixA = matrixMultiplier(n)
            # MatrixB = matrixMultiplier(n)
        
            # This multiplies the matrices and times the operation.
            startTime = time.perf_counter_ns()
            classicalMultiplication(MatrixA, MatrixB) 
            finishTime = time.perf_counter_ns()
        
            # Calculates the elapsed time in seconds.
            classicalTotalTime += ((finishTime - startTime) * (10**-9)) 
            
            # This multiplies the matrices and times the operation.
            startTime = time.perf_counter_ns()
            strassenMultiplication(MatrixA, MatrixB) 
            finishTime = time.perf_counter_ns()
        
            # Calculates the elapsed time in seconds.
            strassenTotalTime += ((finishTime - startTime) * (10**-9)) 
            
            # This multiplies the matrices and times the operation.
            startTime = time.perf_counter_ns()
            divideConquerMultiplication(MatrixA, MatrixB) 
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
    

