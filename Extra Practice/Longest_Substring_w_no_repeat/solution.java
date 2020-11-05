
class Solution {
    //add my new solution
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        
       
        for (int i = 0 ; i < s.length() ; i ++){
            int count = 0 ; 
             ArrayList<String> str = new ArrayList<String>();
             str.add(s.substring(i,i+1));
            for (int j = i+1 ; j < s.length() ; j++){
                if (str.contains(s.substring(j,j+1))){
                    count++;
                    break;
                }
                else {
                    str.add(s.substring(j,j+1));
                }
            }
            if (str.size() > longest){
                longest = str.size();
            }
        }
        
        
        
        
        
        

        
           if (s.length() > 0 && longest == 0  ){
               return 1;
       }
        
        else{
         return longest;
               
        } 
        
            
        }
        
        
    }
