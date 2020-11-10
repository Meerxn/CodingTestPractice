
def setZeroes(matrix):
    """
    The main idea was to flag the first col or first row with zeros while iterating over rows 2---n 
    after that we again to a loop to check for those zeros and flag the appropriate bits. Once we finish this we 
    finally add our zeros to the first row as the other rows depend on the first rows and cols
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
