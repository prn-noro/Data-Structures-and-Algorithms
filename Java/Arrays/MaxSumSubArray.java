//Kadane's Algorithm


public class MaxSumSubArray {

	public static void main(String [] args) {
		int myArr[]= {-2, -3, 4, -1, -2, 1, 5, -3};
		
		int maxTillHere=0;
		int globalMax=-100000;
		
		for(int i=0;i<myArr.length;i++) {
			maxTillHere+=myArr[i];
			
			if (maxTillHere>globalMax) {
				globalMax=maxTillHere;
			}
			
			if(maxTillHere<0) {
				maxTillHere=0;
			}
		}
		
		
		System.out.println(globalMax);
	}
	
}
