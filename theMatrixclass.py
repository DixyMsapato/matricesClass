

class theMatrix:
    def __init__(self, array, rowNum=0, colNum=0):
        rowNum = len(array)
        colNum = len(array[0])
        #number of rows
        self.rows = rowNum
        #number of columns
        self.cols = colNum
        #shape of arrya
        self.shape = (rowNum,colNum)



        #dimension check, to see that the entered array has the correct shape
        #The initial if statement checks the row number is correct
        #The second if the statement checks if the column number is correct
        if (rowNum == len(array)):
            checks = 0
            for i in range(0,len(array)):
                if len(array[i]) == colNum:
                    checks = checks + 1
            if checks == rowNum:
                #print("checks out")
                self.matrix = array
            else:
                print("entered array of the shape, it's not a matrix")
                self.matrix = None
        else:
            print("entered array of the shape, it's not a matrix")
            self.matrix = None

        #check the entries/data of the matrix is either int or floats
        for i in range(0,rowNum):
            for j in range(0,colNum):
                if (type(array[i][j]) == float) or (type(array[i][j]) == int):
                    #do nothing
                    pass
                else:
                    #print(array[i][j])
                    #print(type(array[i][j]))
                    print("Check that your matrix only has float or int entries")
                    self.matrix = None

    def display(self):
        print(self.matrix)



    #matrix addition
    #addition is only defined for matrices with the same shape
    #addition is component wise
    def __add__(self, other):
        if (self.shape == other.shape):
            #need to initialise a theMatrix object of the same shape for the sum
            sum = theMatrix([[0 for i in range(0,self.cols)] for j in range(0,self.rows)])
            for i in range(0,self.cols):
                for j in range(0,self.rows):
                    sum.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return sum
        else:
            print("The shape of the summands are not matched")
            return None
    #matrix subtraction
    #subtraction like addition is only defined for matrices of the same shape
    #also like addition, subtraction is defined component wise
    def __sub__(self, other):
        if (self.shape == other.shape):
            #initialise a sum object with zero matrix of shape self.shape
            difference = theMatrix([[0 for i in range(0,self.cols)] for j in range(0,self.rows)])
            for i in range(0,self.cols):
                for j in range(0,self.rows):
                    difference.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return difference
        else:
            print("The shape of the summands are not matched")
            return None

    #matrix multiplication
    #Matrix multiplication for matrices A,B where A.shape() = (m,n) and B.shape() = (p,q)
    #Matrix multiplication is defined iff n=p
    def __mul__(self, other):
        if (self.shape[1] == other.shape[0]):
            #initialise a product object with a zero matrix of shape (self.shape[0],other.shape[1])
            product = theMatrix([[0 for i in range(0,other.shape[1])] for j in range(0,self.shape[0])])
            m = product.rows
            q = product.cols
            n = self.shape[1]
            for i in range(0,m):
                for j in range(0,q):
                    for k in range (0,n):
                        product.matrix[i][j] = product.matrix[i][j] + (self.matrix[i][k]*other.matrix[k][j])
            return product
        else:
            print("The shapes of the multiplicands are mismatched")
            return None
    #scalar multiplication
    #scalar multiplication n*A where n is a real number and A a matrix
    def __rmul__(self, other):
        #first if statement to check the other argument is a real number
        if (type(other) == float) or (type(other) == int):
            multiple = copy.deepcopy(self)
            for i in range(0,self.rows):
                for j in range(0, self.cols):
                    multiple.matrix[i][j] = other*(multiple.matrix[i][j])
            return multiple
        else:
            return None


    #determinant for 2x2 or 3x3 matrices
    def determinant(self):
        if (self.shape == (2,2)) or (self.shape==(3,3)):
            #2x2 determinant calculation
            if self.shape == (2,2):
                return self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]
            #else do the 3x3 determinant calculation
            else:
                minor1 = self.matrix[1][1]*self.matrix[2][2] - self.matrix[1][2]*self.matrix[2][1]
                minor2 = self.matrix[1][0]*self.matrix[2][2] - self.matrix[1][2]*self.matrix[2][0]
                minor3 = self.matrix[1][0]*self.matrix[2][1] - self.matrix[1][1]*self.matrix[2][0]

                return self.matrix[0][0]*minor1 - self.matrix[0][1]*minor2 + self.matrix[0][2]*minor3
        else:
            return None

    #matrix transpose
    #Calculate the transpose of a matrix
    def transpose(self):
        #initialise zero matrix of transposed shape
        trans = theMatrix([[0 for i in range(0,self.rows)] for j in range(0,self.cols)])
        for i in range(0,self.cols):
            for j in range(0, self.rows):
                trans.matrix[i][j] = self.matrix[j][i]
        return trans

    #matrix trace for square matrix
    #calculate the trace of a square matrix of shape (n,n)
    def trace(self):
        traceVal = 0
        if self.shape[0] == self.shape[1]:
            for i in range(0, self.shape[0]):
                traceVal =  traceVal + self.matrix[i][i]
            return traceVal
        else:
            print("The trace is only defined for square matrices")
            return None

    #Cofactors
    #Calculate the matrix of cofactors for 3x3
    def cofactors(self):
        #check that the shape is a (3,3) matrix
        if (self.shape ==(3,3)):
            #initialise the matrix of cofactors
            cof = theMatrix([[0 for i in range(0, self.cols)] for j in range(0, self.rows)])
            #set the entries of the cofactor matrix with minors
            cof.matrix[0][0] = self.matrix[1][1]*self.matrix[2][2] - self.matrix[1][2]*self.matrix[2][1]
            cof.matrix[0][1] = (self.matrix[1][0]*self.matrix[2][2] - self.matrix[1][2]*self.matrix[2][0])*(-1)
            cof.matrix[0][2] = self.matrix[1][0]*self.matrix[2][1] - self.matrix[1][1]*self.matrix[2][0]
            cof.matrix[1][0] = (self.matrix[0][1]*self.matrix[2][2] - self.matrix[0][2]*self.matrix[2][1])*(-1)
            cof.matrix[1][1] = self.matrix[0][0]*self.matrix[2][2] - self.matrix[0][2]*self.matrix[2][0]
            cof.matrix[1][2] = (self.matrix[0][0]*self.matrix[2][1] - self.matrix[0][1]*self.matrix[2][0])*(-1)
            cof.matrix[2][0] = self.matrix[0][1]*self.matrix[1][2] - self.matrix[0][2]*self.matrix[1][1]
            cof.matrix[2][1] = (self.matrix[0][0]*self.matrix[1][2] - self.matrix[0][2]*self.matrix[1][0])*(-1)
            cof.matrix[2][2] = self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]

            return cof
        else:
            print("The shape of the matrix needs to be (3,3)")
            return None

    #Calculate the inverse of a matrix
    #Only when the matrix is 2x2 or 3x3
    def invMatrix(self):
        #check the matrix 2x2 or 3x3
        if (self.shape == (2, 2)) or (self.shape == (3, 3)):
            #2x2 case
            if self.shape == (2,2):
                #check the determinant is non-zero
                #if determinant is non-zero calculate the inverse matrix
                #otherwise return error message
                if self.determinant() != 0 :
                    #initialise a theMatrix object for the inverse
                    invMat = theMatrix([[0 for i in range(0,self.cols)] for j in range(0,self.rows)])
                    invMat.matrix[0][0] = self.matrix[1][1]
                    invMat.matrix[1][1] = self.matrix[0][0]
                    invMat.matrix[0][1] = self.matrix[0][1]*(-1)
                    invMat.matrix[1][0] = self.matrix[1][0]*(-1)

                    invMat = (1/self.determinant())*invMat
                    return invMat
                else:
                    print("The matrix cannot be inverted since it has 0 determinant")
                    return None
            else:
                # check the determinant is non-zero
                # if determinant is non-zero calculate the inverse matrix
                # otherwise return error message
                if self.determinant() != 0:
                    cofactorMatrix = self.cofactors()
                    return (1/self.determinant())*(cofactorMatrix.transpose())
                else:
                    print("The matrix cannot be inverted since it has 0 determinant")
                    return None
