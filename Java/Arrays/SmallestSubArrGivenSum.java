//Given an array of integers and a number x, find the smallest subarray with sum greater than the given value.

public class SmallestSubArrGivenSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int myArr[]= {1, 4, 45, 6, 10, 19};
		int targetSum=51;
		int localSum=0;
		int minWindSize=10000000;
		int left=0;
		int localWindSize;
		for(int i=0;i<myArr.length;i++) {
			localSum+=myArr[i];
			
			while (localSum>=targetSum) {
				localWindSize=i-left+1;
				localSum-=myArr[left];
				left+=1;
				if(localWindSize<minWindSize) {
					minWindSize=localWindSize;
				}
				
			}
		}
		
		System.out.println(minWindSize);

	}

}
