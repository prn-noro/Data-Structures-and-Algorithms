
public class CountOnes {
	 public static int findMaxConsecutiveOnes(int[] nums) {
	        int flag=0;
	        int maxCount=0;
	        int currCount=0;
	        for(int i=0;i<nums.length;i++){
	            currCount=0;
	            flag=0;
	            for(int j=i;j<nums.length;j++){
	                if(nums[j]==0 && flag==0){
	                    currCount+=1;
	                    flag=1;
	                }
	                else if(nums[j]==1){
	                    currCount+=1;
	                }
	                else{
	                 if(currCount>maxCount){
	                     maxCount=currCount;
	                    }   
	                    break;
	                }
	            }
	        }
	        
	        return maxCount;
	    }
	 
	 public static void main(String [] args) {
		 int nums[]= {1,0,0,0,1,1,0,1,0,1,0};
		 int maxCount=findMaxConsecutiveOnes(nums);
		 System.out.println(maxCount);
	 }
}
   