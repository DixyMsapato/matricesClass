# matricesClass
A simple class matrix class implemented in Python3
A simple class for matrices that is capable of the basic matrix operations, including;
-multiplication e.g A = theMatrix([[3,5],[6,7]]), B =theMatrix([[1,7],[2,1]]), the operator * is overloaded, so A * B is the matrix multiplication operator
-addition, A + B
-subtraction, A - B
-scalar multiplication,n * A, where n is an int or float. 
-transpositions on matrices of any size. At = A.transpose() creates a new theMatrix object with At.matrix being the transpose of A
For square matrices, the tranpose operation is defined. For 2x2 and 3x3 matrices, determinants and inversions are defined. 
To define a matrix A, the syntax is as in the following example, A =  theMatrix([[4,2,5],[3,6,9],[4,6,9]]), using lists of lists. There is a restriction on which lists of lists define matrices, in particular, the sublists must be of the same length. The basic attributes of theMatrix objects are, row number, column number and shape. 
