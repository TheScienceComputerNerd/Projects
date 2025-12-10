# Module file that contains all python matrix functions

def matrixMult(rmatrix, cmatrix): # Only calculates for 2x2 matrices or above, 1x1 matrix calc not needed
   # rmatrix is the matrix by rows
   # cmatrix is the matrix by columns
   m = len(rmatrix)    # Rows in rmatrix
   p = len(cmatrix[0]) # Columns in cmatrix
   n = len(rmatrix[0]) # Length of row in rmatrix == Length of column in cmatrix == n, or wouldn't work
   if n != len(cmatrix[0]):
       return None

   nmatrix = [[0 for i in range(p)] for j in range(m)]
   for i in range(m): # For row in rmatrix
       for j in range(p): # For column in cmatrix
           for k in range(n): # For the length of each row in rmatrix and column in cmatrix
               # Calculate the individual value and assign to intersection
               nmatrix[i][j] += rmatrix[i][k] * cmatrix[k][j]
   return nmatrix

def det(matrix):
   add = 0
   for i in range(len(matrix)):
       if i % 2 == 1:
           matrix[0][i] *= -1 # Alternating scalar multiplication of submatrices, already setting it
   if len(matrix) == 1:
       return matrix[0][0]
   elif len(matrix) == 2:
       return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
   elif len(matrix) > 2:
       for i in range(len(matrix)):
           # Deal with submatrix split
           l = [[matrix[k+1][(i+j+1) % len(matrix)] for j in range(len(matrix))] for k in range(len(matrix)-1)] #submatrix
           add += matrix[0][i]*det(l) # Recursive way of calculating determinant
   return add

def eigenvalue(matrix): # This gives the right polynomial for eigenvalue calculations
   trA = 0
   for i in range(len(matrix)):
       trA += matrix[i][i]
   eigendecompoly = [det(matrix)]
   for i in range(len(matrix)-1):
       eigendecompoly.reverse()
       eigendecompoly.append(((-1)**(i))*trA)
       eigendecompoly.reverse()
   eigendecompoly.reverse()
   eigendecompoly.append((-1)**(len(matrix)))
   eigendecompoly.reverse()
   print(eigendecompoly)