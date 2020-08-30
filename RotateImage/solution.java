class Solution {
    public void rotate(int[][] matrix) {
       int newRow = 0 ; 
        int newCol = 0 ;
        
        int [][] temp = twoClone(matrix);
         for (int col = 0 ; col < matrix.length ; col ++){
             for (int row = matrix.length-1 ; row > -1 ; row --){
                 matrix[newRow][newCol] = temp[row][col];
                 newCol++;
             }
            newCol = 0; 
             newRow++;
         }
     return;
   }
         
    
   

public static int[][] twoClone(int[][] a) {
    int[][] b = new int[a.length][];
    for (int i = 0; i < a.length; i++) {
      b[i] = a[i].clone();
    }
    return b;
  }
}