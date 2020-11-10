
def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    zeroFirst = False
    indexSave = None
    #THIS WAS A DISCUSSION PYTHON SOLUTION AND I PUT SOME NOTES OVER IT FOR MYSELF
    for i in range(1,len(matrix)):
        for j in range(len(matrix[0])):
            #checking for zero in second to n rows
            if matrix[i][j] == 0:
                #marking top row col 
                matrix[0][j] = 0
                #marking end of row to zero dwon
                matrix[i][0] = 0   
    #checking for zeros in flagged rows or cols            
    for i in range(1,len(matrix)):
        #reverse loop to avoid flagging everything zero before the computations
        for j in range(len(matrix[0])-1,-1,-1):
            #checks for flags on rows or columns
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    #lastly finish on row 0   
    if firstRowHasZero:
        matrix[0] = [0]*len(matrix[0])
    return matrix                
