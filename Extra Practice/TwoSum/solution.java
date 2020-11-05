class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] returnArray = new int[2];
        for (int i = 0 ; i < nums.length ; i++){
            for (int j = 0 ; j < nums.length;j++){
                if (nums[i] + nums[j] == target && i != j){
                    // if (i> j ){
                    returnArray [0] = j;
                     returnArray[1] = i;
                    // }
                    // else if (j > i ) {
                    // returnArray [0] = i;
                    // returnArray[1] = j;  
                    // }
                }
            }
        }
        return returnArray;
    }
}