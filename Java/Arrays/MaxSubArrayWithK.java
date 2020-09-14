//Find Max Sum of Subarray of size K (Sliding Window Protocol) 
public class MaxSubArrayWithK {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int myArr[]= {4,2,1,7,8,1,2,8,1,0};
		int k=3;
		int mySum=0;
		int count=0;
		int globalSum=0;
		for(int i=0;i<myArr.length;i++) {
			
			mySum+=myArr[i];
			count+=1;
			
			if (count>=k) {
				if (mySum>globalSum) {
					globalSum=mySum;
				}
				mySum-=myArr[i-k+1];
			}
		
			
		}
				
	
		System.out.println(globalSum);
		
	}

}
