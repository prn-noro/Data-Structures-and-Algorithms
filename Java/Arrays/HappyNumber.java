import java.util.HashSet;

class Solution {
    public boolean isHappy(int n) {
        
        HashSet<Integer> mySet=new HashSet<Integer>();
       
        mySet.add(n);
        while (true){
            int sumSquare=0;
            while(n>0){
                int lastDigit=n%10;
                sumSquare+=lastDigit*lastDigit;
                n=n/10;
            }
            if (sumSquare==1){
                return true;
            }
            else if (mySet.contains(sumSquare)){
                return false;
            }
            else{
                mySet.add(sumSquare);
                n=sumSquare;
            }
        
        }
    }
}