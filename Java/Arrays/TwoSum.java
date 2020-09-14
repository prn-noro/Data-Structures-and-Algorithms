import java.util.HashMap;
public class TwoSum {
	
	public static int[] twoSum(int[] nums, int target) {
	        
	        HashMap<Integer,Integer> myMap = new HashMap<Integer,Integer>();
	        
	        for(int i=0;i<nums.length;i++){
	            int complement=target-nums[i];
	            
	            if (myMap.containsKey(nums[i])){
	                // int newArr[]={i,myMap.get(complement)};
	                // System.out.println(newArr);
	                return new int[] {i,myMap.get(nums[i])};
	            }
	            else{
	                myMap.put(complement,i);
	            }
	            
	        }
	        
	        return new int [] {0,0};
	        
	    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int myArr[]= {2,7,11,15};
		int target=9;
		int myAns[]=twoSum(myArr,target);
		for(int i=0;i<myAns.length;i++) {
			System.out.println(myAns[i]);
		}
		
	}

}
