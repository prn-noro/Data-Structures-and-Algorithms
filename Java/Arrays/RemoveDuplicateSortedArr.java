//Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
//Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

public class RemoveDuplicateSortedArr {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int myArr[]= {1,2,2,3,3,4,4,5,5,5,6,7,7,7,8};
		
		int index=1;
		for(int i=1;i<myArr.length;i++) {
			
			if (myArr[i]!=myArr[i-1]) {
				myArr[index]=myArr[i];
				index+=1;
			}
		}
		for(int i=0;i<index;i++) {
			System.out.print(myArr[i] + " ");
		}
		
		
	}

}
